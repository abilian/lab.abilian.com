**Goal:** To demystify time series forecasting, moving beyond simple trend lines to build robust, insightful models. We will cover key techniques for feature engineering, model adaptation, and evaluation specific to temporal data. Where applicable, we'll note how libraries like `pandas` and `skrub` can streamline these processes.

## The tutorial

### 1. Crafting Time-Structured Features

Raw time series data (e.g., daily sales) often requires significant feature engineering to reveal patterns, seasonality, and dependencies that machine learning models can leverage.

1.  **Temporal Resampling:**
    *   **Concept:** Adjusting the time frequency of your data.
    *   **Why?** Data might be too granular (e.g., per-second readings when hourly forecasts are needed) or not granular enough. It's also used to align series with different native frequencies.
    *   **Techniques (typically using `pandas`):**
        *   **Downsampling:** Aggregating data to a lower frequency (e.g., daily to weekly using `df.resample('W').sum()`). Common aggregations include mean, sum, median, min, max.
        *   **Upsampling:** Increasing data frequency (e.g., daily to hourly using `df.resample('H').interpolate()`). This usually involves an interpolation strategy like forward/backward fill or linear interpolation.
    *   *Pipeline Integration:* These `pandas` operations can be encapsulated within custom transformers or `skrub.deferred` functions to become part of a reproducible machine learning pipeline (e.g., a `skrub` pipeline).

2.  **Temporal Merges & Joins (Enriching Time Series with External Data):**
    *   **Concept:** Combining your primary time series with other relevant data sources, which might include other time series or static features. Timestamps and join keys may not align perfectly.
    *   **Why?** External factors often influence time series. For instance, sales data could be enriched with weather information, marketing campaign schedules, or economic indicators.
    *   **Techniques & Tools:**
        *   **Exact Joins (e.g., `pandas.merge`):** For when timestamps or other keys align perfectly.
        *   **Approximate ("Fuzzy") Joins (e.g., `skrub.fuzzy_join` or `skrub.Joiner`):** Useful if time-based keys (like week numbers) or descriptive keys (like location names) have minor discrepancies.
            *   *Example:* Joining daily sales to a weekly marketing spend table by matching to the closest week start.
        *   **Interpolation-Based Joins (e.g., `skrub.InterpolationJoiner`):** Very powerful for spatio-temporal data. If you have sparse auxiliary data (e.g., weather readings from stations not at your exact location/time), this can *infer* the value of an auxiliary variable at the precise time and location of your main series' observations.
            *   *Example:* Predicting temperature at an airport for a flight's departure time, using data from nearby weather stations that report at different times.
        *   **Aggregate-then-Join (e.g., `skrub.AggJoiner`):** If you have high-frequency auxiliary data (e.g., hourly website clicks) and a lower-frequency main series (e.g., daily sales), you can aggregate the auxiliary data (e.g., total daily clicks) *before* joining it to your main series.
    *   *Pipeline Integration:* Join operations, especially complex ones like those offered by `skrub`'s joiners, benefit from being part of a stateful pipeline to ensure correct application during training and inference.

3.  **Calendar Features:**
    *   **Concept:** Extracting structured features directly from the date/time index or columns.
    *   **Why?** Time series often exhibit strong patterns based on calendar cycles (e.g., day of week, month, holidays).
    *   **Features:** Year, month, day of week, day of year, week of year, hour, season, is_weekend, is_holiday, etc.
    *   **Tools:**
        *   **`pandas` datetime accessors:** (e.g., `df.index.month`, `df.index.dayofweek`).
        *   **`skrub.DatetimeEncoder`:** This transformer automatically breaks down datetime columns into a comprehensive set of numerical calendar features. It can also generate periodic encodings (e.g., sine/cosine transformations for cyclical features like month or hour), which are particularly useful for linear models and help tree-based models capture cyclicity effectively. It's often used within `skrub.TableVectorizer`.

4.  **Lag Features:**
    *   **Concept:** Using past values of the target variable (autoregressive features) or other exogenous variables as features for predicting the current or future value.
    *   **Why?** The state of a time series at a previous point often influences its current or future state (autocorrelation).
    *   **Techniques (typically using `pandas.DataFrame.shift()`):**
        *   `y(t-1)`: Value of the target at the previous time step.
        *   `y(t-k)`: Value of the target `k` steps ago (e.g., `y(t-7)` for daily data with weekly seasonality).
        *   Lags of exogenous variables (e.g., marketing spend from the previous month).
    *   *Pipeline Integration:* Once created, these lagged columns become regular numerical features that can be processed by tools like `skrub.TableVectorizer`.

5.  **Aggregate Features over Rolling Windows:**
    *   **Concept:** Calculating summary statistics (e.g., mean, median, standard deviation, min, max, sum) over a moving ("rolling") window of past data points.
    *   **Why?** Helps capture recent trends, local volatility, or other dynamic patterns in the series.
    *   **Techniques (typically using `pandas.DataFrame.rolling().agg()`):**
        *   `rolling_mean_7_days`: Average value over the past 7 days.
        *   `rolling_std_30_days`: Standard deviation over the past 30 days (a measure of recent volatility).
    *   *Pipeline Integration:* Similar to lag features, these rolling aggregates become standard input columns for downstream processing.

### 2. Adapting Tabular Models for Forecasting

Many state-of-the-art machine learning models (like Gradient Boosted Trees, Random Forests, or linear models) are designed for tabular data. With proper feature engineering, they can be powerful forecasters.

1.  **The Core Idea: Transform to Supervised Learning:**
    *   The goal is to predict a target variable `y(t)` at time `t`.
    *   The features `X(t)` consist of all the time-structured features engineered in Part 1 (lags, calendar features, rolling aggregates, relevant external data, etc.).
    *   The tabular model learns the mapping: `X(t) -> y(t)`.

2.  **Automated Preprocessing for Tabular Models:**
    *   Once you've created your comprehensive feature set (including temporal features), tools like **`skrub.TableVectorizer`** can automate the final preprocessing steps.
    *   It detects column types (numeric, categorical—including those derived from calendar features like 'day_of_week_name') and applies appropriate transformations (e.g., scaling for numerics, one-hot encoding for categoricals). Its internal `DatetimeEncoder` handles any raw date columns.
    *   The output is a numerical matrix ready for any scikit-learn compatible estimator.
    *   For quick model building, **`skrub.tabular_learner`** can create a full pipeline (e.g., `TableVectorizer` + `HistGradientBoostingRegressor`) from your feature-engineered DataFrame.

3.  **Managing Complex Data Flows:**
    *   For advanced scenarios involving multiple temporal data sources requiring intricate preprocessing and joining *before* the final feature set is assembled, pipeline frameworks like **`skrub` expressions** (`skrub.var`, `.skb.apply()`, `skrub.choose_from()`) allow defining complex, stateful, and tunable data processing graphs.

### 3. Pitfalls of Recursive Forecasting & Alternatives

A common approach is to train a model to predict only one step ahead (`t+1`) and then use its own predictions recursively to forecast further.

1.  **The "t+1" Regressor:** You train a model `ŷ(t+1) = model(features_at_t)`.
2.  **Recursive Forecasting:** To predict `ŷ(t+2)`, you use `ŷ(t+1)` as if it were an actual observation to construct features for time `t+1`. This process is repeated for `t+3`, `t+4`, ..., up to the desired forecast horizon `H`.
3.  **The Pitfall: Error Accumulation.** Any error in `ŷ(t+1)` is fed back into the model as input for predicting `ŷ(t+2)`. These errors can compound, leading to increasingly unreliable forecasts further into the horizon.
4.  **Alternatives to Recursive Forecasting:**
    *   **Direct Forecasting (or Multi-Output Forecasting):**
        *   Train separate models for each step `h` in the forecast horizon: `model_h` predicts `ŷ(t+h)` directly from `features_at_t`.
        *   Alternatively, use a multi-output regressor that simultaneously predicts `[ŷ(t+1), ŷ(t+2), ..., ŷ(t+H)]` from `features_at_t`.
    *   **DIRMO (Direct Multi-Horizon Forecasting):** Train a single model to predict `y(t+h)` where `h` (the forecast step, e.g., 1 to H) is itself a feature: `ŷ(t+h) = model(features_at_t, h)`.
    *   *Note:* All these strategies still rely on a well-prepared feature matrix `features_at_t`.

### 4. Sound Prediction Intervals (Beyond Point Estimates)

A single point forecast (e.g., "sales will be $1000") is often insufficient. Quantifying the uncertainty around this forecast is crucial.

1.  **What are Prediction Intervals (PIs)?**
    *   A range `[lower_bound, upper_bound]` within which the true future value is expected to lie with a certain probability (e.g., 95%).
    *   Example: "We are 95% confident that sales will be between $800 and $1200."

2.  **Methods to Generate PIs (using models trained on appropriately prepared data):**
    *   **Quantile Regression:** Train models to predict specific quantiles of the future distribution (e.g., the 2.5th and 97.5th percentiles for a 95% PI). Gradient Boosted Trees, for instance, can be configured with a quantile loss function.
    *   **Bootstrapping Residuals:** After training a point forecasting model, collect its residuals (actual - predicted) on a hold-out set. For a new forecast, repeatedly sample from these residuals, add them to the point forecast to create an empirical distribution, and then take percentiles of this distribution.
    *   **Conformal Prediction:** A model-agnostic framework that can provide PIs with statistical coverage guarantees under certain assumptions.
    *   **Model-Specific Uncertainty:** Some models (e.g., Bayesian models, Gaussian Processes) inherently output uncertainty estimates that can be converted into PIs.

## 5. Methodologically Sound Model Selection & Evaluation

Evaluating forecasting models requires care to avoid data leakage from the future into the past.

1.  **Time-Structured Cross-Validation:**
    *   **The Problem with Standard CV:** Randomly splitting time series data allows the model to "see the future" during training (e.g., training on data from `t+k` to predict `t`), leading to overly optimistic performance estimates.
    *   **Solution (Respecting Temporal Order):** Use cross-validation schemes that preserve the temporal sequence.
        *   **`sklearn.model_selection.TimeSeriesSplit`** is a standard implementation. It creates folds where the training set always precedes the test set. Variations include expanding windows (training set grows) or rolling windows (training set slides).
    *   *Pipeline Integration:* When using pipeline tools (e.g., `skrub` expressions for hyperparameter search with `.skb.get_grid_search()`), ensure you pass a time-aware splitter like `TimeSeriesSplit` as the `cv` argument.

2.  **Informative Evaluation Metrics:**
    *   **For Point Estimates:**
        *   MAE (Mean Absolute Error), RMSE (Root Mean Squared Error).
        *   MAPE (Mean Absolute Percentage Error) - use with caution (issues with zero actuals, asymmetry).
        *   MASE (Mean Absolute Scaled Error) - compares forecast to a naive (e.g., seasonal random walk) baseline.
    *   **For Prediction Intervals:**
        *   **Prediction Interval Coverage Probability (PICP):** Percentage of actual values falling within the PIs. For 95% PIs, PICP should be close to 95%.
        *   **Mean Prediction Interval Width (MPIW):** Average width of PIs. Narrower is better, *given good coverage*.
        *   **Winkler Score (or Interval Score):** A "strictly proper scoring rule" that simultaneously penalizes for poor coverage and overly wide intervals.
    *   **For Probabilistic (Distributional) Predictions:**
        *   **Continuous Ranked Probability Score (CRPS):** Generalizes MAE for probabilistic forecasts. A strictly proper scoring rule; lower is better.
        *   **Log-Likelihood/Log Score:** For models outputting full predictive distributions.
    *   *"Strictly Proper Scoring Rules"* are desirable as they are uniquely optimized when the forecast matches the true underlying probability distribution, encouraging honest and well-calibrated probabilistic forecasts.

### 6. Diagnosing & Mitigating Bias (Especially for Extremes)

Models often struggle with extreme values, potentially systematically under- or over-predicting them.

1.  **Reliability Diagrams (for Probabilistic Forecasts/Quantiles):**
    *   **Concept:** Plot the observed frequency of an event (or actual values falling below a certain quantile) against the forecast probability (or predicted quantile).
    *   **How it works (example for quantiles):** If you predict the 10th percentile, ideally 10% of actual future values should fall below this predicted 10th percentile. If, for instance, only 5% of actuals fall below your predicted 10th percentile, your model is systematically overestimating this quantile (i.e., not predicting values low enough).
    *   **Interpretation:** A perfectly calibrated model has its reliability curve along the diagonal. Deviations indicate bias.

2.  **Strategies to Mitigate Bias:**
    *   **Recalibration:** Post-process model outputs (e.g., using isotonic regression for quantiles) based on observed biases on a calibration set.
    *   **Model Adjustments:** Consider different loss functions (e.g., to penalize errors on extremes more heavily), engineer features specifically designed to capture drivers of extremes, or transform the target variable (e.g., log transform for skewed data).
    *   **Separate Models for Extremes:** Sometimes, modeling "normal" behavior and "extreme" behavior with distinct models can be effective.

## Practical Considerations (Real-World vs. Synthetic Data)

*   **Real-World Data:** Often messy (missing values, outliers, structural breaks like policy changes or pandemics, evolving seasonality).
    *   Initial cleaning (e.g., with `skrub.Cleaner` for obvious nulls and date parsing) is often necessary.
    *   If categorical features exist alongside the time series (e.g., store IDs, product types) and have inconsistencies, tools like `skrub.deduplicate` can be helpful.
*   **Synthetic Data:** Useful for isolating specific problems and understanding model behavior under controlled conditions (e.g., to demonstrate catastrophic pitfalls of recursive forecasting or issues with specific CV methods).

## Key Takeaways

1.  **Feature Engineering is King:** Lags, rolling statistics (often via `pandas`), calendar features (e.g., via `skrub.DatetimeEncoder`), and joined external data (e.g., via `skrub` joiners or `pandas.merge`) are crucial.
2.  **Tabular Models are Versatile Forecasters:** With appropriate time-aware features, standard ML models can be very effective. Tools like `skrub.TableVectorizer` can then prepare this data for `scikit-learn`.
3.  **Beware Recursive Forecasting Pitfalls:** Understand its limitations and consider direct forecasting strategies.
4.  **Quantify Uncertainty:** Prediction intervals provide a more complete picture than point forecasts.
5.  **Evaluate Rigorously:** Use time-structured cross-validation (e.g., `TimeSeriesSplit`) and appropriate, ideally proper, scoring rules.
6.  **Diagnose Your Model:** Actively look for systematic biases, especially for extreme values.

## Your "Homework"

*   Explore `pandas` for time series resampling, generating lag features (`.shift()`), and calculating rolling window statistics (`.rolling()`).
*   Take a time series dataset:
    *   Identify potential calendar features and try extracting them using `pandas` datetime accessors or `skrub.DatetimeEncoder`.
    *   If you have auxiliary temporal data, consider how it could be merged or joined.
    *   Construct a feature set and use `skrub.TableVectorizer` to prepare it for a `scikit-learn` model.
*   Familiarize yourself with `sklearn.model_selection.TimeSeriesSplit` and think about how you would use it to evaluate a forecasting model.

## References

- [Skrub pour préparer efficacement vos données : une solution Python pour le machine learning](https://www.stat4decision.com/fr/skrub-preparer-donnees-python-ml/) (2025)

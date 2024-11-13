## What Makes a Good Prompt?

A good prompt provides the model with clear and detailed instructions, guiding it to deliver the desired output. It must be specific enough to prevent ambiguous results but flexible enough to allow the model to function creatively within the scope defined. Below are some principles for designing effective prompts.

### Be Clear and Specific When Prompting
When interacting with LLMs, clarity is critical. Avoid vague language, implicit assumptions, or unnecessarily complicated phrasing. Clearly define what you expect from the model. Specific instructions increase the likelihood of receiving accurate and useful results.

**Example:**
- Poor Prompt: "Explain how LLMs work."
- Improved Prompt: "Provide a brief explanation of how transformer-based language models work, focusing on self-attention and token embeddings."

### Using Delimiters
Delimiters can be helpful to structure the input and make it easier for the model to understand different parts of the query. You can use quotes, brackets, or other symbols to demarcate boundaries for specific instructions or examples.

**Example:**
- "Summarize the following article in 100 words: ``` The rise of AI models has revolutionized the field of natural language processing. LLMs, such as GPT, are based on transformer architectures...```"

### Specifying Output Length
You may want the response to fit within certain constraints, especially when dealing with specific formats or platforms. By specifying the desired length, the LLM can adjust its output accordingly.

**Example:**
- "Summarize this article in no more than 200 words."
- "Write a 50-word product description for an AI-powered chatbot."

### Output Format
In many use cases, the output needs to adhere to a specific structure, whether it’s a table, bullet points, JSON, or code. Specifying the desired output format is crucial for tasks that require structured data.

**Example:**
- "Generate a list of five key features of open-source software, formatted as bullet points."
- "Provide the output in JSON format with keys 'feature' and 'description'."

### Split Complex Tasks into Subtasks
When requesting complex information, it's better to break the task into smaller, more manageable components. This not only simplifies the model’s task but also allows you to review and refine the output for each subtask.

**Example:**
- Instead of asking: "Explain the key components of a machine learning pipeline and how they interact with each other."
- Use: "First, explain the data preprocessing step in a machine learning pipeline. Next, describe the model training process. Finally, explain how the model evaluation is performed."

## Introduction to Few-Shot Prompting

Few-shot prompting is a powerful technique used with large language models (LLMs) where you provide a few examples (demonstrations) of the desired input-output behavior within the prompt. The model learns from these examples to generalize the task and produce appropriate outputs for new inputs. This technique is useful when you want to improve the model’s ability to perform specific tasks without additional training or fine-tuning.

Few-shot prompting bridges the gap between "zero-shot" (no examples provided) and "fine-tuning" (adjusting the model's parameters). It leverages the model's ability to adapt based on patterns in the examples, enabling it to perform complex or domain-specific tasks with limited input.

### How Many Demonstrations?

The number of examples you provide directly influences the model's output quality. However, there are trade-offs to consider:

1. **Too Few Demonstrations:** With fewer examples, the model might not fully capture the desired task, leading to suboptimal or inconsistent results.
2. **Too Many Demonstrations:** Overloading the model with too many examples might confuse it or make the prompt too long, which can result in less coherent outputs or even memory/processing limits on the model.

The optimal number of demonstrations depends on factors such as:
- **Task complexity:** Simpler tasks may only need 1-2 examples, while more complex tasks might require 3-5 examples.
- **Model size and capacity:** Larger models typically handle more examples better.
- **Desired outcome specificity:** If you need highly accurate or structured output, more examples may help.

A good rule of thumb is to start with 1-3 examples and experiment to find the balance that works best for the specific task.

**Example of Few-Shot Prompting:**

*Task: Classify sentences as positive or negative sentiment.*

- Input: "The movie was amazing!"
- Output: "Positive"

- Input: "I didn’t enjoy the film."
- Output: "Negative"

- Input: "The plot was dull."
- Output: "Negative"

- Now, ask the model to classify a new input based on these demonstrations:
  - "The acting was incredible."

### Tips for Preparing Demonstrations

Effective demonstrations are key to good results in few-shot prompting. Here are some tips to consider when preparing examples:

1. **Diverse Examples:** Ensure that your demonstrations cover a variety of cases within the task domain. For instance, when performing text classification, show both positive and negative examples.

2. **Clear Structure:** Maintain a consistent structure across examples. Each demonstration should follow a predictable pattern (e.g., input → output), so the model understands how to generalize the task.

3. **Context Relevance:** Choose examples that closely match the type of inputs the model will handle in the task. Avoid using examples that are too dissimilar, as this may confuse the model.

4. **Avoid Overfitting:** If you use too few or overly specific examples, the model may overfit to those and fail to generalize. Use a broad enough range of examples to prevent this.

5. **Input Length Considerations:** Be mindful of token limits. If you provide too many examples, it may result in the model truncating or ignoring part of the prompt, especially if the input itself is long.

**Example of Diverse Demonstrations:**

*Task: Identifying the type of animal based on descriptions.*

- Input: "It has a long neck and eats leaves from tall trees."
- Output: "Giraffe"

- Input: "This animal swims in the ocean and has sharp teeth."
- Output: "Shark"

- Input: "It hops and carries its young in a pouch."
- Output: "Kangaroo"

Providing examples from various animal types will help the model generalize better when given new inputs.

### Quiz

**Q1.** What is the key difference between few-shot and zero-shot prompting?
- a) Few-shot uses a pre-trained model, while zero-shot requires a fine-tuned model.
- b) Few-shot uses examples to demonstrate the task, while zero-shot does not use any examples.
- c) Zero-shot is more effective than few-shot prompting in all cases.

*Correct Answer:* b) Few-shot uses examples to demonstrate the task, while zero-shot does not use any examples.

**Q2.** What is a potential downside of using too many demonstrations in a prompt?
- a) The model might generalize the task too well.
- b) The model might struggle with processing due to length limits or become confused by conflicting examples.
- c) It will always improve output quality, so there are no downsides.

*Correct Answer:* b) The model might struggle with processing due to length limits or become confused by conflicting examples.

**Q3.** When crafting demonstrations, what is an important factor to consider?
- a) The demonstrations should be as vague as possible to allow the model flexibility.
- b) The demonstrations should cover diverse cases within the task domain to improve generalization.
- c) You should always provide at least 10 examples to maximize accuracy.

*Correct Answer:* b) The demonstrations should cover diverse cases within the task domain to improve generalization.

**Q4.** Which of the following is a good practice when preparing a demonstration for a classification task?
- a) Using examples that only show one type of class (e.g., all positive sentiment).
- b) Ensuring that all examples follow a clear and consistent format.
- c) Overloading the model with as many examples as possible.

*Correct Answer:* b) Ensuring that all examples follow a clear and consistent format.

## References

- https://www.promptingguide.ai/
- https://llmnanban.akmmusai.pro/Book/LLM-Prompt-Engineering-Simplified-Book/

<!-- Keywords -->
#sentences
<!-- /Keywords -->

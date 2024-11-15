## Tutorials

- https://rust-exercises.com/
- https://doc.rust-lang.org/book/title-page.html
- https://fasterthanli.me/articles/a-half-hour-to-learn-rust (2020)
- https://www.scotto.me/blog/rust-101/?utm_source=pocket_saves
- https://www.shuttle.dev/blog/2024/02/08/uptime-monitoring-rust

## Rust + Python

- https://pythonspeed.com/articles/intro-rust-python-extensions?utm_source=pocket_shared
- https://rust-exercises.com/rust-python-interop/
- https://towardsdatascience.com/nine-rules-for-writing-python-extensions-in-rust-d35ea3a4ec29

From the post above:

1. Create a single repository containing both Rust and Python projects
2. Use maturin & PyO3 to create Python-callable translator functions in Rust
3. Have the Rust translator functions call “nice” Rust functions
4. Preallocate memory in Python
5. Translate nice Rust error handling into nice Python error handling
6. Multithread with Rayon and ndarray::parallel, returning any errors
7. Allow users to control the number of parallel threads
8. Translate nice dynamically-type Python functions into nice Rust generic functions
9. Create both Rust and Python tests

## Cons of Rust

- https://scribe.rip/using-rust-at-a-startup-a-cautionary-tale-42ab823d9454
    - "Rust has a huge learning curve."
    - "Rust has made the decision that safety is more important than developer productivity"
    - "Rust makes roughing out new features very hard."

#rust

<!-- Keywords -->
#rust
<!-- /Keywords -->

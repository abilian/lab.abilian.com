#hr #internship 

## Source code

- Not available yet.

## Internship

- <https://abilian.com/fr/a-propos/jobs/stage-compilation-python/>

## Références

- [[Python & WASM]]
- [[Compilation Python]]
- [[Compilers]]

## Challenges / open questions

- Identifying good use cases and trade-offs

- Efficient and agile methods for AST transformation (tree rewriting techniques à la Stratego/XT)

- Should we generate WASM directly, or use a IR (à la LVM) ?
    - Benefits of using an IR: 

- WASM runtime
    - A lot of things (strings, lists, dicts, even floats?) need to be reimplemented on top of the very primitive types supported by WASM
    - Browser interface and access to the plateform (WASI)

- All the usual challenges linked to compiling a dynamic language
    - See https://stefan-marr.de/2020/06/efficient-and-safe-implementations-of-dynamic-languages/ for a recent state-of-the-art presentation

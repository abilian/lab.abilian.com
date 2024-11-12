#public

## Source code

- Not available yet.

## Internship

- <https://abilian.com/fr/a-propos/jobs/stage-compilation-python/>

## Références

- [[Python & WASM]]
- [[Compiling Python]]
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

## Narrative

The development of a Python to WebAssembly (WASM) compiler presents a significant opportunity in web development. The project aims to bring the ease and versatility of Python into the secure and universally supported environment of web browsers. While the source code is not yet available, the project has gained attention, with internship opportunities focused on its development.

Challenges:

1. Identifying suitable use-cases and trade-offs for Python within a WASM runtime.
2. Implementing efficient Abstract Syntax Tree (AST) transformations, potentially using techniques like Stratego/XT.
3. Deciding between generating WASM directly or using an Intermediate Representation (IR) for flexibility and adaptability.
4. Reimplementing Python's standard library to fit into WASM's primitive type system.
5. Interfacing with the browser and other platforms through WebAssembly System Interface (WASI).
6. Compiling a dynamic language like Python, which has been explored in state-of-the-art presentations.

Opportunities:

1. Redefining web capabilities by bridging the gap between server-side logic and client-side execution.
2. Developing more efficient applications with lower server loads.
3. Ushering in a new era of web development with increased flexibility and power.

The Python to WASM compiler project presents both technical challenges and the potential for a paradigm shift in web development. Its success could lead to a more integrated and powerful web experience. The project is actively seeking contributions, with internship positions available for those interested in being part of this groundbreaking work.

<!-- Keywords -->
#compilers #compiler
<!-- /Keywords -->

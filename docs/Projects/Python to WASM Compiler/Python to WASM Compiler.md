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

In the ever-evolving landscape of web development, the concept of a Python to WebAssembly (WASM) compiler is like a breath of fresh air. It's an idea whose time has come, not just as an academic exercise but as a genuine need for a multitude of potential use-cases. Imagine the power of Python—its ease, its libraries, its community—transplanted into the nimble, secure, and universally supported environment of the web browser. It's not just bringing Python to the browser; it's about redefining what we can do on the web.

Though the source code isn't available yet, there's already momentum building, highlighted by internship opportunities focused on this very project. This suggests that there's a serious commitment to tackle the inherent challenges and open questions that accompany such a bold endeavor.

So, what are these challenges? First off, there's the question of identifying the right use-cases and trade-offs. Python is known for its versatility, but where does it shine the brightest when constrained within a WASM runtime? Could it be for data analytics right within your browser, or perhaps the development of more robust client-side applications? The possibilities are both exciting and need careful pondering.

Then comes the technical prowess needed for Abstract Syntax Tree (AST) transformations, drawing inspiration from techniques like Stratego/XT. This is not just about a straightforward compilation; it's about agile, efficient methods to make the transformation as seamless as possible.

Another thought-provoking question is whether to generate WASM directly or to use an Intermediate Representation (IR), similar to LLVM. Opting for an IR could offer more flexibility and could make the compiler adaptable to future changes in both Python and WASM ecosystems.

The WASM runtime presents its own set of hurdles. We're talking about reimplementing much of Python's rich standard library—from strings and lists to dictionaries and possibly even floats—all to fit into the WASM's more primitive type system. Not to mention the need to interface seamlessly with the browser and potentially other platforms through WebAssembly System Interface (WASI).

Lastly, there's the ever-daunting challenge of compiling a dynamic language like Python, a subject that has been explored in-depth, as evidenced by the state-of-the-art presentations in the field.

The project doesn't just stand as a technical challenge but as a paradigm shift. If successful, it could redefine what we consider "web capabilities," bridging the gap between server-side logic and client-side execution in a way that's more integrated than ever before. This could result in more efficient applications, lower server loads, and a new era of web development.

In summary, a Python to WASM compiler isn't just a tool; it's a vision of a more powerful, more flexible web. The challenges are many, but so are the opportunities. And if you're intrigued enough, there are even internship positions to be a part of this groundbreaking work.

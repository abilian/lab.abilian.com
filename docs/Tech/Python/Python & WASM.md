## Why ? (Some use cases)

- Template engine that works both on server and browser
- Apps that work "on the edge" (e.g. Cloudflare -> need to better understand the technology involved)

- Discussion w/ Paul Everitt:
  
> (From 2019): Russell’s talk has a very good analogy about “winged keel” in yacht racing, which he applies to WASM. On the other hand, it isn’t clear how it will manifest. Lukazs makes a strong case that we shouldn’t do the Python runtime in the browser, but should translate to as native WASM as we can on the server in a build step.  
> Namely, we’ll never get 60 fps in the browser if there’s a Python runtime and compiler there, even in WASM.
> Lukazs mentioned Cython but was more interested in mypyc as part of a toolchain that generated WASM. Any thoughts?

> (Dec. 2021): OTOH, I *really* would like to leave the door open to generate client-side template logic that can work in either server-side Python or client-side JS/WASM. Jinja has a language which isn’t Python. It’s an AST of expressions.
> I think it’s too early to tell if wasmer for Python will be viable to live with. But it’s fun to imagine a WASM-based engine that worked in Python and the browser, with templating and the things that go with it — state model, injection, etc.

- Discussion with Robert Smallshire regarding this: https://twitter.com/robsmallshire/status/1477004769298456580

> Me: "On the other hand, one could imagine a compiler from Python (or a subset of Python) to WASM, which could open new perspectives in terms of web development. There are precedents (Brython, Pyjs, Pyjamas, Transcript, etc.), some of which seem to meet concrete needs. It would be necessary to understand in what way compilation towards WASM would bring something more than compilation towards JavaScript."

- Full-stack web app, à la: https://www.sheshbabu.com/posts/rust-wasm-yew-single-page-application/

## Issues / limitations

- Need for a runtime. Hopefully small (but probably won't be). How can that be competitive with a JS program that can tap freely into the JS runtime ?

## Examples / inspiration

- List of languages that run on WASM (not all compiled): https://github.com/appcypher/awesome-wasm-langs
- JS port of Micropython: https://github.com/micropython/micropython/tree/master/ports/javascript (not a compiler)
- "Cheerp - a C/C++ compiler for Web applications - compiles to WebAssembly and JavaScript" -> https://github.com/leaningtech/cheerp-meta - https://leaningtech.com/cheerp/
- AssemblyScript = variant of Typescript with Binaryen as the backend. Large project.

### Recent (2022/04) links

- https://speakerdeck.com/tiran/language-summit-2022-webassembly-python-in-the-browser-and-beyond "Language Summit 2022: WebAssembly: Python in the browser and beyond"
- https://github.com/pyscript/pyscript "PyScript is a Pythonic alternative to Scratch, JSFiddle or other "easy to use" programming frameworks, making the web a friendly, hackable, place where anyone can author interesting and interactive applications."
- https://wazero.io/ "wazero: the zero dependency WebAssembly runtime for Go developers. WebAssembly is a way to safely run code compiled in other languages. Runtimes execute WebAssembly Modules (Wasm), which are most often binaries with a .wasm extension. wazero is the only zero dependency WebAssembly runtime written in Go."

### Update 2023/04

- **Micropython**/webassembly could be a solution but needs more documentation.
    - cf. https://github.com/rafi16jan/micropython-wasm for some hints
    - `firmware.wasm` is 1MB (430 MB gzipped)
    - One needs something like https://github.com/rafi16jan/micropython-wasm/blob/master/js.py for JS<>Python interop.
    - No docs.

## References

- https://tomassetti.me/wasi-how-to-run-webassembly-code-outside-of-your-browser/
- (Books about WebAssembly)

## Potential leads

### Compiler technologies

- https://github.com/WebAssembly/binaryen (Compiler infrastructure and toolchain library for WebAssembly - in C++)
    - There is a Python binding: https://pypi.org/project/pybinaryen/
- [PPCI](https://github.com/windelbouwman/ppci) - has a WASM backend. Not active currently.
- [MIR](https://github.com/vnmakarov/mir) (NB: no WASM support currently)
- [QBE Intermediate Language](https://c9x.me/compile/doc/il.html) (No WASM backend).

### Tiny python compilers (all abandonned)

- github.com/philhassey/tinypy
- github.com/alehander92/Airtight
- gitlab.com/hartsantler/tpythonpp

→ Renovate + add WASM backend ?

## Dev log

### 2021/10/01: playing with PPCI again
New repo with some experiments: <https://github.com/abilian/ppci-sandbox>

### 2020/12/21: Simple WASM experiment

A tiny subset of Python can be compiled to WASM using PPCI:

- Install PPCI <https://pypi.org/project/ppci/>
- Write a Python module (`mandelbrot.py`) with only one function, no annotation, only simple arithmetics
- Use `ppci.lang.python.python_to_wasm`
- Run it wih `wasmer run playground/mandelbrot.wasm -i mandelbrot`

=> Result: quite fast (300ms vs. 180ms for the C version).

TODO: 

- Investigate other Py->WASM compilers (are there any ?)
- Benchmark other WASM runtimes

#cython-plus

## See also

- [[Cython+ - Idées connexes et notes diverses]]

### Notes

- https://tomassetti.me/wasi-how-to-run-webassembly-code-outside-of-your-browser/
- [# WebAssembly on the Server: How System Calls Work](https://christine.website/talks/webassembly-on-the-server-system-calls-2019-05-31) (2019)
- http://neugierig.org/software/blog/2022/06/wasm-notes.html
- https://blog.scottlogic.com/2022/06/20/state-of-wasm-2022.html

<!-- Keywords -->
#python_to_wasm
<!-- /Keywords -->

## Existing projects

### mypyc

Compiles a subset of (type-annotated) Python to C.
doc: https://mypyc.readthedocs.io/en/latest/
source: https://github.com/python/mypy/tree/master/mypyc

### mycpp

https://www.oilshell.org/blog/2022/05/mycpp.html "This post is for Python experts! I briefly describe [mycpp](https://www.oilshell.org/cross-ref.html?tag=mycpp#mycpp), a hacky Python-to-C++ translator I wrote on top of the [MyPy](https://www.oilshell.org/cross-ref.html?tag=MyPy#MyPy) type checker."

> ## Question: MyPy Subset with Python 3.10 Pattern Matching?
> 
> [Python 3.10 was released](https://docs.python.org/3/whatsnew/3.10.html) late last year, with structural pattern matching.
> 
> One thing I found difficult when building on top of [MyPy](https://www.oilshell.org/cross-ref.html?tag=mypy#mypy) is the "inverted" visitor style. My brain doesn't like"losing the stack" — i.e. when local variables become member variables.
> 
> I also noticed that recent versions of the [AST module](https://docs.python.org/3/library/ast.html) support **type comments**, which Oil still uses.
> 
> So I wonder if anybody has tried to write a **strictly typed** subset of [MyPy](https://www.oilshell.org/cross-ref.html?tag=mypy#mypy) with Python 3.10 pattern matching and the new `ast` info? I think that could be a fun project. If it's limited to what Oil uses, it shouldn't be too big.
> 
> **Gradual typing** was crucial to get Oil to where it is now, but our translator can now assume strict typing.
> 
> -   Somewhat related repository: [Exercises for _Types and Programming Languages_ in Python](https://github.com/iamkroot/pytapl), with Python 3.10 pattern matching
 
### transonic

vision: https://fluiddyn.netlify.app/transonic-vision.html
source: https://foss.heptapod.net/fluiddyn/transonic

### PPCI

https://pypi.org/project/ppci/
> The PPCI (Pure Python Compiler Infrastructure) project is a compiler written entirely in the [Python](https://www.python.org/) programming language. It contains front-ends for various programming languages as well as machine code generation functionality. With this library you can generate (working!) machine code using Python (and thus very easy to explore, extend, etc.)!


### Byterun and Tailbiter

https://github.com/nedbat/byterun.git
https://github.com/darius/tailbiter.git

Byterun = Python VM in python (see also: https://aosabook.org/en/500L/a-python-interpreter-written-in-python.html)
Tailbiter = compiler from Python to bytecode, in python.

https://github.com/rocky/x-python = fork (maintained) of byterun

### Core Python

https://github.com/windelbouwman/corepython = "A [Python](https://www.python.org/) to [WebAssembly](https://webassembly.org/) compiler written in [Rust](https://www.rust-lang.org/)."

Features:
-   Very minimal subset of the Python language. Only the core of it, nothing fancy.
-   CorePython compiler itself is embeddable in browser (small WebAssembly download).


### Older projects

https://mython.org/ 
> Mython is an extensible variant of the [Python](http://www.python.org/) programming language. Mython makes Python extensible by adding two things: _parametric quotation statement_, and _compile-time metaprogramming_. The parametric quote statement is simply syntactic sugar for saying "run some function on this embedded string". Compile-time metaprogramming allows you to evaluate that function on the embedded string at compile time. This gives you added choice, both in terms of what your code looks like, and when you want to evaluate that code.

➜ Not sure what this really means, and if it's useful (it was never released)
➜ There are a few research papers.
    - https://dl.acm.org/doi/10.1145/1837513.1640141 "Language embedding and optimization in mython"
    - http://people.cs.uchicago.edu/~jriehl/dissertation.pdf

## Interesting techniques / libraries

### Term rewriting

Python projects:

- https://github.com/sdiehl/pyrewrite.git
- https://github.com/true-grue/raddsl.git
- https://github.com/sdiehl/subpy
- https://github.com/chrisbouchard/termination.git
- https://refactor.readthedocs.io/en/latest/index.html#

Article:

"Improving performance of Python code using rewriting rules technique"
http://ceur-ws.org/Vol-2866/ceur_115-125jereb11.pdf / http://pp.isofts.kiev.ua/ojs1/article/view/403
> "We propose an approach to increasing performance of Python code by transforming fragments of code to more efficient languages such as Cython and C++. We use high-level algebraic models and rewriting rules technique for semi-automated code transformation. Performance-critical fragments of code are transformed into a low-level syntax model using Python parser"

Others: 
- http://strategoxt.org/ (see also: https://tudelft-cs4200-2020.github.io/lectures/2020/10-transformation/CS4200-2020-10-transformation.pdf)

### AST manipulation

Read this first: https://pybit.es/articles/ast-intro/

Libraries:

- 'astpretty': Pretty print the output of python stdlib `ast.parse`.
    - https://pypi.org/project/astpretty/
- 'astunparse': An AST unparser for Python. This is a factored out version of unparse found in the Python source distribution; under Demo/parser in Python 2 and under Tools/parser in Python 3.
- astor (previously codegen): Python AST read/write 
    - https://github.com/berkerpeksag/astor
- Asteria (`Al2O3`): Missing AST features (monkey-patches ast using astor / astpretty):
    - https://github.com/isidentical-archive/asteria
- gast: A generic AST to represent Python2 and Python3’s Abstract Syntax Tree(AST). GAST provides a compatibility layer between the AST of various Python versions, as produced by ast.parse from the standard ast module.
- beniget: A static analyzer for Python2 and Python3 code. Beniget provides a static over-approximation of the global and local definitions inside Python Module/Class/Function. It can also compute def-use chains from each definition.

### Parsers (for other things)

- Textx

### Others

- 'multipledispatch',
- 'jinja2',
- 'numexpr': The `numexpr` package supplies routines for the fast evaluation of array expressions elementwise by using a vector-based virtual machine.

## Books and tutorials

Course/Book: Essentials of Compilation - An Incremental Approach in Python
https://github.com/IUCompilerCourse/Essentials-of-Compilation + https://github.com/IUCompilerCourse/python-student-support-code
➜ Interesting tutorial / book for undergraduate students. Compiles Python to machine language. Easy to read.

"Let's Write an LLVM Specializer for Python!"
http://dev.stephendiehl.com/numpile/ and https://github.com/sdiehl/numpile  
➜ Very interesing tutorial. But old. 
➜ Hints at some additional ideas (including using https://github.com/sdiehl/pyrewrite and https://github.com/sdiehl/subpy)

https://codewords.recurse.com/issues/seven/dragon-taming-with-tailbiter-a-bytecode-compiler
➜ Shows some basic compilation techniques (Python AST ➜ Python Bytecode)
➜ Repo here: https://github.com/darius/tailbiter

https://arxiv.org/abs/2011.13127 "Copy-and-Patch Compilation: A fast compilation algorithm for high-level languages and bytecode"
➜ Maybe interesting (or not) for us. At least, contains references to recent papers.

### WASM

https://github.com/appcypher/awesome-wasm-langs -> Lua, mruby, grain...
https://tomassetti.me/wasi-how-to-run-webassembly-code-outside-of-your-browser/

## Additional references

### Benchmarks

- https://www.semanticscholar.org/paper/Performance-Comparison-of-Python-Translators-for-a-Milla-Rucci/4927481ef6100194a12e98fb8ad3ecad1f1547c6
- https://www.semanticscholar.org/paper/Comparing-Python%2C-Go%2C-and-C%2B%2B-on-the-N-Queens-Fua-Lis/27045c99c8702d73dc44128877ef002945ae8c72
- https://www.semanticscholar.org/paper/Benchmarking-Python-Interpreters-%3A-Measuring-of-and-Roghult/7979ff96a2441260f87597057ed24642854439da

### Interesting compiler in Python

- https://github.com/evhub/coconut/blob/master/coconut/compiler/compiler.py


## See also

[[Compilers]]
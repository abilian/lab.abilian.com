# A plan for Benchmarking Cython+
#todo #cython-plus

## Goals
As part of the Cython+ project, this subproject will have to help evaluate the benefits of Cython+ against the *statu quo* (CPython and Stefan Behnel's Cython) and alternative approaches (various Python JIT accelerators, including Numba, and).

More specifically, we will have to evaluate Cython+ along two axes:

1. How more performant (in terms of elapsed time, CPU and memory consumption) Cython+ is.
2. How improved (or degraded) the developer experience (DX) is relative to the baselines, in terms of:
	1. Compilation time
	2. Startup time
	3. How different it is from standard Python (in terms of both added and removed features)
	4. Support from and from the Python tooling ecosystem (formatters, linters, IDEs...) and the Python librairies
	5. Language support for things that can't be done (easily) in standard Python

The "performance" part is mostly numerical. The "DX" part has some numerical, but most of it is qualitative.

## Current state
I have created a project for running and reporting benchmarks of Cython+ against both regular implementations of Python and Cython (including some exotic variants), and other languages: 

- GitHub project: <https://github.com/abilian/python-benchmarks>
- Results: <https://lab.abilian.com/>

## General observations

### 3 Levels of benchmarks
We will have to consider three main categories of benchmarks, which each provide different insights:

1. Micro and mini benchmarks (from 10 to a few 100s of LOC). This is the easiest category to start with, and also the only one that allow rigourous comparison between languages or language variants.

2. Benchmarking based on existing librairies (ex: SQLAlchemy, Jinja2, etc.) or applications (ex: PyDis, see below). This category is probably the most useful for users, but it will be quite hard to do in our context since a big part of the benefits of using Cython comes at the price of changes in the syntax (if not the semantics) of the language.

3. Benchmarking of applications specifically written for the project (see below).

### Benchmarks for various use cases

Benchmarks are only relevant for a class of applications.

We will classify our micro-benchmarks in several categories:

1. Non-numerical algorithms
2. Numerical algorithms
	1. Scalar
	2. Vector
3. Networked apps

And provide synthetic marks for various usage profiles based on the weighted results of these benchmarks.

### Benchmarks against relevant contenders
No need to benchmark against all the existing language. We will choose a subset:

- Languages most similar to Python ("Scripting languages"): JS, Ruby, Lua.
- Most performant languages as of today: C and C++
- Additional newcomers: Go, Rust, maybe a couple other...
- Maybe Pony because it's also an actor-based language ?

## Current plan
- [x] Run a decent set of micro and mini benchmarks with a decent set of languages and language variants. (WIP)
- [ ] Identify a subset of these benchmarks that correspond to the main use cases outlined above
- [ ] Add currently missing implementations of the programs (from the Debian Computer Language Benchmarks Game)
- [ ] Check that the results are indeed corrects for all the implementations
- [ ] Make a decent website to present the results
- [ ] Compute and present synthetic marks for each of the main use cases
- [ ] Run benchmarks remotely on various machines
	- [ ] Small (Raspberry Pi, Single CPU x86)
	- [ ] Medium (Core i5 or similar)
	- [ ] Large and very large (Rapid.Space ?)
	- [ ] "Exotic" (RISC-V board ?)
- [ ] Add a few "exotic" implementations of Python to the mix
	- [x] Pyjion
	- [x] Pyston
	- [ ] Micropython and variants
	- [ ] tpythonpp
- [ ] Implement higher level benchmarks i.e. PyDis, the Web Server, etc.
- [ ] Benchmark the web server against TechEmpower and https://github.com/klen/py-frameworks-bench
- [ ] Add https://github.com/paugier/nbabel
- [ ] Play w/ https://transonic.readthedocs.io/


## Projets to Cythonize+ for benchmarking
- [ ] Web server
- [ ] Pydis (see below)
- [ ] https://github.com/geohot/minikeyvalue


### Pydis
- [ ] Trouver un moyen de paralléliser
- [ ] Re-implementer Pydis en:
	- [ ] Cython
	- [ ] Cython+ / Acthon
	- [ ] One or more of Go, Rust, Swift, V, Pony, Zig, Nim

Additional databases that could be cythonized+ and/or used as benchmarks without changes:

- [ ] [GitHub - msiemens/tinydb: TinyDB is a lightweight document oriented database optimized for your happiness :)](https://github.com/msiemens/tinydb) + benchmarks
- [ ] Buzhug (= tinydb)
- [ ] [[BlackSheep]] (already Cythonized)
- [ ] Minikeyvalue (Go+leveldb): <https://github.com/geohot/minikeyvalue> "A distributed key value store in under 1000 lines. Used in production at comma.ai"


### Web server / app server
See dedicated page: [[Use cases]].

See: https://github.com/klen/py-frameworks-bench


## Notes / references
### Specifically on benchmarks
> *Google originally optimized the V8 JIT using the Richards benchmark, because its a good test of polymorphism and how classes are often used.*
   -- Source: <https://medium.com/analytics-vidhya/77x-faster-than-rustpython-f8331c46aea1>
  
- The [Debian Computer Language Benchmarks Game](https://benchmarksgame-team.pages.debian.net/benchmarksgame/)
- PyBenchmarks: <https://github.com/Dundee/pybenchmarks> / <https://pybenchmarks.org/>
- <https://github.com/smarr/are-we-fast-yet> - Are We Fast Yet? Comparing Language Implementations with Objects, Closures, and Arrays (Pas de Python)
- <https://github.com/ltratt/vms_experiment> - Benchmark suite for dynamically typed languages and VMs
- <https://pyperformance.readthedocs.io/benchmarks.html>
- <https://benchmarksgame-team.pages.debian.net/benchmarksgame/measurements/python3.html>
- https://github.com/renaissance-benchmarks/renaissance Modern benchmark suite for Java
- <https://browserbench.org/JetStream/> Browser (JS) bench (with interesting comments)
- <https://github.com/smarr/Classic-Benchmarks> "This is a collection of classic benchmarks collected from all over the internet. Each file contains an indicate of its origin and changes to it are documented via the repositories' history."
- <https://github.com/TechEmpower/FrameworkBenchmarks.git>
- <https://benjamin.computer/posts/2020-12-12-rust-python.html>

### Papers on benchmarks and performance
- [On Evaluating the Renaissance Benchmarking Suite: Variety, Performance, and Complexity](https://arxiv.org/pdf/1903.10267.pdf) (pour la JVM). 
- https://www.cs.ucsb.edu/sites/default/files/docs/reports/2010-14.pdf "Understanding the Potential of Interpreter-based Optimizations for Python" (2010)
- https://www.researchgate.net/publication/264647016_Are_We_There_Yet_Simple_Language_Implementation_Techniques_for_the_21st_Century
- https://www.researchgate.net/publication/310464226_Cross-Language_Compiler_Benchmarking_Are_We_Fast_Yet
- https://stefan-marr.de/2020/07/is-this-noise-or-does-this-mean-something-benchmarking/

- https://blog.sigplan.org/2020/10/12/from-heavy-metal-to-irrational-exuberance/
- https://stefan-marr.de/2020/10/irrationally-annoyed/
- https://stefan-marr.de/2020/08/optimizing-the-unoptimizable-using-old-ideas/
- https://stefan-marr.de/2020/06/efficient-and-safe-implementations-of-dynamic-languages/

### Misc info
- [Rust is now overall faster than C in benchmarks](https://benchmarksgame-team.pages.debian.net/benchmarksgame/which-programs-are-fastest.html)
- https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-172-performance-engineering-of-software-systems-fall-2018/lecture-slides/

## Older benchmarks (by Nexedi)
[Cette page](https://www.nexedi.com/NXD-Blog.Multicore.Python.HTTP.Server) contient un tableau utile pour comparer des librairies de coroutines.

Et [cette page](https://www.nexedi.com/NXD-Blog.Cython.Multithreaded.Coroutines) donne une idée des performances relatives de coroutines.

Si cela t'intéresse, j'aimerais bien avoir une évaluation de haproxy vs. lwan selon les mêmes principes.

---

## More recent links (2022/12)

- https://programming-language-benchmarks.vercel.app/python
- https://sschakraborty.github.io/benchmark/index.html
- https://salsa.debian.org/benchmarksgame-team/benchmarksgame
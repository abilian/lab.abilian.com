## Existing Python libraries

* [GitHub - tomerfiliba/plumbum: Plumbum: Shell Combinators](https://github.com/tomerfiliba/plumbum)
* [1.12.13 — sh 1.12.13 documentation](http://amoffat.github.io/sh/)
* [GitHub - aeroxis/sultan: Sultan: Command and Rule over your Shell](https://github.com/aeroxis/sultan)
* [Seashore](https://github.com/elcaminoreal/seashore/) "Seashore -- A collection of shell abstractions" (not actively developped)
* [Shelmet](https://github.com/dgilland/shelmet): promising but no background tasks [[Shelmet]]
* https://domonic.readthedocs.io/packages/terminal.html
* https://pypi.org/project/shellby/
- https://github.com/KonishchevDmitry/psh = Process management library
- https://github.com/Ovsyanka83/pysh/ = A library of small functions that simplify scripting in python
- https://hitchdev.com/commandlib/ = a library for calling external UNIX commands (e.g. in build scripts) in a clean, readable way.
## Docs / blogs posts

- https://martinheinz.dev/blog/98 "The Right Way to Run Shell Commands From Python"

## Shell -> Python converter / compiler

- https://www.swag.uwaterloo.ca/bash2py/index.html

See also:

- https://github.com/vorpaljs/bash-parser "Parses bash into an AST" (JavaScript)
- https://niols.fr/materials/papers/sle18.pdf "Morbig: A Static Parser for POSIX Shell" research paper
- https://www.oilshell.org/blog/2019/02/07.html "How to Parse Shell Like a Programming Language" blog post
- https://www.oilshell.org/blog/2021/01/comments-parsing.html
- http://shell.cs.pomona.edu/ "Smoosh - The Symbolic, Mechanized, Observable, Operational Shell"

## Type-safe shell scripting

- [Type-safeness in Shell](https://www.lesswrong.com/posts/Fr7FpCNhnTP2i5iaG/)
- https://www.researchgate.net/publication/221055373_Declarative_Scripting_in_Haskell
- https://www.oilshell.org/cross-ref.html
- https://www.oilshell.org/blog/2020/01/simplest-explanation.html

## Misc

- https://github.com/sustrik/uxy "UXY: Adding structure to the UNIX tools"
- https://hush-shell.github.io/foreword.html - "This is the official guide of [_Hush_](https://github.com/hush-shell/hush), a modern shell scripting language."

## Misc ideas for a new API

Goals:

- Ease / naturalness of use
- Type safety

Shell object: `shell = Shell()`

Run something: `result = shell.ls()`

With options: `result = shell.ls(l=True)` (== `ls -l`).

Errors recovery:

```
try:
	result = shell.ls()
except ShellException as e:
	print(e.status)
```

Strong typing: generate `.pyi` files for common commands ? By parsing man pages ?

Piping: `shell.ls().pipe.grep('*.py')` ? bof.

`shell.pipe(shell.ls(), shell.grep('*.py')` ? (Needs to parse AST inside the pip argument).


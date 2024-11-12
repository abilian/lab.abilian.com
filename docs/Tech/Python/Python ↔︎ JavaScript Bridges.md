
## Projects

- https://github.com/Distributive-Network/PythonMonkey - A Mozilla SpiderMonkey JavaScript engine embedded into the Python VM, using the Python engine to provide the JS host environment.
    - → Not ready for prime time (Aug. 2023)

- https://github.com/cloudflare/stpyv8 - Python 3 and JavaScript interoperability. Successor To PyV8

- https://github.com/amol-/dukpy - DukPy is a simple javascript interpreter for Python built on top of duktape engine **without any external dependency**. It comes with a bunch of common transpilers built-in for convenience:
    - → Implements an old version of JavaScript (ex: no `let` / `const`)

- https://github.com/extremeheat/JSPyBridge - Bridge to interoperate Node.js and Python
    - https://blog.logrocket.com/exploring-jspybridge-library-python-javascript/

- https://github.com/PetterS/quickjs = Thin Python wrapper of [https://bellard.org/quickjs/](https://bellard.org/quickjs/)

- https://pypi.org/project/javascript/ = Call and interop Node.js APIs with Python

## Quickjs usage

```python
from quickjs import Function

f = Function("f", """
    function adder(a, b) {
        return a + b;
    }
    
    function f(a, b) {
        return adder(a, b);
    }
    """)

assert f(1, 2) == 3
```

<!-- Keywords -->
#quickjs #pythonmonkey
<!-- /Keywords -->

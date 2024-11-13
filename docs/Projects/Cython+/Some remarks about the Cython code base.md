Stefane Fermigier, 16 jul. 2020.

## Tests
Cf. [HackerGuide · cython/cython Wiki · GitHub](https://github.com/cython/cython/wiki/HackerGuide#tests).

Tests are run using the `runtests.py` script. A test run takes between 15 and 20 minutes on a decent machine.

See [this Travis run](https://travis-ci.com/github/abilian/cython/builds/175864790).

It’s also possible (but doesn’t seem to be officially supported) to launch a subset of the test suite using the command: `pytest tests/`. Most of the tests in `tests/` pass, and the run is quite quick (~5s):

```
=========================== short test summary info ============================
FAILED tests/run/test_asyncgen.py::AsyncGenAsyncioTest::test_async_gen_await_same_aclose_coro_twice
FAILED tests/run/test_asyncgen.py::AsyncGenAsyncioTest::test_async_gen_await_same_anext_coro_twice
FAILED tests/run/test_grammar.py::GrammarTests::testAssert2 - AssertionError:...
FAILED tests/run/test_grammar.py::GrammarTests::test_funcdef - AssertionError...
============ 4 failed, 159 passed, 12 skipped, 42 warnings in 4.42s ============
```


### Proposals

1. Update `tox.ini` to be on par with the current version of `.travis.yml`,  then simplify the Travis config to rely on Tox, using the `tox-travis` plugin, to remove duplication.
2. Split the test suite.

---

## Code style and linters
The Cython code doesn’t adhere to PEP8.


### Proposals
1. Run `black` on the code base.

<!-- Keywords -->
#cython
<!-- /Keywords -->

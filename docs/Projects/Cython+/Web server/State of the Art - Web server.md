#cython-plus #web

## Notes on HTTP/2 and HTTP/3
* [GitHub - nghttp2/nghttp2: nghttp2 - HTTP/2 C Library and tools](https://github.com/nghttp2/nghttp2)
* [GitHub - aiortc/aioquic: QUIC and HTTP/3 implementation in Python](https://github.com/aiortc/aioquic)
* [GitHub - h2o/h2o: H2O - the optimized HTTP/1, HTTP/2, HTTP/3 server](https://github.com/h2o/h2o)

Pour les tests: https://en.wikipedia.org/wiki/HTTP/3#Libraries

## Serveurs Web
### WSGI
- Bjoern (Python + C, simple)
- [GitHub - mopemope/meinheld: Meinheld is a high performance asynchronous WSGI Web Server (based on picoev)](https://github.com/mopemope/meinheld) (plus complexe)
- uWsgi
- Gunicorn...

- https://github.com/mahmoud/hematite (A full-featured and high-accuracy implementation of HTTP/1.1 in pure Python)

### ASGI
- https://www.uvicorn.org/: Uvicorn is a lightning-fast ASGI server implementation, using [uvloop](https://github.com/MagicStack/uvloop) and [httptools](https://github.com/MagicStack/httptools). Uvicorn currently supports HTTP/1.1 and WebSockets. Support for HTTP/2 is planned.
- https://gitlab.com/pgjones/hypercorn: is an ASGI Server based on Hyper libraries and inspired by Gunicorn. Hypercorn supports HTTP/1.1, HTTP/2, and WebSockets.
- Daphne: It is run widely in production, and supports HTTP/1.1, HTTP/2, and WebSockets.

### Low-level libraries used
- https://gist.github.com/andreybolonin/2413da76f088e2c5ab04df53f07659ea Libuv vs. Libev
- https://github.com/libuv/libuv: libuv is a multi-platform support library with a focus on asynchronous I/O. It was primarily developed for use by [Node.js](http://nodejs.org/), but it's also used by [Luvit](http://luvit.io/), [Julia](http://julialang.org/), [pyuv](https://github.com/saghul/pyuv), and [others](https://github.com/libuv/libuv/wiki/Projects-that-use-libuv).
- https://github.com/saghul/pyuv: Python interface for libuv
- https://nikhilm.github.io/uvbook/introduction.html
- https://blog.gevent.org/2011/04/28/libev-and-libevent/
- https://github.com/kazuho/picoev
- https://github.com/qweeze/nanoasgi "This is a toy ASGI web framework. It has zero dependencies and only 170 lines of code. I wrote it to play around with ASGI and to study how frameworks work under the hood."

And:
- https://github.com/MagicStack/httptools: httptools is a Python binding for the nodejs HTTP parser.
- https://github.com/MagicStack/uvloop: uvloop is a fast, drop-in replacement of the built-in asyncio event loop. uvloop is implemented in Cython and uses libuv under the hood.

### Others
* Caddy (Go)
* HA Proxy (C or C++)
- LWAN: https://lwan.ws/

List here: https://en.wikipedia.org/wiki/HTTP/3#Server


## Application servers
- En Cython: [[BlackSheep]]

## Random notes
- [https://www.loggly.com/blog/benchmarking-5-popular-load-balancers-nginx-haproxy-envoy-traefik-and-alb/](https://www.loggly.com/blog/benchmarking-5-popular-load-balancers-nginx-haproxy-envoy-traefik-and-alb/)
- [https://fr.slideshare.net/kazuho/h2o-making-http-better](https://fr.slideshare.net/kazuho/h2o-making-http-better)
- [https://www.haproxy.com/fr/blog/multithreading-in-haproxy/](https://www.haproxy.com/fr/blog/multithreading-in-haproxy/)
- <https://github.com/pfalcon/picoweb> : picoweb is a "micro" web micro-framework (thus, "pico-framework") for radically unbloated web applications using radically unbloated Python implementation, Pycopy.
- https://indico.cern.ch/event/282910/contributions/645355/attachments/521441/719267/efficient_parallel_IO_on_multicore_arch2.pdf
- https://eli.thegreenplace.net/2021/go-https-servers-with-tls/

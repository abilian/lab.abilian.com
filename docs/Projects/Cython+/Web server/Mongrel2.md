Mongrel2 is an open-source "language agnostic" web server written by Zed Shaw, and is the successor to Shaw's Mongrel server. The server supports HTTP, Flash XMLSockets, WebSockets and long polling connections.

The code was mostly writen in 2010.

## Features (according to the README)

- Language Agnostic with a simple backend protocol supporting 17 languages and platforms all written by Mongrel2 fans.
- Modern Browser Friendly designed to handle HTTP, Flash XMLSockets, or
  WebSockets, Long Polling on the same socket transparently.
- ZeroMQ Enabled as well as HTTP proxy support so it works with what you have
  already while giving you new super powers.
- Network Architecture Agnostic so you can carve your operations up any way that reduces costs.
- N:M Messaging Patterns means you can have any N handlers answer to any M
  browsers arbitrarily, but still easy to do plain request/response.
- Automation Loving Configs that are easily accessible via any programming
  language with a Model-View-Controller design.
- Modern Internal Design using the Mongrel 1 HTTP parser powering many big
  companies with a proven security track record, event based I/O, fast
  coroutines to handle that I/O, and smart reasonable defaults with zero
  configuration needed usually.
- Documented, Documented, Documented. We document everything in a well written manual that shows you how to use every feature.
- BSD Licensed and all with a BSD 3-clause license.
- Tir -- An official framework written in Lua that shows how to use Mongrel2 to
  create other frameworks for PHP, Python, etc.

Market share: ~0 (according to <https://www.wappalyzer.com/technologies/web-servers> or <https://w3techs.com/technologies/overview/web_server>)

## Uses (notably)

- Ragel <http://www.colm.net/open-source/ragel/> state machine for the HTTP protocol.
- Dexy: documentation generator

<!-- Keywords -->
#websockets #backend
<!-- /Keywords -->

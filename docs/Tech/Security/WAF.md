Web Application Firewalls (WAFs) have become an essential component of web security, acting as gatekeepers to protect web applications from a variety of cyber threats.

## Rule Sets

One of the main components of the open source WAF ecosystem is the OWASP® ModSecurity Core Rule Set (CRS), a set of generic attack detection rules designed for ModSecurity or compatible WAFs. This rule set is pivotal in defending web applications against a spectrum of attacks, including the notorious OWASP Top Ten, while striving to minimize false alerts.

https://coreruleset.org/

> The **OWASP® ModSecurity Core Rule Set (CRS)** is a set of generic attack detection rules for use with [ModSecurity](https://www.modsecurity.org/) or compatible web application firewalls. The CRS aims to protect web applications from a wide range of attacks, including the OWASP Top Ten, with a minimum of false alerts. The CRS provides protection against many common attack categories.

Sources: https://github.com/coreruleset/coreruleset

## Open source solutions

### Coraza (1.6k★)

https://github.com/corazawaf/coraza.git "OWASP Coraza WAF is a golang modsecurity compatible web application firewall library"

> Coraza is an open source, enterprise-grade, high performance Web Application Firewall (WAF) ready to protect your beloved applications. It is written in Go, supports ModSecurity SecLang rulesets and is 100% compatible with the OWASP Core Rule Set v4.


https://securitypilgrim.com/top-30-free-open-source-tools/#Web_Application_Firewalls_WAF ➜ lists 3 solutions below

### ModSecurity (5.4k★)

https://github.com/SpiderLabs/ModSecurity "ModSecurity is an open source, cross platform web application firewall (WAF) engine for Apache, IIS and Nginx that is developed by Trustwave's SpiderLabs. It has a robust event-based programming language which provides protection from a range of attacks against web applications and allows for HTTP traffic monitoring, logging and real-time analys…"

https://owasp.org/blog/2024/01/09/ModSecurity.html
> After serving as its steward for over a decade, [Trustwave](https://www.trustwave.com) has agreed to transfer the reins of the renowned open-source web application firewall (WAF) engine, ModSecurity, to the [Open Worldwide Application Security Project (OWASP)](https://owasp.org). This landmark move promises to inject fresh energy and perspectives into the project, ensuring its continued evolution as a vital line of defense for countless websites worldwide.

### Shadow Daemon (250★)

https://github.com/zecure/shadowd "Shadow Daemon is a collection of tools to detect, record and prevent attacks on web applications. Technically speaking, Shadow Daemon is a web application firewall that intercepts requests and filters out malicious parameters. It is a modular system that separates web application, analysis and interface to increase security, flexibility and expandability."

### NAXSI (4k★)

https://github.com/nbs-system/naxsi "NAXSI is an open-source, high performance, low rules maintenance WAF for NGINX"
→ Moved to: https://github.com/wargio/naxsi.git

### Videur (dead project)

https://github.com/mozilla/videur "Videur is a Lua library for OpenResty that will automatically parse an API specification file provided by a web server and proxy incoming Nginx requests to that server." Maybe some interesting ideas there.
Discussion here: https://ziade.org/2014/10/24/web-application-firewall/
(Saved at ~/ghq/github.com/mozilla/videur).

### See also

- https://github.com/libinjection/libinjection ("SQL / SQLI tokenizer parser analyzer")
- https://github.com/sysdig/wafer "Wafer is a simple but effective web application firewall (WAF) fuzzing tool. It is designed to be used as a standalone script, it uses various techniques build payloads which could potentially bypass a WAF."

## Not open source

- https://www.imperva.com/

## Ressources

- "2022 Cloud Web Application Firewall (WAF) CyberRisk Validation Comparative Report"
- https://nishtahir.com/i-looked-through-attacks-in-my-access-logs-heres-what-i-found/ 
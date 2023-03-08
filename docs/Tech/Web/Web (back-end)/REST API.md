## REST-based protocols
* HAL (http://tools.ietf.org/html/draft-kelly-json-hal-07)
	* https://halogen.readthedocs.io/en/latest/
* JSON API (http://jsonapi.org/)
* Restful Objects (http://www.restfulobjects.org/)
* “collection.document+json”  (http://cdoc.io/)
* “collection+json” (http://amundsen.com/media-types/collection/)
* OData ( [www.odata.org](http://www.odata.org) ), soutenu par Microsoft et SAP…
- http://www.hydra-cg.com/spec/latest/core/#hydra-at-a-glance
- https://github.com/JornWildt/Mason

## Alternatives (not REST)
- GRPC-Web - <https://github.com/grpc/grpc-web>
- GraphQL

## Comparisons
https://www.fabernovel.com/en/article/tech-en/which-technologies-should-you-use-to-build-hypermedia-apis

From: https://www.nginx.com/blog/building-your-api-for-longevity-best-practices/

-   The first is [HAL](https://en.wikipedia.org/wiki/Hypertext_Application_Language), which is a very popular specification. \[The IETF draft is [JSON Hypertext Application Language](https://tools.ietf.org/html/draft-kelly-json-hal-08).\]
-   The second one is [JSON‑LD](https://www.w3.org/TR/json-ld/), which is a W3C standard but was really designed for linking definitions between databases. I’d actually avoid using that one.
-   [JSON API](https://jsonapi.org/) is a very popular hypermedia format which I highly recommend.
-   [Collection+JSON](http://amundsen.com/media-types/collection/) was one of the original ones created by Mike Amundsen. It’s a great specification, but I would still lean towards HAL or JSON API.
-   Siren is actually really interesting in that it went a different direction. Siren has foreign properties, class properties, and entity properties, and it’s action‑driven.
-   Then there’s [CPHL](https://github.com/mikestowe/CPHL). I put the asterisk on because I made it. It’s also action‑driven.

## Best practices
https://www.nginx.com/blog/building-your-api-for-longevity-best-practices/

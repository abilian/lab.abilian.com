"[Furl](https://github.com/gruns/furl)" and "[yarl](https://pypi.org/project/yarl/)" are both Python libraries that provide convenient and powerful APIs for working with URLs, but they have some differences in terms of features, design choices, and their respective goals:

1. **API Design:**

   - "Furl" aims to provide a simple and straightforward API for working with URLs. It offers a chainable API, similar to method chaining, allowing you to build and modify URLs fluently.
   - "Yarl" aims to provide a more comprehensive and flexible API for URL manipulation. It offers a more object-oriented approach, with separate objects for URLs, schemes, query strings, etc., allowing for more fine-grained control and customization.

1. **URL Parsing and Construction:**

   - "Furl" provides comprehensive parsing and construction capabilities for URLs. It can parse URLs, modify their components (scheme, host, path, query parameters, etc.), and construct valid URLs from scratch.
   - "Yarl" also offers URL parsing and construction features, but with additional flexibility and fine-grained control. It provides separate objects for different URL components, allowing for more granular manipulation.

1. **Immutability**:

   - The "furl" library provides mutable URL objects by default. It allows you to modify various components of a URL, such as scheme, host, path, and query parameters, in-place using its chainable API. This means that when you modify a URL object, the changes are applied directly to the object itself.
   - **On the other hand, the "yarl" library follows an immutable approach for URL manipulation.** It treats URLs as immutable objects, meaning that any modification operations return a new URL object with the desired changes. This design ensures that the original URL object remains unchanged, preserving immutability.

1. **Unicode Handling:**

   - "Furl" has limited support for Unicode handling in URLs. It assumes that the URLs are already properly encoded and doesn't perform any encoding or decoding internally.
   - "Yarl" provides robust Unicode handling for URLs. It automatically encodes and decodes URL components as needed, ensuring correct and consistent handling of Unicode characters.

1. **Query Parameter Handling:**

   - "Furl" offers convenient methods for working with query parameters, such as adding, updating, or removing individual parameters. It also supports parsing and formatting query strings.
   - "Yarl" provides advanced query parameter handling with rich support for multi-valued parameters, nested parameters, and complex data structures. It offers methods for adding, updating, removing, and iterating over query parameters.

1. **Dependencies:**

   - "Furl" has minimal external dependencies, making it lightweight and easy to integrate into projects with limited dependencies.
   - "Yarl" has dependencies on more extensive libraries, such as "multidict" and "idna", which provide additional functionality and support for complex URL manipulation scenarios.

1. **Maturity and Popularity:**

   - "Furl" has been around for a longer time and has gained popularity as a lightweight and easy-to-use URL manipulation library.
   - "Yarl" is a newer library and has gained popularity for its more comprehensive API and Unicode support.

→ We choose to use Yarl when given the choice.

## Other alternatives

- The stdlib's [`urllib.urlparse`](https://docs.python.org/3/library/urllib.parse.html#module-urllib.parse) module
- [[Boltons]]' [urlutils](https://boltons.readthedocs.io/en/latest/urlutils.html) (mutable)
- [Hyperlink](https://github.com/python-hyper/hyperlink) (immutable, but less popular and inactive).

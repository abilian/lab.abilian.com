See also [[Search]].

1. **Apache Lucene**: A free and open-source search library written in **Java** used for full-text indexing and searching. It is the underlying technology for many open-source and closed-source search engines. Lucene is often used to build search applications similar to Google and DuckDuckGo.

    1. **Apache Solr**: Solr is a subproject of Apache Lucene, created to provide a powerful REST API for search operations. It's a highly scalable and popular search platform, which is also used as a NoSQL database. Solr is particularly known for its distributed indexing and search capabilities, and its highly extensible architecture.

    1. **Nutch**: Another subproject of Apache Lucene, Nutch is an extensible and scalable web crawler that relies on Apache Hadoop. It allows users to build their own search engine from web page data.

    1. **Elasticsearch**: Elasticsearch is a highly scalable open-source search engine based on the Lucene library. It provides a distributed, multitenant-capable full-text search engine with an HTTP web interface and schema-free JSON documents. Elasticsearch is known for its speed, scale, and ability to index structured and unstructured data.

4. **Sonic**: Sonic is an open-source search index server written in **Rust**. It is lightweight and schema-less. Sonic's inverted index, based on a Levenshtein automaton, makes it a minimalist and resource-efficient alternative to database tools.

5. **Typesense**: Typesense is an open-source, lightweight search engine optimized for speed, written in **C++**. It is designed to provide instant search experiences with a focus on simplicity and ease of installation.

6. **Bleve**: Inspired by Apache Lucene, Bleve is a full-text search and indexing library for **Go**. It provides components to tokenize, filter, and analyze text, then create a searchable index.

7. **Tantivy**: Tantivy is a text search engine library inspired by Lucene and written in **Rust**. It's a low-level library designed to be the foundation for building a full-fledged search engine.

9. **MeiliSearch**: MeiliSearch is a lightweight and powerful open-source search engine built with **Rust**. It aims to provide an easy and customizable search experience. MeiliSearch supports features like typo tolerance, filters, ranking rules, and a high write rate.

10. **Whoosh**: Whoosh is (or was) a fast, featureful full-text indexing and searching library implemented in pure **Python**. Programmers can use it to easily add search functionality to their applications and websites. Every part of how Whoosh works can be extended or replaced to meet your needs exactly. See also [Whoosh-Reloaded](https://pypi.org/project/Whoosh-Reloaded/), a fork, that is not really active either, however.

Note that these projects don't have the exact same scope. For instance, some are standalone search engines, while others are libraries or tools that can be used to build custom search solutions.

<!-- Keywords -->
#lucene #solr #elasticsearch #nosql #google
<!-- /Keywords -->

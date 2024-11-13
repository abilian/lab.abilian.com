A vector database is a database designed to handle high-dimensional vectors efficiently. These databases are used for storing embeddings or representations of data points in a high-dimensional space.

Vector databases excel in performing operations that standard databases struggle with, such as nearest neighbour search in high-dimensional spaces. This operation is fundamental in many machine learning applications, including recommendation systems, image recognition, natural language processing, and more. 

## Example

Let's consider a machine learning model that converts images into high-dimensional vectors (also known as embeddings), where each dimension captures a different feature of the image. To find images similar to a given image, the system would search for vectors close to the vector of the given image. With a high-dimensional space and a large number of vectors, this operation can be computationally expensive. Vector databases are optimized for this kind of operation, enabling efficient similarity searches.


## Examples

### Databases

1. **[Qdrant](https://qdrant.tech/)**: is a vector similarity search engine and vector database. It provides a production-ready service with a convenient API to store, search, and manage points—vectors with an additional payload Qdrant is tailored to extended filtering support. It makes it useful for all sorts of neural-network or semantic-based matching, faceted search, and other applications. Qdrant is written in Rust.

1. **[Milvus](https://github.com/milvus-io/milvus)**: An open-source vector database designed specifically for AI and machine learning applications. It supports a variety of distance metrics and is scalable, reliable, and capable of handling hybrid (vector and scalar) search. Milvus is written in Go.

1. **[Weaviate]()**: Weaviate is an open source vector database that stores both objects and vectors, allowing for combining vector search with structured filtering with the fault-tolerance and scalability of a cloud-native database, all accessible through GraphQL, REST, and various language clients. Written in Go.

1. **[Deeplake](https://github.com/activeloopai/deeplake)**: Deep Lake is a Vector Database powered by a unique storage format optimized for deep-learning and Large Language Model (LLM) based applications. It simplifies the deployment of enterprise-grade LLM-based products by offering storage for all data types (embeddings, audio, text, videos, images, pdfs, annotations, etc.), querying and vector search, data streaming while training models at scale, data versioning and lineage for all workloads, and integrations with popular tools such as LangChain, LlamaIndex, Weights and Biases, and many more. Written in Python.

### Related projects

1. **[FAISS](https://github.com/facebookresearch/faiss) (Facebook AI Similarity Search)**: Developed by Facebook, FAISS isn't a database per se but a library for efficient similarity search of high-dimensional vectors. It is often used in combination with a traditional database to manage the vector part of data.

3. **[Annoy](https://github.com/spotify/annoy) (Approximate Nearest Neighbors Oh Yeah)**: Developed by Spotify, Annoy is a C++ library with Python bindings that supports efficient search of approximate nearest neighbors.

4. **[NMSLIB](https://github.com/nmslib/nmslib) (Non-Metric Space Library)**: An efficient cross-platform library for nearest neighbor search in generic non-metric spaces.

5. **[NGT](https://github.com/yahoojapan/NGT) (Neighborhood Graph and Tree)**: Developed by Yahoo! Japan, NGT provides high-speed search algorithms for nearest neighbors.

8. **[ScaNN](https://github.com/google-research/google-research/tree/master/scann) (Scalable Nearest Neighbors)**: A library for efficient vector similarity search, released by Google Research.

9. [Vectra](https://github.com/Stevenic/vectra) and [Vectra-py](https://github.com/BMS-geodev/vectra-py): A local vector database with features similar to pinecone but built using local files.

## References

- [Top 10 Best Vector Databases & Libraries](https://byby.dev/vector-databases)
-  [Getting started with Vector DBs in Python](https://code.dblock.org/2023/06/16/getting-started-with-vector-dbs-in-python.html "Getting started with Vector DBs in Python")
- [The Best Vector Databases for Storing Embeddings](https://safjan.com/the-best-vector-databases-for-storing-embeddings/#the-best-vector-databases-for-storing-embeddings)
- [vector-database tag on GitHub](https://github.com/topics/vector-database)
- [How can I retrieve K nearest embedding vectors quickly?](https://platform.openai.com/docs/guides/embeddings/how-can-i-retrieve-k-nearest-embedding-vectors-quickly)

>     For searching over many vectors quickly, we recommend using a vector database. You can find examples of working with vector databases and the OpenAI API [in our Cookbook](https://github.com/openai/openai-cookbook/tree/main/examples/vector_databases) on GitHub.

> Vector database options include:

>     - [Pinecone](https://github.com/openai/openai-cookbook/tree/main/examples/vector_databases/pinecone), a fully managed vector database
>     - [Weaviate](https://github.com/openai/openai-cookbook/tree/main/examples/vector_databases/weaviate), an open-source vector search engine
>     - [Redis](https://github.com/openai/openai-cookbook/tree/main/examples/vector_databases/redis) as a vector database
>     - [Qdrant](https://github.com/openai/openai-cookbook/tree/main/examples/vector_databases/qdrant), a vector search engine
>     - [Milvus](https://github.com/openai/openai-cookbook/blob/main/examples/vector_databases/Using_vector_databases_for_embeddings_search.ipynb), a vector database built for scalable similarity search
>     - [Chroma](https://github.com/chroma-core/chroma), an open-source embeddings store
>     - [Typesense](https://typesense.org/docs/0.24.0/api/vector-search.html), fast open source vector search
>     - [Zilliz](https://github.com/openai/openai-cookbook/tree/main/examples/vector_databases/zilliz), data infrastructure, powered by Milvus

#database #machine-learning

<!-- Keywords -->
#databases #database #embeddings
<!-- /Keywords -->

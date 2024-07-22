Hierarchical Navigable Small World (HNSW) is a graph-based algorithm used for approximate nearest neighbor search in high-dimensional spaces. [It was proposed](https://arxiv.org/pdf/1603.09320.pdf) by Yury Malkov and Dmitry Yashunin in 2016.

The HNSW algorithm is designed to handle large-scale datasets and provides an efficient trade-off between accuracy and speed. It constructs a hierarchical structure of layers, where each layer is a navigable small world graph. The top layer of the hierarchy contains a small subset of the data points, while the bottom layer contains all the data points.

The HNSW algorithm uses a greedy search strategy to find the approximate nearest neighbors of a query point. Starting from the top layer, the algorithm navigates through the graph to find the closest point to the query point. It then moves down to the next layer and repeats the process, using the closest point found in the previous layer as the starting point. This process continues until the bottom layer is reached.

The HNSW algorithm has been shown to outperform other approximate nearest neighbor search algorithms in terms of both speed and accuracy, especially on large-scale datasets. It has been used in various applications, such as image and video retrieval, natural language processing, and recommendation systems.

## References

- https://towardsdatascience.com/similarity-search-part-4-hierarchical-navigable-small-world-hnsw-2aad4fe87d37
- https://github.com/nmslib/hnswlib (C++ + Python)
- https://github.com/brtholomy/hnsw (Python)
- https://faiss.ai/cpp_api/struct/structfaiss_1_1HNSW.html (part of FAISS)

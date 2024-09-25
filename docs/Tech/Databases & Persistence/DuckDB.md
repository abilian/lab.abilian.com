
DuckDB is an in-memory analytical database written in C++. It is designed to provide sophisticated database management optimized for analytical queries, similar to other analytical databases such as Apache Arrow. DuckDB supports standard SQL queries and is designed to be easy to integrate with existing data analysis software in R, Python, and other languages.

Key features of DuckDB often highlighted include:

-   **In-Memory & On-Disk Storage:** DuckDB operates directly on data stored in main memory but also supports data stored on disk.
-   **Vectorized Query Execution:** DuckDB uses a columnar data layout and vectorized query execution for efficient analytical query processing.
-   **Support for Complex SQL Queries:** DuckDB supports complex SQL queries, including joins, subqueries, window functions, etc.
-   **Integration with Data Analysis Tools:** DuckDB provides APIs for integration with popular data analysis tools in languages like R and Python.

## Difference w/ Sqlite

-   **Use Case:** SQLite is primarily designed for transactional workloads (OLTP) and works well for lightweight applications, embedded systems, and scenarios requiring single-user access. DuckDB is designed for analytical workloads (OLAP) and is great for data analysis tasks and big data workloads.
-   **Storage:** SQLite is a disk-based database, which means it stores its data on disk, making it a great choice for persistent storage. DuckDB, on the other hand, is an in-memory database but can also handle data stored on disk. However, its primary strength lies in processing data held in memory.
-   **Query Execution:** DuckDB uses vectorized query execution and a columnar data layout, which is optimized for complex analytical queries operating on large amounts of data. SQLite doesn't feature this and instead is optimized for transactional workloads.
-   **Concurrency & Access:** SQLite uses file-level locking for transactions, which can limit concurrency in multi-user scenarios. DuckDB, primarily aimed at analytical tasks, is not generally expected to deal with high levels of concurrent write access.

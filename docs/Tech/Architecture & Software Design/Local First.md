## Notes

Before the advent of cloud computing, data management was straightforward: files were written to local disks, and file exchanges were handled via floppy disks. The shift to cloud storage introduced new challenges, particularly concerning data dependency on cloud providers, which could lead to data loss or vendor lock-in.

### The Local-First Movement

The local-first movement aims to reclaim user control over data by emphasizing local processing and storage while retaining the advantages of the internet. The core principles of local-first software include:

1. **Local Processing and Storage**: Data should be processed and stored locally to ensure accessibility even when offline.
2. **Robust Synchronization**: Synchronization should be resilient to interruptions, ensuring data consistency across devices using Conflict-Free Replicated Data Types (CRDT).
3. **Privacy and Security**: Data should be end-to-end encrypted (E2EE) to ensure privacy, even during transmission.

### Resilient Sync: Bridging Local and Cloud Storage

To address these principles, I propose a resilient sync model that integrates both file system and internet-based approaches. This model involves a continuous log of changes, unique client identifiers, and efficient handling of large binary data (assets).

#### Log of Changes

Each client maintains a simple, continuous log of changes with an index starting at 0. These changes can be CRDT compliant and stored in an encrypted form. Each client is identified by a unique ID (UUID), and changes are linked to this clientId, forming a workspace.

- **Indexing and Timestamping**: Each change is indexed and optionally timestamped, allowing for historical data processing and endless “undo” functionality.
- **Data Consistency**: To ensure consistency, entries can include hashes of previous entries, similar to a blockchain, and potentially evolve towards a Merkle tree structure.

#### Handling Large Binary Data

Assets such as images, videos, and audio files, which rarely change, are managed separately from the content changes to prevent synchronization bottlenecks. These assets are indexed similarly to content changes and can be referenced through URLs containing metadata like size, MIME type, and checksum.

### Implementation Strategies

#### Databases

A database implementation involves tables with fields for index, clientId, data, timestamp, and previous hash. This structure can be used both locally (e.g., IndexedDB) and on synchronization servers.

#### Filesystems

In a filesystem implementation, data is stored in directories with metadata in an `index.json` file. Each client has directories for changes and assets, and files are distributed evenly to avoid directory overloading. 

#### Online Services and Peer-To-Peer Sync

Online services can adopt either the database or filesystem approach based on their needs. For example, Dropbox or WebDAV could use the filesystem approach, while Apple CloudKit might benefit from a database approach. Additionally, peer-to-peer (P2P) synchronization can be employed for direct client communication, leveraging CRDT to manage redundancy and data consistency.

### Refinements and Future Directions

Several areas can be refined to enhance this model:

- **Data Size Control**: Managing the size of log entries by bundling changes or splitting large changes into smaller packages.
- **Data Compression**: Implementing data compression to optimize storage and transmission.
- **Client Announcement**: Using special log entries for announcing new clients and employing cryptographic methods for validation.
- **Logical Clocks**: Incorporating logical clocks like the Lamport clock to improve the chronological ordering of entries.
- **Resource Optimization**: Writing data to a single file per client to optimize resource usage.
- **Cryptographic Enhancements**: Implementing advanced cryptographic techniques for rights management and security (e.g., Cryptree).

### References

- https://www.youtube.com/@localfirstconf / https://www.localfirstconf.com/
- Kleppmann, Martin. “The Past, Present, and Future of Local-First.” Local-First Conf, YouTube, 2024. https://www.youtube.com/watch?v=NMq0vncHJvU&list=PL4isNRKAwz2O9FxP97_EbOivIWWwSWt5j&index=4
- Holtwick, Dirk. “Resilient Sync for Local First.” Blog Post, 2024. https://holtwick.de/en/blog/localfirst-resilient-sync
- Automerge and Yjs projects for CRDT improvements.
- TypeScript function for file distribution from the Zeed Framework.

## Projects

- https://tinybase.org/ "The reactive data store for local‑first apps."
- https://jazz.tools/  "Jazz is an open-source toolkit that replaces APIs, databases and message queues with a single new abstraction: “Collaborative Values” — distributed state with secure permissions built-in. Features that used to take months to build now work out-of-the-box."

<!-- Keywords -->
#storage
<!-- /Keywords -->

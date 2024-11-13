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

## Designing REST APIs: Resources

Resources represent data or functionality accessible through the API. A resource is any type of object, data, or service that can be accessed by the client.

Here are the 4 main types of resources:

1. **Document Resources**: These are single instances of a resource, typically represented as a single entity or object. For example, a specific user or a particular blog post can be a document resource. Each document resource can be accessed by a unique URI.

2. **Collection Resources**: These resources represent a list or collection of child resources that are of the same type. For instance, you might have a collection resource for "users" or "blog posts". A collection resource is also accessed via its own URI, and from there, individual items in the collection can be accessed, manipulated, or added.

3. **Store Resources**: Similar to collection resources, store resources are containers of other resources and allow the client to both add and remove items. However, the key difference is that in a store, the client may have more control over the identity (URI) of the stored resources. For example, a photo storage service where the client can determine the file names and paths.

4. **Controller Resources**: These are executable or actionable resources that perform tasks or functions when invoked. They don't necessarily correspond directly to a data entity but rather represent operations that can be performed. Examples include a resource to resend an email verification or process a payment. These resources are often mapped to functions and procedures on the server-side.

**Hierarchical Resources**: Sometimes, resources are structured in a hierarchical manner where a resource is a parent to one or more child resources. This hierarchical relationship is reflected in the URI structure. For example, accessing a specific blog post (`/blogs/123/posts/456`) where `blogs` is a collection resource, `123` is a specific blog, and `posts/456` represents a specific post within that blog.

### Document resources in detail

Document resources are a foundational concept representing individual instances of a type of data or entity. These resources are typically accessed, manipulated, and represented as discrete, self-contained units that correspond to singular, specific items in the system. Document resources are one of the core elements that facilitate RESTful interactions, emphasizing the management of entities through their life cycles using standard HTTP methods.

#### Characteristics

1. **Unique Identity**:
   - Each document resource is uniquely identifiable through a URI (Uniform Resource Identifier). This unique identifier allows clients to interact directly with a specific instance of a resource, ensuring that operations like GET, PUT, DELETE, and POST (if applicable) are performed on this exact entity.

2. **Self-contained**:
   - A document resource is self-contained, meaning it includes all the data needed to represent the resource in its entirety. This does not preclude linking to other resources but indicates that the resource can be understood and manipulated as a standalone unit.

3. **State Representation**:
   - Document resources are representations of the state of an entity at a particular point in time. When a client fetches a document resource, they receive a snapshot of that resource's state, encapsulated in formats such as JSON or XML.

4. **Lifecycle Operations**:
   - Typical operations on document resources align with the standard HTTP methods: 
     - **GET** to retrieve the resource.
     - **PUT** or **PATCH** to update the resource (PUT for replacing the resource entirely, PATCH for partial updates).
     - **DELETE** to remove the resource.
     - **POST** might be used in certain contexts to perform operations related to the resource, though it's more commonly associated with creating new resources or performing actions.

#### Example Use Cases

1. **User Profiles**:
   - A typical example of a document resource in a social media API would be a user profile accessible through a URI like `/users/{userId}`. Clients can retrieve a user's profile, update it, or delete it, each operation corresponding to a specific HTTP method.

2. **Product Details**:
   - In an e-commerce API, each product might be represented as a document resource with a URI like `/products/{productId}`. This allows for detailed management of individual product entries.

3. **Configuration Settings**:
   - Individual configuration settings or system preferences can also be treated as document resources, where each setting is accessible and modifiable via its own unique URI.

#### Design Considerations

- **Granularity**: The level of detail included in a document resource should balance between providing complete information and avoiding overly large payloads. The design might include mechanisms for fetching partial resources if needed.

- **Versioning**: As entities change over time, managing versions of document resources or handling concurrent edits (e.g., with ETags for caching and conflict detection) can be crucial.

- **Hypermedia Controls**: To make document resources more discoverable and self-descriptive, embedding links to related resources and actions (following the HATEOAS principle) enhances usability and navigability.

- **Security**: Access to document resources must be carefully managed to prevent unauthorized access or manipulation. Security measures might include authentication, authorization, and secure data transmission protocols.

Document resources are pivotal in RESTful design, representing the core entities with which clients interact. They provide a structured and intuitive way to manage the entities' lifecycles via standard web protocols, making them a natural fit for web-based APIs that require direct, standardized access to individual data items.

### Collection resources

Collection resources represent a group or list of items that are of the same type. These resources are essentially containers that manage and organize multiple instances of a particular resource, often corresponding to the "document resources" they contain. Collections are a fundamental aspect of RESTful design because they provide a systematic way to handle sets of similar entities.

#### Characteristics

1. **Grouping of Similar Entities**:
   - Collection resources group similar entities together under a common umbrella. Each item within the collection typically represents an individual document resource.

2. **Uniform Interface**:
   - Like all REST resources, collection resources are manipulated through standard HTTP methods. For example:
     - **GET** to retrieve the entire collection or a subset of items within it.
     - **POST** to add a new item to the collection.
     - **PUT** or **DELETE** might not typically apply to the entire collection in standard practices but could be used in specific contexts (like replacing or deleting multiple resources at once if the API design allows it).

3. **Identifiable by URIs**:
   - Each collection has a unique URI which clients use to interact with it. Items within the collection can also be accessed by appending the item identifier to the collection’s URI (e.g., `/items/{itemId}`).

4. **Scalable Interaction**:
   - APIs should provide mechanisms to efficiently interact with large collections, such as pagination, filtering, and sorting. This allows clients to request subsets of data, manage data retrieval effectively, and interact with large data sets without performance degradation.

#### Example Use Cases

1. **Users List**:
   - An API managing user data might have a collection resource accessible via `/users` that lists all users. A `GET` request to this endpoint would retrieve the list of users, while a `POST` request with a user object would add a new user to the system.

2. **Product Catalog**:
   - For an e-commerce platform, `/products` might represent the collection of all products available for sale. Clients can retrieve all products or post a new product to this collection.

3. **Blog Posts**:
   - A blogging platform could use `/posts` as a collection resource to manage blog posts. The collection supports operations such as retrieving all posts and adding new posts.

#### Design Considerations

- **Pagination**: Large collections should implement pagination to limit the number of items returned in a single response. This reduces the load on both the server and client and improves the user experience by providing data in manageable chunks.

- **Filtering and Sorting**: Providing parameters to filter and sort the collection can greatly enhance the usability and efficiency of the API. For example, allowing users to retrieve all products of a certain type or all posts by a specific author.

- **Hypermedia as the Engine of Application State (HATEOAS)**: Including hypermedia links in the collection's response can guide clients through the available actions, like links to the detailed view of items or actions to the next page of the collection.

- **Security**: Access control mechanisms are essential to protect the data, especially when the collections contain sensitive information. Proper authentication and authorization should ensure that clients can only access data permitted by their access levels.

### Store resources in detail

Store resources behave like a repository or container for other resources. This type of resource is particularly useful when the API consumers need to have control over the creation and management of the resources within the store, including setting or knowing the identifiers (URIs) of these resources.

#### Characteristics

1. **Client-Assigned Identifiers**:
   - In most RESTful designs, the server typically assigns resource identifiers automatically (like auto-incrementing IDs or UUIDs). However, in a store resource scenario, clients can specify the identifier when they create a new resource. This is common in scenarios where the resource identifier needs to be predictable or meaningful, such as user-defined filenames in a storage API.

2. **Resource Management**:
   - Clients have the capability to add, remove, and update resources within the store. This is similar to a collection, but with the added capability that clients often manage the existence of these resources directly.

3. **Independent Lifecycle**:
   - Each resource within a store can have its own lifecycle, independent of others in the same store. For example, in a file storage API, each file can be created, modified, and deleted independently.

#### Example Use Cases

1. **File Storage Services**:
   - An API that allows users to upload, retrieve, and manage files. Users can specify file names (identifiers) when uploading files, and these names are used to access the files later. The API endpoint might look like `PUT /files/{filename}` for uploading or updating a file and `GET /files/{filename}` to retrieve it.

2. **Customizable Data Stores**:
   - APIs that allow users to define their data structures or schemas, such as a database service where users can create tables with specific names and access them directly via the API. The API might allow users to perform operations like `POST /databases/{dbname}/tables/{tablename}` to create a new table.

3. **Configuration Settings**:
   - An API where clients can store and retrieve configuration settings by key. Each setting can be accessed through a unique key provided by the client, such as `GET /settings/{key}` to fetch a setting and `PUT /settings/{key}` to update or create a setting.

#### Design Considerations

- **Validation and Security**: Since clients can specify identifiers, the API must robustly validate these to avoid conflicts, overwriting, security issues related to unauthorized access, or injection attacks.
- **Resource Cleanup and Management**: APIs need to handle scenarios where resources are no longer needed or when they should be cleaned up, possibly through expiration mechanisms or explicit deletion APIs.
- **Scalability and Performance**: Managing a large number of client-defined resources can introduce challenges in terms of indexing, lookup performance, and data consistency, which need to be addressed in the API's design.

Store resources give clients a significant degree of control over the resources they interact with, making them a powerful but complex component of REST API architecture. This design pattern is particularly useful when the API’s use case requires a high level of customization and direct management of resource identifiers by the clients.

### Controller resources in detail

Controller resources encapsulate operations or actions rather than data entities. These resources are particularly useful for exposing functionalities that don't naturally map to the standard Create, Read, Update, and Delete (CRUD) operations typically associated with resource-oriented APIs.

#### Characteristics

1. **Action-Oriented**:
   - Controller resources are typically designed to perform specific actions or operations. These resources often represent procedural concepts or functions rather than data.

2. **State Changes**:
   - Invoking a controller resource usually results in a change of state or side effects in the system, such as processing a payment, changing configuration settings, or triggering a complex workflow.

3. **Non-Idempotent Operations**:
   - While not exclusively so, many controller resources implement non-idempotent operations, meaning that the same operation can have different effects when executed multiple times. For example, a "restart" operation on a service may be non-idempotent.

4. **URL Design**:
   - Controller resources are often expressed as verbs or verb phrases in the API URL to clearly indicate the action being performed, e.g., `/restartServer` or `/processPayment`.

#### Example Use Cases

1. **Payment Processing**:
   - An API endpoint that triggers a payment transaction might be designed as a controller resource. For example, `POST /processPayment` could accept payment details and carry out the transaction.

2. **Job or Task Management**:
   - For systems that manage long-running jobs or tasks, a controller resource might be used to start or stop these tasks. For instance, `POST /jobs/{jobId}/start` and `POST /jobs/{jobId}/stop` could control the execution of jobs.

3. **Complex State Changes**:
   - In scenarios where an entity needs to undergo a complex state transition that cannot be simply described by updating fields, a controller resource might be used. For example, `POST /orders/{orderId}/cancel` could handle the specific logic required to cancel an order.

### Design Considerations

- **Clear Intent**: It should be clear what action a controller resource performs, and the API should document potential side effects or state changes resulting from the action.
  
- **Security and Permissions**: Since controller resources can trigger significant changes in the system, securing these endpoints is crucial. Proper authentication and authorization mechanisms must be in place to ensure that only entitled users can execute these operations.

- **Idempotency and Safety**: While many controller actions are non-idempotent, designing some controller endpoints to be idempotent when possible can improve the reliability and predictability of the API. For example, designing an activation endpoint that can be safely called multiple times without adverse effects.

- **Feedback and Response**: Controller resources should provide appropriate feedback about the outcome of the operation, including success, failure, and any relevant state changes or results from the action.

Controller resources in REST API design are used to model actions that are more procedural and less about directly managing resource states. They are a powerful tool for API designers to encapsulate operations that do not fit neatly into the CRUD paradigm, allowing for more flexible and expressive service interfaces.

## REST and DDD

In Domain-Driven Design (DDD), the focus is on modeling a software domain comprehensively and accurately, using an ubiquitous language shared by developers and domain experts. This model then informs the architecture of the system, aiming to reflect the real-world complexities and rules of the domain. When integrating RESTful API design with Domain-Driven Design, the different types of resources (Document, Collection, Store, and Controller) can be mapped onto elements of the domain model to create a powerful and coherent system.

### Document Resources and DDD

**Document resources** in REST correspond closely to **Entities** in DDD. Entities are objects with a distinct identity that are tracked through different states and lifetimes. Each document resource typically represents a single entity, with its unique identifier and full lifecycle management. By modeling entities as document resources, a REST API can maintain the identity and integrity of domain objects, ensuring that they can be created, retrieved, updated, and deleted individually.

- **Example**: A `Customer` entity in DDD could be represented as a `/customers/{customerId}` document resource in a REST API, where each customer is uniquely identifiable and can be managed directly via the API.

### Collection Resources and DDD

**Collection resources** map well to **Repositories** in DDD. Repositories are used to manage collections of entities and provide methods to retrieve and store them. In a REST API, collection resources provide endpoints to access lists of entities and add new entities to the domain. This aligns with the repository pattern, which abstracts the collection operations away from the core domain model, facilitating domain logic that focuses on individual entities without worrying about data access mechanics.

- **Example**: A repository handling `Product` entities in a domain model would correspond to a `/products` collection resource in REST, allowing clients to retrieve all products or add new ones to the collection.

### Store Resources and DDD

**Store resources** are similar to collections but with added flexibility that allows clients to define identifiers for stored resources. This can be likened to a more flexible form of repository or a service in DDD that allows for direct client control over the identities of entities or value objects. Store resources are less common in standard DDD models but can be useful for domains where entities or value objects must be client-defined.

- **Example**: A file storage system where clients specify file paths and names when storing files, akin to a `FileRepository` or `StorageService` in DDD, could be implemented as a `/files/{filePath}` store resource in REST.

### Controller Resources and DDD

**Controller resources** in REST represent operations or commands in DDD. These are actions that typically don't fit neatly into CRUD operations, corresponding instead to **Domain Services** or **Application Services** that perform specific domain tasks or transactions. Controller resources often encapsulate complex business logic that involves more than simple data retrieval or storage, thus acting as the operational side of a domain-driven design.

- **Example**: An operation like processing a payment, which might involve complex validations and interactions between different domain entities and services, can be encapsulated in a RESTful controller resource like `/processPayment`.

### Integrating REST and DDD

Integrating these REST resource types into a DDD architecture involves careful alignment to ensure that the RESTful interface accurately represents and interacts with the underlying domain model. This integration should respect the boundaries set by aggregates in DDD, use repositories to manage collections of entities, treat entities as document resources with unique identities, and handle complex domain operations through controller resources. This approach not only maintains the purity and integrity of the domain model but also leverages the scalability and flexibility of RESTful services to expose the domain to a wide range of clients.

<!-- Keywords -->
#json #apis #api #schemas
<!-- /Keywords -->

## References

https://research.google/pubs/zanzibar-googles-consistent-global-authorization-system/
https://zanzibar.academy/
https://workos.com/blog/google-zanzibar


## Summary

### Introduction

Google Zanzibar is a centralized authorization system designed to handle access control at an unprecedented scale, powering authorization for hundreds of Google services, including Gmail, Drive, YouTube, and Maps. It was introduced through a 2019 whitepaper and has since gained significant recognition, influencing both proprietary and open-source authorization solutions.

### Key Characteristics

Zanzibar’s defining features are its support for fine-grained, relationship-based access control (ReBAC) and its centralized nature. It uses relational tuples to represent permissions in a graph structure and offers APIs for querying and managing access. These capabilities enable Zanzibar to address the unique challenges of managing permissions across Google's diverse ecosystem of services with the following goals:
- **Correctness:** Strong consistency and fault tolerance, ensuring accurate authorization decisions.
- **Scalability:** Designed to handle billions of objects and users, processing millions of queries per second.
- **Speed and Availability:** Targeting sub-10ms latency, Zanzibar employs caching, replication, and distributed architectures to ensure high availability and low response times.

### Core Components

1. **Data Model:** Relational tuples define relationships between objects, users, and permissions, e.g., `document:123#viewer@user:456`.
2. **Configuration Language:** Enables flexible definitions of access control policies using constructs like unions, intersections, and computed relationships.
3. **APIs:** Core methods include:
   - **Read:** Retrieve access control data.
   - **Write:** Modify permissions.
   - **Check:** Verify permissions for a user-resource pair.
   - **Expand:** Enumerate permissions for a resource.
   - **Watch:** Monitor changes in permissions.
4. **Storage and Consistency:** Relies on Google Spanner for global consistency and replication. It introduces "zookies" (Zanzibar cookies) for client-defined consistency across authorization queries.

### Innovations
- **Graph-Based Model:** Zanzibar replaces traditional Access Control Lists (ACLs) and Role-Based Access Control (RBAC) with a graph model, enabling complex, hierarchical relationships.
- **User-Specified Consistency:** Clients can choose tradeoffs between performance and consistency on a per-query basis using zookies.
- **Optimizations:** Caching layers and global replication reduce latency, while request hedging mitigates tail latency issues.

### Strengths

1. **Centralized Authorization:** Acts as a single source of truth, providing consistent authorization decisions across services.
2. **Flexible and Fine-Grained:** Supports diverse use cases, from consumer applications (e.g., Google Docs sharing) to enterprise systems (e.g., role-based cloud access).
3. **Scalability:** Built to handle Google’s global scale with trillions of rules and billions of users.
4. **Reverse Indexing:** Supports queries like “What resources can this user access?” which are crucial for audits and debugging.

### Challenges

1. **Data Centralization:** Requires duplicating all authorization-related data (roles, hierarchies, attributes) in Zanzibar, increasing complexity.
2. **Resource Intensive:** Demands significant engineering effort to implement and maintain; Google employs a dedicated team for Zanzibar.
3. **Limited Extensibility:** Pure Zanzibar systems lack support for attributes (e.g., time or location constraints), which are essential in Attribute-Based Access Control (ABAC).
4. **Opinionated Design:** Focused heavily on ReBAC, making integration with existing RBAC or ABAC systems challenging without additional abstractions.

### Applications and Alternatives

Zanzibar-inspired systems have been adopted by companies like Airbnb (Himeji) and Carta. Open-source implementations aim to democratize its usage, but these require expertise to scale effectively. Alternatives include:
- **Open Policy Agent (OPA):** Stateless policy engine supporting ABAC and RBAC.
- **Casbin:** Lightweight library for ACL, RBAC, and ABAC.
- **Permit.io:** Combines Zanzibar with other policy models for extensibility.

See also [[Access control in Python]], [[RBAC]].

### Conclusion

Google Zanzibar represents a pioneering approach to fine-grained authorization at scale, combining graph-based models, centralized policies, and distributed systems. While its implementation demands significant resources and commitment, it offers unparalleled benefits for organizations requiring hierarchical, relationship-aware access control. However, its suitability depends on specific needs, such as the complexity of authorization queries and the importance of hierarchical relationships. For broader use cases, hybrid solutions integrating Zanzibar with ABAC or RBAC may offer the best of both worlds.

#authorization #rbac #abac #rebac

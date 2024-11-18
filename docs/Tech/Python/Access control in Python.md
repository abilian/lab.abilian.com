
## Intro

https://medium.com/identity-beyond-borders/a-beginners-guide-to-xacml-6dc75b547d55
https://medium.com/globant/attribute-based-access-control-in-a-microservices-architecture-7c68f633b2d3

## Standards

https://en.wikipedia.org/wiki/XACML
https://www.identityserver.com/documentation/enforcer/alfa/QuickGuideToAlfa/
https://en.wikipedia.org/wiki/Abbreviated_Language_for_Authorization

## Research

https://www.researchgate.net/publication/339352934_PEP4Django_-_A_Policy_Enforcement_Point_for_Python_Web_Applications
https://www.researchgate.net/publication/315638965_A_Systematic_Approach_to_Implementing_ABAC

## See also

[[Zanzibar]]

## Projects
### Vakt

https://github.com/kolotaev/vakt

"Vakt is an attribute-based and policy-based access control (ABAC) toolkit that is based on policies. ABAC stands aside of RBAC and ACL models, giving you a fine-grained control on definition of the rules that restrict an access to resources and is generally considered a "next generation" authorization model. In its form Vakt resembles IAM Policies, but has a way nicer attribute managing."

### py-abac

https://pypi.org/project/py-abac/
https://py-abac.readthedocs.io/en/latest/
https://github.com/ketgo/py-abac

"Py-ABAC is an attribute-based access control (ABAC) toolkit based on policies. ABAC gives you a fine-grained control on definition of the rules that restrict an access to resources and is generally considered a "next generation" authorization model. The design of py-ABAC stems from the XACML standard, and the ABAC python SDK Vakt."

### SGL

https://pypi.org/project/sgl/
https://github.com/evernym/sgl

"SGL is a simple but flexible [DSL](https://en.wikipedia.org/wiki/Domain-specific_language) for matching people against criteria (typically, authorization). It is like [XACML](https://en.wikipedia.org/wiki/XACML) but simpler and JSON-oriented. You can use it to write rules about who should be able to do what, and then to compare circumstances to the rules to enforce custom logic. This lets you create your own [Role-Based Access Control](https://en.wikipedia.org/wiki/Role-based_access_control) mechanisms, as well as authorizations based on other criteria."

### Permit

https://docs.permit.io/sdk/python/usage-example

### Cerbos

https://github.com/cerbos/cerbos-sdk-python

### OSO

API:

```
authorize(actor, action, resource) : Ensure that an actor can perform an action on a certain resource. Read about resource-level enforcement.

authorize_request(actor, request) : Ensure that an actor is allowed to access a certain endpoint. Read about request-level enforcement.

authorize_field(actor, action, resource, field) : Ensure that a actor can perform a particular action on one field of a given resource. Read about field-level enforcement.
authorized_fields(actor, action, resource)

authorized_actions(actor, resource) : List the actions that actor is allowed to take on resource.

authorized_fields(actor, action, resource) : List the fields that actor is allowed to perform action upon.
```

## DSL

ALFA (see above)
https://github.com/kazuare/alfa-dsl-playground (Kotlin internal DSL)

In Python:

```python
policyset = PolicySet("Root", FirstApplicable, [
    PolicySet("NestedPolicy", FirstApplicable, [
        Policy("NotApplicablePolicy", DenyUnlessPermit, [
            Target(user.function == "support"),
            Rule(Deny)
        ]),
        Policy("ActualPolicy", DenyUnlessPermit, [
            Target(user.active == False),
            Rule(Permit, [
                Target(user.login == "user@mail.com",
            ])
        ])
    ])
])
```


## Comparisons

### Comparison: SGL vs. Vakt

Both **SGL (Simple Grant Language)** and **Vakt** are tools for managing access control, but they serve different purposes, follow distinct paradigms, and are optimized for different use cases. Below is a detailed comparison:

---

### Core Philosophy

| Feature               | **SGL**                                                                                     | **Vakt**                                                                                  |
|-----------------------|---------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|
| **Model**             | Privilege-based access control with conditions.                                             | Attribute-Based and Policy-Based Access Control (ABAC).                                  |
| **Granularity**       | Focuses on **privileges** tied to roles and conditions.                                      | Enables fine-grained control based on **attributes** and complex conditions.             |
| **Flexibility**       | Simpler structure with limited rule complexity.                                              | Highly customizable and supports complex, dynamic policies.                              |
| **Design Philosophy** | Designed for scenarios requiring hierarchical privilege relationships (e.g., guardianship). | General-purpose tool for building dynamic access control systems.                        |

---

### Architecture and Workflow

| Feature                  | **SGL**                                                                                         | **Vakt**                                                                                  |
|--------------------------|-------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|
| **Policy Definition**    | Rules define privileges (e.g., `medical-care`, `travel`) with specific conditions.              | Policies define access based on attributes of resources, subjects, actions, and context. |
| **Decision Process**     | Evaluates privileges and conditions for principals using simple API calls (`satisfies()`).       | Evaluates whether an inquiry satisfies a policy using a `Guard` with customizable checkers. |
| **Target Resources**     | Focused on managing privileges for a specific set of use cases.                                  | Supports general-purpose resource, subject, action, and context matching.                |
| **Execution**            | Rules are evaluated dynamically using principal objects.                                         | Inquiry-based evaluation against a set of policies stored in a backend.                  |

---

### Policy Representation

| Feature                  | **SGL**                                                                                         | **Vakt**                                                                                  |
|--------------------------|-------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|
| **Structure**            | JSON-like rules define conditions and privileges.                                               | Policies are Python objects with attributes for resources, actions, context, and effect. |
| **Condition Complexity** | Supports **basic conditions** like role counts or logical relationships.                        | Supports **complex conditions** with attribute-based rules, regex, and logical operators. |
| **Customization**        | Limited to predefined roles and conditions.                                                     | Extensible: supports user-defined rules and dynamic attributes.                          |
| **Effect**               | Implicitly grants or denies privileges based on conditions.                                      | Explicitly specifies `ALLOW_ACCESS` or `DENY_ACCESS` as policy outcomes.                 |

---

### Use Cases

| Feature                  | **SGL**                                                                                         | **Vakt**                                                                                  |
|--------------------------|-------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|
| **Primary Use Cases**    | Ideal for hierarchical or role-based privilege systems (e.g., guardianship, family access).     | Suitable for complex, dynamic environments (e.g., enterprise systems, cloud infrastructure). |
| **Example Scenarios**    | - Assigning permissions to guardians based on familial relationships.<br>- Conditional access requiring multiple approvals. | - Controlling API access in microservices.<br>- Implementing dynamic rules for SaaS platforms.<br>- Securing cloud resources (IAM-like). |
| **Domain Focus**         | Narrow focus on privilege management in specific domains.                                       | General-purpose; applicable to any domain needing dynamic access control.                |

---

### Rules and Attributes

| Feature                  | **SGL**                                                                                         | **Vakt**                                                                                  |
|--------------------------|-------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|
| **Rule Types**           | - Role-based (`roles` attribute).<br>- Logical relationships (`any`, `all`).<br>- Numeric counts (`n`). | - Attribute-based (`Eq`, `Greater`, `Less`, etc.).<br>- Logical (`And`, `Or`, `Not`).<br>- String manipulation (`StartsWith`, `RegexMatch`). |
| **Contextual Rules**     | Limited to predefined conditions (e.g., role counts or combinations).                           | Fully supports context (e.g., IP restrictions, referrer URLs).                           |
| **Custom Rules**         | Not supported; relies on predefined patterns.                                                   | Allows custom rule definitions and extensions.                                           |

---

### Storage and Integration

| Feature                  | **SGL**                                                                                         | **Vakt**                                                                                  |
|--------------------------|-------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|
| **Storage**              | No dedicated storage; relies on JSON representations and external principal data sources.       | Supports multiple backends: in-memory, MongoDB, SQL, Redis.                              |
| **Integration**          | Tight coupling with SGL API; limited external compatibility.                                    | Integrates with existing systems via inquiry objects; flexible API.                      |
| **Caching**              | Not supported.                                                                                  | Supports caching at multiple layers (policies, decisions, storage).                      |

---

### Performance and Scalability

| Feature                  | **SGL**                                                                                         | **Vakt**                                                                                  |
|--------------------------|-------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|
| **Performance**          | Optimized for small-scale, single-purpose use cases.                                            | Designed for scalability; performance varies by storage and policy complexity.           |
| **Scalability**          | Limited; rules and evaluations are relatively static.                                           | Scalable with support for large policy sets, caching, and optimized storage.             |

---

### Strengths and Limitations

| Feature                  | **SGL**                                                                                         | **Vakt**                                                                                  |
|--------------------------|-------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|
| **Strengths**            | - Simplicity.<br>- Easy to use and configure.<br>- Focused on domain-specific scenarios.         | - Flexibility.<br>- Extensible and customizable.<br>- Broad use-case applicability.       |
| **Limitations**          | - Limited to predefined privilege-based rules.<br>- Not suitable for large-scale or dynamic systems. | - More complex setup.<br>- May require significant effort for highly specific use cases. |

---

### Choosing Between SGL and Vakt

| **Criterion**                        | **When to Use SGL**                                      | **When to Use Vakt**                                  |
|--------------------------------------|----------------------------------------------------------|------------------------------------------------------|
| **Simplicity**                       | When rules are simple and domain-specific.               | When policies and conditions are complex.            |
| **Granularity**                      | When broad privilege assignments suffice.                | When fine-grained access control is needed.          |
| **Scalability**                      | For small, static rule sets and few principals.          | For dynamic, large-scale environments.               |
| **Customization**                    | When predefined rules cover all requirements.            | When custom attributes and extensibility are needed. |
| **Integration with Existing Systems**| Limited; best for standalone privilege management.       | High; can integrate into existing ABAC workflows.    |

---

### Conclusion

Vakt offers more flexibility and extensibility at the cost of additional complexity. SGL, on the other hand, provides a streamlined solution for specific privilege management scenarios.

- Use **SGL** when simplicity, predefined privilege rules, and hierarchical relationships are central to your requirements. Examples include guardianship, family access control, or static domain-specific privilege assignments.
- Use **Vakt** when you need fine-grained, attribute-based, and dynamic access control. Examples include securing cloud environments, API management, or complex enterprise systems.


<!-- Keywords -->
#authorization
<!-- /Keywords -->

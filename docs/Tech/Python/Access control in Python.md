
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

<!-- Keywords -->
#authorization
<!-- /Keywords -->

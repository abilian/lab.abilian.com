Role-based access control (RBAC) is a method of regulating access to computer or network resources based on the roles of individual users within an organization. In RBAC, users are assigned to specific roles, and each role is associated with a set of permissions or access rights. Users are granted access to resources based on the roles they have been assigned, rather than on their individual identities.

For example, a user in the role of "manager" may be granted access to certain resources that are not available to a user in the role of "employee." This approach can simplify access management, as it allows organizations to manage access rights for groups of users at once, rather than having to manage access rights for each individual user.

RBAC is widely used in enterprise organizations, especially in large scale systems, because it allows organizations to manage access to resources in a more structured and efficient way, and also it allows to separate the roles of the users from the individual identities.

## Standards

-  NIST: https://csrc.nist.gov/projects/role-based-access-control
-  ANSI INCITS 359

## Libraries

- https://github.com/osohq/oso "Oso is a batteries-included library for building authorization in your application."
- Apache Fortress

## References

- https://en.wikipedia.org/wiki/Role-based_access_control
- https://blog.symops.com/2022/09/07/evolution-access-control-python/

## See also

### PBAC = "Purpose-Based Access Control (PBAC)"

A type of access control that limits access to resources based on the specific purpose for which the resource is being requested. This means that users are only granted access to resources if they have a legitimate need for them, and the access they are granted is limited to the specific tasks they need to perform. PBAC systems typically include a process for requesting and approving access, as well as a mechanism for revoking or modifying access as needed. This approach can help to improve security by reducing the risk of unauthorized access or misuse of resources. PBAC also helps to enforce compliance with regulations, such as data protection laws like GDPR, HIPAA and others. It also helps to meet the requirement of compliance standards such as SOC 2, PCI-DSS and others. 
PBAC also increases the efficiency of the organization by making sure that the resources are used only for the intended purpose and not wasted on unnecessary access."

### [OrBAC](https://fr.wikipedia.org/wiki/Contr%C3%B4le_d%27acc%C3%A8s_bas%C3%A9_sur_l%27organisation) = Organization-Based Access Control

The concepts of roles, views and activities are organisational concepts. Each organisation defines the roles, activities and views to which it wishes to regulate access by applying an authorisation policy.

Access control models are usually based on the three entities: subject, action, object. So, to control access, we specify whether a subject has permission to perform an action on an object.

The main aim of OrBAC is to enable a security policy to be defined independently of its implementation. The method chosen to achieve this goal is to introduce an abstract level.

- Subjects are abstracted into roles. A role is a set of subjects to which the same security rules are applied.
- Actions are abstracted into activities. An activity is a set of actions on which the same security rules are applied.
- Objects are abstracted into views. A view is a set of objects on which the same security rules are applied.

The OrBAC access control model is not restricted to permissions. It also includes the possibility of specifying prohibitions and obligations.

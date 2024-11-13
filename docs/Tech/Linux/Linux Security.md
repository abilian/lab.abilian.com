## Debian

https://unix.foo/posts/insecurity-of-debian/
→ The article critiques Debian's security framework, emphasizing that its reliance on **AppArmor**, though a positive step, is insufficient compared to Red Hat’s **SELinux** implementation. It argues that SELinux provides stronger security, with comprehensive policies applied consistently across the system, whereas Debian’s AppArmor profiles are limited, inconsistent, and often leave significant security gaps. Red Hat's proactive approach to security, particularly in container environments, offers robust isolation and protection, which Debian lacks due to resource constraints and less comprehensive security defaults.

## AppArmor vs. SELinux
 
- **Security Model**: SELinux is based on Mandatory Access Control (MAC) with fine-grained policies that define the actions every process can perform. AppArmor uses a simpler, path-based access control model.
  
- **Configuration**: SELinux policies are more complex and cover system-wide rules, while AppArmor is easier to configure, relying on profiles that restrict program behavior.

- **Adoption**: SELinux is more commonly used in Red Hat and CentOS, whereas AppArmor is popular in Debian and Ubuntu.

<!-- Keywords -->
#security
<!-- /Keywords -->

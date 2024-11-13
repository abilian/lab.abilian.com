GNU Guix is a powerful package manager and system distribution that emphasizes reproducibility, transparency, and user freedom. At the heart of Guix's functionality lies the `guix.scm` file, a crucial component for defining packages and configuring environments. This short guide will walk you through the process of creating your first Guix package, explaining the significance of the `guix.scm` file and its various applications in software development and deployment.

Whether you're a seasoned developer looking to streamline your build processes or a newcomer to Guix eager to harness its full potential, understanding how to craft and utilize a `guix.scm` file is essential. This knowledge will empower you to create reproducible builds, manage dependencies efficiently, and ensure consistent development environments across your team.

## References

### On MacOS

- [Guix System (GuixSD) VM on an M1 Mac](https://n8henrie.com/2022/10/guix-system-guixsd-vm-on-an-m1-mac/): describes setting up an aarch64 Guix System virtual machine on an M1 Mac.
- [MacOS Subsystem for Guix](https://superkamiguru.org/projects/msg.html)

### Package generator

- https://guix-hpc.gitlabpages.inria.fr/guix-packager/

### Service management

- https://guix.gnu.org/manual/devel/en/html_node/Shepherd-Services.html


---

(TODO: move an independent card).

## Tutorial: Your First Guix Package

The cornerstone of package management in Guix is the `guix.scm` file. This file serves as a blueprint for your package, defining its characteristics, build instructions, and dependencies. Let's explore the primary uses and benefits of a `guix.scm` file:

### Package Definition

1. **Package Metadata**: The `guix.scm` file contains crucial metadata about your package, including its name, version, source location, build system, and dependencies. This information allows Guix to uniquely identify and manage your package within its ecosystem.

2. **Build Instructions**: It specifies how to build the package from source, including any custom build phases or patches that may be necessary. This ensures that your package can be consistently built across different environments.

### Environment Configuration

1. **Development Environments**: One of the most powerful features of Guix is its ability to create reproducible development environments. The `guix.scm` file defines these environments by specifying dependencies and environment variables, ensuring consistency across different machines and team members.

2. **Containerized Environments**: Guix can create isolated environments or containers based on your `guix.scm` file, complete with all necessary dependencies. This is invaluable for both development and deployment scenarios, as it minimizes "it works on my machine" issues.

### Reproducible Builds

1. **Reproducibility**: By explicitly defining all aspects of the build process, Guix ensures that builds are reproducible. This means that the same source code will produce identical binary artifacts, regardless of the build environment.

2. **Dependency Management**: The `guix.scm` file allows for precise control over dependencies, avoiding version conflicts and ensuring that all required components are present for a successful build.

### Usage in CI/CD

1. **Continuous Integration**: The `guix.scm` file integrates seamlessly with CI/CD pipelines, ensuring consistent and reproducible builds throughout your development process. This is particularly useful for automating testing and deployment workflows.

2. **Automated Testing**: By providing a consistent environment for running automated tests, Guix helps ensure that your tests are reliable and reproducible, catching issues early in the development cycle.

### Collaboration

1. **Sharing Environments**: The `guix.scm` file makes it easy to share development environments among team members, ensuring that everyone is working with the same setup and reducing onboarding time for new contributors.

2. **Community Contributions**: For open-source projects, a well-defined `guix.scm` file enables contributors to quickly set up the necessary environment to build and test contributions, lowering the barrier to entry for community participation.

### Example of a `guix.scm` File

Here's a simple example to illustrate the structure and components of a `guix.scm` file:

```scheme
(use-modules (guix packages)
             (guix download)
             (guix build-system gnu)
             (gnu packages base))

(define-public my-package
  (package
    (name "my-package")
    (version "1.0.0")
    (source (origin
              (method url-fetch)
              (uri (string-append "https://example.com/my-package-" version ".tar.gz"))
              (sha256 (base32 "1l1z5jq4k3nnl1k1s8k8sk5qzcv6h1kpqwrp4j2c9a6ffk3j5spg"))))
    ;; Build
    (build-system gnu-build-system)
    (inputs
     `(("gcc" ,gcc)))
    ;; Additional metadata
    (home-page "https://example.com/my-package")
    (synopsis "A brief description of my package")
    (description "A detailed description of my package")
    (license gpl3+)))

my-package
```

## Key Components of `guix.scm`:

- **use-modules**: Specifies the Guix modules required for building the package.
- **define-public**: Defines a new package that can be used by other packages or directly by users.
- **package**: The main form that encapsulates all the package information and build instructions.
- **name, version, source**: Basic metadata that identifies the package and specifies where to obtain its source code.
- **build-system**: Specifies the build system to use (e.g., `gnu-build-system` for packages using the standard GNU build process).
- **inputs**: Lists the dependencies required to build and run the package.
- **home-page, synopsis, description, license**: Additional metadata that provides context and legal information about the package.

### Using the `guix.scm` File

Once you have created your `guix.scm` file, you can use it in various ways:

- `guix build -f guix.scm`: Builds the package defined in the file.
- `guix shell -f guix.scm`: Starts a shell with the given package and its dependencies available.
- `guix shell -C -f guix.scm`: Creates a more isolated environment (in a container) based on the package definition.

By mastering the creation and use of `guix.scm` files, you'll be well-equipped to manage packages, create reproducible builds, and maintain consistent development environments in the Guix ecosystem. This knowledge forms the foundation for advanced package management and system configuration, enabling you to fully leverage the power of GNU Guix in your projects.

### References

- https://guix.gnu.org/manual/en/html_node/Defining-Packages.html

<!-- Keywords -->
#guix #package
<!-- /Keywords -->

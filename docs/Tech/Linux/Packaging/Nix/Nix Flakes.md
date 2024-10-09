A **Nix Flake** is a feature in the **Nix** package manager that provides a standardized and declarative way to define and manage projects, packages, dependencies, and development environments. It simplifies the way Nix projects are packaged, versioned, and shared by introducing a **flake** as a well-structured, self-contained unit of code or configuration.

### Key Features of Nix Flakes:

1. **Reproducibility**: Flakes ensure that the same environment or package can be recreated anywhere, providing consistency across different systems and users.
   
2. **Dependency Pinning**: Flakes allow you to lock dependencies to specific versions, ensuring that builds remain reproducible even if upstream packages change.

3. **Composability**: Flakes can reference other flakes, allowing for easier reuse of configuration or packages across different projects. This makes it simpler to manage dependencies and compose complex projects from smaller, reusable parts.

4. **Standard Structure**: A Nix Flake has a standardized structure, usually defined in a `flake.nix` file, which clearly outlines how the package or project is built, what dependencies are required, and what outputs are expected (e.g., applications, libraries, development shells, etc.).

5. **Multiple Outputs**: Flakes support defining multiple outputs, such as:
   - **Packages**: Pre-built binaries or libraries.
   - **Development Shells**: Development environments that can be instantiated with `nix develop`.
   - **Apps**: Executable programs.
   - **Tests**: Automated tests for the flake.
   
6. **Easy Sharing**: Flakes simplify sharing Nix configurations by using the `flake.nix` file as a single source of truth, which can be distributed or referenced easily via Git repositories or other remote locations.

### Structure of a Nix Flake:

A Nix Flake is defined in a `flake.nix` file, which typically includes information like:
- **Inputs**: The dependencies of the flake (other flakes or packages).
- **Outputs**: What the flake provides, such as packages, applications, or development environments.

Here's an example structure of a `flake.nix` file:

```nix
{
  description = "A simple example Nix Flake";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs";
  };

  outputs = { self, nixpkgs }: {
    packages.default = nixpkgs.lib.mkShell {
      buildInputs = [ nixpkgs.hello ];
    };

    devShell = nixpkgs.mkShell {
      buildInputs = [ nixpkgs.gcc nixpkgs.cmake ];
    };
  };
}
```

- **Inputs**: The `nixpkgs` input references the standard Nix package collection from GitHub.
- **Outputs**: It defines a default package and a development shell, each using dependencies from `nixpkgs`.

### How Nix Flakes are Used

- **Package Management**: Flakes make it easier to manage project dependencies by pinning specific versions and providing a consistent environment.
- **Development Environments**: Developers can use flakes to define and share reproducible development environments, ensuring that everyone on a team uses the same tooling and dependencies.
- **Continuous Integration/Deployment**: Flakes simplify CI/CD pipelines by providing a consistent, declarative way to define how applications are built and tested.

## Using Flakes

To use a Nix Flake, you'll need **Nix 2.4 or newer**, as flakes are a relatively new feature that requires enabling specific functionality in Nix. Below is a step-by-step guide on how to use a flake.

### Enable Flakes in Nix

Before using flakes, you need to enable them. To do this, add the following to your Nix configuration:

**For single commands**, you can enable flakes by passing the `--experimental-features` flag:
  
```bash
nix --experimental-features 'nix-command flakes' <command>
```

**To enable flakes globally** (recommended):
  Edit or create the `~/.config/nix/nix.conf` file and add the following line:

```bash
mkdir -p ~/.config/nix/
echo 'experimental-features = nix-command flakes' \
    >> ~/.config/nix/nix.conf
```


### Basic Commands to Use a Flake

Once flakes are enabled, here’s how you can use them in different contexts:

#### Clone and Explore a Flake
To fetch and inspect a flake from a remote repository, you can use the following command:

```bash
nix flake info github:<user>/<repo>
```

For example:

```bash
nix flake info github:NixOS/nixpkgs
```

This will show details about the flake, such as its inputs, outputs, and versions.

#### Run a Flake Application

If a flake provides applications, you can run them directly using the `nix run` command:

```bash
nix run github:<user>/<repo>#<app>
```

For example, to run the `hello` application from a flake:

```bash
nix run github:NixOS/nixpkgs#hello
```

This will download and execute the `hello` package from the specified flake.

#### Enter a Development Environment (DevShell)

If a flake defines a **development shell**, you can enter it using the `nix develop` command:

```bash
nix develop github:<user>/<repo>
```

This command drops you into a shell where all the dependencies required for development (as specified by the flake) are available. For example:

```bash
nix develop github:NixOS/nixpkgs
```

This is particularly useful for ensuring that all developers working on a project have the same development environment.

#### Build a Flake

If the flake provides build outputs (such as applications, packages, or containers), you can build them using the `nix build` command:

```bash
nix build github:<user>/<repo>#<package>
```

For example:

```bash
nix build github:NixOS/nixpkgs#hello
```

This command fetches the source code and dependencies, builds the application, and stores the resulting output in the `./result` symlink, which you can run or inspect.

### Create Your Own Flake

You can also create your own flake. Here's how to get started:

#### Create a `flake.nix` File

In your project’s directory, create a `flake.nix` file. Below is a simple example that provides a development shell and an application:

```nix
{
  description = "A simple example Nix Flake";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs";
  };

  outputs = { self, nixpkgs }: {
    packages = {
      default = nixpkgs.hello;
    };

    devShell = nixpkgs.mkShell {
      buildInputs = [ nixpkgs.gcc nixpkgs.cmake ];
    };
  };
}
```

- **Inputs**: This defines external dependencies (in this case, `nixpkgs` from GitHub).
- **Outputs**: This defines the flake's outputs:
  - `packages.default`: Points to a package (in this case, the `hello` application).
  - `devShell`: Defines a development shell with `gcc` and `cmake` installed.

#### Build Your Flake

You can build your flake with:

```bash
nix build
```

This will build the `default` package specified in the `flake.nix` file.

#### Enter the DevShell

To enter the development shell defined in the flake:

```bash
nix develop
```

This will provide you with a shell where `gcc` and `cmake` are pre-installed.

### Pin Dependencies with `flake.lock`

When you use or create a flake, Nix will automatically generate a `flake.lock` file. This file locks the versions of all inputs (such as `nixpkgs`), ensuring that builds remain reproducible even if the upstream repositories change.

For example, if you're using the latest version of `nixpkgs`, `flake.lock` ensures that subsequent builds use the same version unless you manually update the lock file.

To update your dependencies, run:

```bash
nix flake update
```

### Use Local Flakes

If you're working on a local flake, you can reference it using a path:

```bash
nix develop ./my-flake
```

This lets you test local flakes and ensure they are working as expected before sharing them.

### Summary of Common Commands:

| Command                         | Description                                                  |
|----------------------------------|--------------------------------------------------------------|
| `nix flake info <flake>`         | Show information about a flake (e.g., inputs, outputs).       |
| `nix run <flake>#<app>`          | Run an application provided by a flake.                      |
| `nix develop <flake>`            | Enter a development shell provided by a flake.               |
| `nix build <flake>#<package>`    | Build a specific package from the flake.                     |
| `nix flake update`               | Update the lock file to use the latest versions of inputs.    |

## Summary

Nix Flakes introduce a more structured and user-friendly approach to managing Nix projects by providing reproducibility, dependency pinning, and ease of sharing. They help simplify complex workflows, making it easier to manage environments, packages, and deployments across different systems while ensuring consistency and reliability. Using a Nix Flake allows you to manage dependencies, build environments, and share configurations in a declarative and reproducible way. Whether you're running pre-built applications or setting up a consistent development environment, flakes help streamline and standardize your workflow, ensuring consistency across different systems.

## References

- https://www.youtube.com/watch?v=JCeYq72Sko0 "Ultimate Nix Flakes Guide"
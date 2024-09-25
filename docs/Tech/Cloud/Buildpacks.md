#cloud #docker #containers #paas 

- Doc here: https://buildpacks.io/docs/buildpack-author-guide/create-buildpack/
- Intro (slides): https://docs.google.com/presentation/d/13j_Im9ZLPpAKmQmMSkkeZS9e4Tebhjc_bz8yTF8dR_w/edit#slide=id.p1

## Lifecycle

A buildback has the following components:

- `detect`: script (typically, shell-script)
- `build`: same (also: installs the environment, etc.)
- `buildpack.toml`: metadata for the buildback

It generates, for a given application:

- A "layer" (= the "compiled" application)
- A `launch.toml` metadata file, similar to:

```
[[processes]]
type = "web"
command = "bundle exec ruby app.rb"
default = true
```
- A SBOM (see: https://buildpacks.io/docs/buildpack-author-guide/create-buildpack/adding-bill-of-materials/)

Buildpacks are composable: https://buildpacks.io/docs/buildpack-author-guide/build-phases-overview/

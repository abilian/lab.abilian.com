"Simple" linux distribution (not for end-users but simple to understand).

https://kisslinux.org/ and https://github.com/kisslinux/

Simple packaging and build system.

Package manager is a bash script.

Packages ar described by a small set of files.

- build (a shell script, could be any language actually)
- version
- sources
- depends
- checksums
- /files
- /patches

-> Most of this could fit in a toml file.

The creator burned out then came back.

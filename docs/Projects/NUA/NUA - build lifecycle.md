
## Nua

- addons
- prep
- build
- install
- cleanup


Addons specifications:

```yaml
addons:
  apt:
    sources:
    - deadsnakes
    - sourceline: 'ppa:ubuntu-toolchain-r/test'
    - sourceline: 'deb https://packagecloud.io/chef/stable/ubuntu/precise main'
      key_url: 'https://packagecloud.io/gpg.key'
```

```toml
[build.addons]
sources = [
    "deadsnakes",
    "ppa:ubuntu-toolchain-r/test",
    { source ="https://packagecloud.io/chef/stable/ubuntu/precise main". key_url = "https://packagecloud.io/gpg.key"},
]
packages = [
    "gcc-4.8",
    "foobar",
]

[run.addons]
# same format
```

## RPM

- prep
- build
- install

Ref: https://janikvonrotz.ch/2019/03/20/the-final-rpm-packaging-guide/

## Travis

Each _job_ is a sequence of [phases](https://docs.travis-ci.com/user/for-beginners/#builds-jobs-stages-and-phases). The _main phases_ are:

1.  `install` - install any dependencies required
2.  `script` - run the build script

Travis CI can run custom commands in the phases:

1.  `before_install` - before the install phase
2.  `before_script` - before the script phase
3.  `after_script` - after the script phase.

The complete sequence of phases of a job is the lifecycle. The steps are:

1.  OPTIONAL Install [`apt addons`](https://docs.travis-ci.com/user/installing-dependencies/#installing-packages-with-the-apt-addon)
2.  OPTIONAL Install [`cache components`](https://docs.travis-ci.com/user/caching)
3.  `before_install`
4.  `install`
5.  `before_script`
6.  `script`


## Gentoo

The ebuild file format is in its basic form a subset of the format of a bash script.


##  Homebrew

https://docs.brew.sh/Formula-Cookbook

<!-- Keywords -->
#build #toolchain
<!-- /Keywords -->

#!/usr/bin/env python3.11

import subprocess as sp

POETRY = "/Users/fermigier/.local/bin/poetry"


def run(*args):
    sp.run(args, check=True)


def poetry_run(*args):
    run(*[POETRY, "run", *args])


def main():
    run("make", "clean")
    poetry_run("make", "sync")
    run("git", "add", "docs")
    run("git", "commit", "-a", "-m", "Update content")
    poetry_run("make", "deploy")


if __name__ == "__main__":
    main()

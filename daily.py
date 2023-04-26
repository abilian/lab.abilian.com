#!/usr/bin/env python3

import os
import subprocess as sp
from os import chdir
from pathlib import Path


HOME = os.environ["HOME"]
POETRY = f"{HOME}/.local/bin/poetry"


def run(*args, check=True):
    sp.run(args, check=check)


def poetry_run(*args):
    run(*[POETRY, "run", *args])


def main():
    chdir(Path(__file__).parent)
    run("make", "clean")
    poetry_run("make", "sync")
    run("git", "add", "docs")
    run("git", "commit", "-m", "Update content", check=False)
    poetry_run("make", "deploy")
    run("git", "push")


if __name__ == "__main__":
    main()

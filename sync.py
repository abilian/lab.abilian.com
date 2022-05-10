#!/usr/bin/env python3

import os
import shutil
from pathlib import Path

HOME = os.environ["HOME"]
SRC = f"{HOME}/Documents/Vaults/Notes"

IGNORED = {
    ".git", ".obsidian", ".DS_Store"
}

PUBLISH = [
    "Projects/Cython+",
    "Projects/Python to WASM Compiler",
    #
    "Tech/Architecture",
    "Tech/Cloud",
    "Tech/Containers",
    "Tech/Machine Learning",
    "Tech/Modeling",
    "Tech/Programming techniques",
    "Tech/Python",
    "Tech/Security",
    "Tech/Tools",
    "Tech/Security",
    "Tech/UX-UI",
    "Tech/Web",
]


def keep_file(src_path, root):
    rel_path = src_path.relative_to(root)

    keep = True
    for ignored in IGNORED:
        if f"/{ignored}/" in str(rel_path):
            keep = False
            break

    if not keep:
        return False

    for publish in PUBLISH:
        if str(rel_path).startswith(publish):
            return True

    return False


def main():
    if Path("docs").exists():
        shutil.rmtree("docs")

    root = Path(SRC)
    for src_path in root.rglob("**/*.md"):
        if not keep_file(src_path, root):
            continue

        rel_path = src_path.relative_to(root)
        content = src_path.open().read()
        if "#private" in content:
            continue

        dst_path = Path("docs") / rel_path
        dst_path.parent.mkdir(parents=True, exist_ok=True)
        dst_path.open("w").write(content)

    shutil.copy("pages/tags.md", "docs/")


if __name__ == "__main__":
    main()

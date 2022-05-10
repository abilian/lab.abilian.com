#!/usr/bin/env python3

import json
import os
import re
import shutil
from dataclasses import dataclass, field
from functools import cached_property
from pathlib import Path

from devtools import debug

HOME = os.environ["HOME"]
SRC = f"{HOME}/Documents/Vaults/Notes"
DST = "docs"

IGNORED = {".git", ".obsidian", ".DS_Store"}

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
    #
    "index.md",
]


@dataclass
class Page:
    path: Path
    root: Path

    tags: list = field(default_factory=list)

    def is_public(self):
        keep = True
        for ignored in IGNORED:
            if f"/{ignored}/" in str(self.rel_path):
                keep = False
                break

        if not keep:
            return False

        if "#private" in self.src_content:
            return False

        for publish in PUBLISH:
            if str(self.rel_path).startswith(publish):
                return True

        return False

    @cached_property
    def rel_path(self):
        return self.path.relative_to(self.root)

    @cached_property
    def dst_path(self):
        return Path(DST) / self.rel_path

    @cached_property
    def src_content(self):
        return self.path.open().read()

    def publish(self):
        self.dst_path.parent.mkdir(parents=True, exist_ok=True)

        content = self.make_content()
        self.dst_path.open("w").write(content)

    def make_content(self) -> str:
        title = ""
        src_lines = self.src_content.split("\n")
        result = []
        for line in src_lines:
            tags = re.findall(r"^#([\w-]+)", line) + re.findall(r"\s#([\w-]+)", line)
            if tags:
                for tag in tags:
                    self.tags.append(tag)
            else:
                result.append(line)

        title = ""
        for line in src_lines:
            if m := re.match("# (\S.*)$", line):
                title = m.group(1)
                break

        if not title:
            title = self.dst_path.name[0 : -len(".md")]
            result = [f"# {title}", ""] + result

        if self.tags:
            tag_line = json.dumps(self.tags)
            result = ["---", f"tags: {tag_line}", "---"] + result

        return "\n".join(result)


def main():
    if Path(DST).exists():
        shutil.rmtree(DST)
    os.makedirs(DST)

    root = Path(SRC)
    for src_path in root.rglob("**/*.md"):
        page = Page(src_path, root)
        if not page.is_public():
            continue

        page.publish()

    for path in Path("pages").glob("*.md"):
        debug(path)
        shutil.copy(path, DST)


if __name__ == "__main__":
    main()

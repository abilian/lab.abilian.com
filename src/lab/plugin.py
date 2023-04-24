import logging
import re
import time

import mkdocs
from mkdocs.plugins import BasePlugin

from lab.git import get_git_commit_timestamp

log = logging.getLogger(f"mkdocs.plugins.{__name__}")
log.addFilter(mkdocs.utils.warning_filter)


class MyPlugin(BasePlugin):
    def on_startup(self, *, command, dirty):
        pass

    def on_nav(self, nav, *, config, files):
        pass

    def on_page_markdown(self, markdown, *, page, config, files):
        tags = self._get_tags(markdown)
        tags.update(page.meta.get("tags", []))
        if tags:
            page.meta["tags"] = sorted(tags)

        title = self._get_title(markdown)

        if not title:
            markdown = f"# {page.title}\n\n" + markdown

        markdown = self._remove_tags(markdown)
        markdown = self._add_timestamp(page, markdown)

        return markdown

    def _get_tags(self, markdown: str) -> set[str]:
        src_lines = markdown.split("\n")
        tags = set()
        for line in src_lines:
            matches = re.findall(r"^#([\w-]+)", line) + re.findall(r"\s#([\w-]+)", line)
            if matches:
                for tag in matches:
                    tags.add(tag)

        return tags

    def _remove_tags(self, markdown: str) -> str:
        return re.sub(r"^#([\w-]+)", "", markdown, flags=re.MULTILINE)

    def _get_title(self, markdown: str) -> str:
        src_lines = markdown.split("\n")
        title = ""
        for line in src_lines:
            if m := re.match(r"# (\S.*)$", line):
                title = m.group(1)
                break

        return title

    def _add_timestamp(self, page, markdown: str) -> str:
        timestamp = get_git_commit_timestamp(page.file.abs_src_path)
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(timestamp))
        if timestamp:
            markdown += f"\n\n<small>Page last modified: {date}</small>\n"

        return markdown

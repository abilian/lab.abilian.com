import time
from pathlib import Path

import arrow
from snoop import pp

from lab.plugin.git import get_git_commit_timestamp

NOW = arrow.get(time.time())

DENY_LIST = [
    "docs/changelog.md",
    "docs/tags.md",
    "docs/index.md",
]

class ChangeLog:
    def __init__(self, output_file):
        self.output_file = Path(output_file).open("w")

    def process(self):
        entries = []
        for src_path in Path("docs").rglob("*.md"):
            if str(src_path) in DENY_LIST:
                continue
            timestamp = get_git_commit_timestamp(src_path)
            date = arrow.get(timestamp)
            entries.append([date, src_path])

        entries.sort(reverse=True)

        sections = [
            ["## Recent changes (last 7 days)", NOW.shift(days=-7), NOW],
            ["## Changed last 30 to 7 days", NOW.shift(days=-30), NOW.shift(days=-7)],
            ["## Changed last 90 to 30 days", NOW.shift(days=-90), NOW.shift(days=-30)],
            ["## Earlier changes", NOW.shift(years=-10), NOW.shift(days=-90)],
        ]

        self.output("# Changelog\n\n")

        for title, after, before in sections:
            subset = self.get_subset(entries, after, before)
            if not subset:
                continue

            self.output(title + "\n\n")

            self.print_changelog(subset)
            self.output("\n\n")

    def get_subset(self, entries, after, before):
        return [entry for entry in entries if after < entry[0] < before]

    def print_changelog(self, entries):
        for date, src_path in entries:
            title = str(src_path).split("/")[-1][0:-3]
            dest_path = "/" + str(src_path.relative_to("docs"))[0:-3] + "/"
            self.output(f"- [{title}]({dest_path}) ({date.format('YYYY-MM-DD')})\n\n")

    def output(self, text):
        self.output_file.write(text)

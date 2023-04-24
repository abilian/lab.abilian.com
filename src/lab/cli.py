import argparse
import importlib.metadata
import sys

from .changelog import ChangeLog
from .sync import sync

VERSION = importlib.metadata.version("lab.abilian.com")


def main():
    parser = argparse.ArgumentParser()

    # Generic / classic options
    parser.add_argument(
        "-v",
        "--verbose",
        default=0,
        action="count",
        help="Show more informations, until -vvv.",
    )
    parser.add_argument(
        "--version",
        "-V",
        action="version",
        version=f"lab version: ",
        help="Show version and exit.",
    )
    parser.add_argument(
        "command",
        help="Command to run (sync, map...)",
    )

    args = parser.parse_args(sys.argv[1:])
    match args.command:
        case "sync":
            sync()
        case "changelog":
            changelog = ChangeLog("docs/changelog.md")
            changelog.process()


if __name__ == "__main__":
    main()

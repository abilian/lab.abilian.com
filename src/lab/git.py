"""
MIT License

Copyright (c) 2018 Terry Zhao
Copyright (c) 2019 Tim Vink
Copyright (c) 2021 Liang Yesheng
Copyright (c) 2023 Stefane Fermigier

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

"""Utility class for mkdocs plugin."""

import logging
import os
import time
from git import (
    Git,
    Repo,
    GitCommandError,
    GitCommandNotFound,
    InvalidGitRepositoryError,
    NoSuchPathError,
)

from functools import cache

logger = logging.getLogger("mkdocs.plugins")


@cache
def _get_repo(path: str) -> Git:
    if not os.path.isdir(path):
        path = os.path.dirname(path)

    return Repo(path, search_parent_directories=True).git


@cache
def get_git_commit_timestamp(path: str, is_first_commit: bool = False) -> int:
    """
    FIXME: not the right docstring.

    Get a list of commit dates in unix timestamp, starts with the most recent commit.

    Args:
        is_first_commit (bool): if true, get the timestamp of the first commit,
                                else, get that of the most recent commit.
        path (str): Location of a markdown file that is part of a Git repository.
        is_first_commit (bool): retrieve commit timestamp when file was created.

    Returns:
        int: commit date in unix timestamp, starts with the most recent commit.
    """
    commit_timestamp = ""

    # perform git log operation
    try:
        # Retrieve author date in UNIX format (%at)
        # https://git-scm.com/docs/git-log#Documentation/git-log.txt-ematem
        # https://git-scm.com/docs/git-log#Documentation/git-log.txt---diff-filterACDMRTUXB82308203
        realpath = os.path.realpath(path)
        git = _get_repo(realpath)
        if is_first_commit:
            # diff_filter="A" will select the commit that created the file
            commit_timestamp = git.log(
                realpath, date="short", format="%at", diff_filter="A", follow=True
            )
            # A file can be created multiple times, through a file renamed.
            # Commits are ordered with most recent commit first
            # Get the oldest commit only
            if commit_timestamp != "":
                commit_timestamp = commit_timestamp.split()[-1]
        else:
            commit_timestamp = git.log(
                realpath, date="short", format="%at", n=1, follow=True
            )
    except (InvalidGitRepositoryError, NoSuchPathError) as err:
        logger.warning(
            "[blogging-plugin] Unable to find a git directory and/or git is not installed."
            " Falling back to build date."
        )
        commit_timestamp = time.time()
    except GitCommandError as err:
        logger.warning(
            "[blogging-plugin] Unable to read git logs of '%s'. Is git log readable?"
            " Falling back to build date." % path
        )
        commit_timestamp = time.time()
    except GitCommandNotFound as err:
        logger.warning(
            "[blogging-plugin] Unable to perform command: 'git log'. Is git installed?"
            " Falling back to build date."
        )
        commit_timestamp = time.time()

    # create timestamp
    if commit_timestamp == "":
        commit_timestamp = time.time()
        logger.warning(
            "[blogging-plugin] '%s' has no git logs, using current timestamp" % path
        )

    return int(commit_timestamp)

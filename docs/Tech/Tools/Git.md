## Tips

### How to "reboot" a repository

```bash
git checkout --orphan latest_branch
git add README.md
git commit -m "Init repo" README.md
git add -A
git commit -m "Import from private repo"
git branch -D main
git branch -m main
git gc --prune=now
```

### How to merge commits

Use `git rebase -i <after-this-commit>` and replace "pick" on the second and subsequent commits with "squash" or "fixup", as described in [the manual](https://git-scm.com/docs/git-rebase#_interactive_mode).

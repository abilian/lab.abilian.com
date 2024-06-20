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

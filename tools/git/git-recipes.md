
# Recipes for Git

---

## Show commit tree in terminal

```bash
git log --graph --decorate --pretty=oneline --abbrev-commit --all
```

  * We can create an alias in `.gitconfig`

```
[alias]
	tree = log --graph --decorate --pretty=oneline --abbrev-commit
```

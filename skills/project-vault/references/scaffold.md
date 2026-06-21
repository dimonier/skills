# Scaffold: ready-made `project-vault/` tree

The **`project-vault/`** directory here is a complete copy of the vault structure for a new repository. Paths below: **`<skill>`** = the directory containing this skill's `SKILL.md` (the parent directory of this file — go one level up).

## Copying into a repository

From the **repository root**, when there is no `project-vault/` directory yet:

```bash
cp -a <skill>/scaffold/project-vault ./project-vault
```

If `project-vault/` already exists, an incomplete `cp` may nest the copy inside — make a backup or deliberately remove the old directory first.

## Updating scaffold from a live vault

From the **repository root**, where `project-vault/` already exists:

```bash
rm -rf <skill>/scaffold/project-vault
cp -a project-vault <skill>/scaffold/project-vault
```

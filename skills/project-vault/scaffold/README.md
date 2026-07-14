# Scaffold: Ready-to-Use `project-vault/` Tree

The **`project-vault/`** directory here is a complete copy of the vault structure for a new repository. Paths below: **`<skill>`** = the directory containing this skill's `SKILL.md` (parent directory of this `scaffold/README.md` — one level up).

## Copying into a Repository

From the **repository root**, when `project-vault/` does not yet exist:

```bash
cp -a <skill>/scaffold/project-vault ./project-vault
```

If `project-vault/` already exists, a non-atomic `cp` may nest the copy inside — make a backup or delete the old directory deliberately.

## Updating Scaffold from a Live Vault

From the **repository root**, where `project-vault/` already exists:

```bash
rm -rf <skill>/scaffold/project-vault
cp -a project-vault <skill>/scaffold/project-vault
```

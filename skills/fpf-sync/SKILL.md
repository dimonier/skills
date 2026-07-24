---
name: fpf-sync
description: |
  Sync the fpf-core skill from the canonical FPF-Spec.md monolith.
  Use when: (1) the FPF specification has been updated (git pull shows new commits),
  (2) the fpf-core skill references/ are stale or show wrong counts,
  (3) running scheduled maintenance on LFW skills.
  Self-contained — bundles decompose_fpf.py + _common.py directly.
  No dependencies on external skills. Works only with the local skill at
  `../fpf-core/` (relative to this skill) — NOT the global user skill.
---

# FPF Core Skill Sync

**Bounded context:** Keeping `../fpf-core/` in sync with the canonical FPF monolith `../../FPF-Spec.md`.

**Self-contained** — all decomposition logic is bundled in `scripts/`. No external skill dependencies. Requires only Python 3.10+ and `git` in PATH.

## Quick Start

```bash
# Check if update is needed (exit code 0=up-to-date, 1=needs update):
python scripts/sync_fpf_core.py --check

# Full sync (git pull + copy + decompose + update SKILL.md):
python scripts/sync_fpf_core.py

# Preview without writing:
python scripts/sync_fpf_core.py --dry-run

# Sync without running git pull (use local state):
python scripts/sync_fpf_core.py --no-git
```

## Workflow

The script performs these steps in order:

1. **`git pull`** in repo root (`../..`) — fetch latest FPF-Spec.md
2. **Compare hashes** — `FPF-Spec.md` vs `skills/fpf-core/assets/FPF-Spec.md`. If identical, exit cleanly
3. **Copy monolith** — updated `FPF-Spec.md` → `skills/fpf-core/assets/FPF-Spec.md`
4. **Decompose** — calls bundled `decompose_fpf.parse_fpf_spec()` to rebuild all `references/*.md` + `INDEX.md` from the monolith. Uses idempotent writes — only changed files are overwritten
5. **Update `SKILL.md`** — refreshes line count (e.g. `100K+`) and reference counts (`291 pattern reference files + INDEX + 34 context sections`)
6. **Report** — prints counts, warnings, and errors

## Scripts

| File | Role | Size |
|---|---|---|
| `sync_fpf_core.py` | Orchestrator: git pull → diff → copy → decompose → update SKILL.md | 7 KB |
| `decompose_fpf.py` | FPF monolith parser: ToC parsing, `:End`-marker boundary detection, pattern extraction | 15 KB |
| `_common.py` | Shared utilities: reference formatting, YAML frontmatter, idempotent writes, INDEX generation | 7 KB |
| `errors.py` | Error types for pattern extraction | 1 KB |

## Error Handling

| Situation | Script behavior |
|---|---|
| `git pull` fails (network, auth) | Warning — continues with local state |
| Source `FPF-Spec.md` missing | Error — exits with code 2 |
| Decomposition produces warnings | Printed — exits with code 0 (non-fatal) |
| Decomposition produces errors | Printed — exits with code 1 |
| No changes detected | Exits cleanly with code 0 |

## SDC Alignment

This skill implements `SDC.SyncDiscipline` (Spec-Decomposer LPF) for the specific case of the `fpf-core` skill:

- **Unidirectional sync** (`AS.10:4.1`): monolith → references. Never the reverse.
- **Carrier split** (`AS.4:4.1`): agent reads `references/`, human edits `assets/FPF-Spec.md`
- **Full rebuild** on every change: copy monolith → decompose → update dispatcher
- **Idempotent writes**: `decompose_fpf.py` skips unchanged files

## Evolution

If the user is dissatisfied with the result or the FPF-Spec structure changes, offer to update this skill's script or its SKILL.md instructions.

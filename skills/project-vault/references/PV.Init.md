---
id: PV.Init
title: "Vault initialization: scaffold copy, inbox/outbox creation"
status: seed
readiness: source-faithful
keywords: [init, initialize, scaffold, bootstrap, setup, vault.py, inbox, outbox]
dependencies:
  builds_on:
    - C.33
    - E.4.DPF
  coordinates_with:
    - E.11
---

## PV.Init - Vault initialization: scaffold copy, inbox/outbox creation

> **Trigger:** When a new repository needs a project-vault, or when the scaffold of the skill must be (re)generated after a schema change.
> **Governing FPF patterns:**
>   → C.33 (kind discipline: the scaffold as a carrier template reproducing the schema)
>   → E.4.DPF (layering D5: a package-carrier returning to the authoritative subject)
> **Skill dependencies:**
>   → none

---

### PV.Init:1 - Problem frame

Use this pattern to initialize a new project-vault: copy the scaffold tree (a
repository-root template — `project-vault/` + `inbox/` + `outbox/`, including the
`project-vault/scripts/` CLI) and confirm the intake/output channels exist.

### PV.Init:2 - Problem

Initialization has no single canonical carrier: the scaffold copy and the
`inbox/`/`outbox/` creation are two unconnected facts. A new vault is assembled
ad hoc and drifts from the schema — risking a missing intake/output channel or a
missing CLI.

### PV.Init:3 - Forces

| Force | Settlement |
|---|---|
| Root template vs project-vault only | The scaffold is a repository-root template: `project-vault/` + `inbox/` + `outbox/`. |
| Copy vs hand-build | A single `cp -a` of the scaffold, which already carries `project-vault/scripts/`. |
| Empty channels vs clutter | `inbox/`/`outbox/` are created empty at init. |

### PV.Init:4 - Solution

1. **Copy the scaffold.** From the repository root, when `project-vault/` does not
   yet exist, copy the three scaffold trees — there is no README in the scaffold,
   so nothing overwrites the repository's own files. The scaffold already carries
   the CLI (`project-vault/scripts/vault.py`, `export_dec.py`), so no separate
   step is needed:
   `cp -a <skill>/scaffold/project-vault ./project-vault`,
   `cp -a <skill>/scaffold/inbox .`,
   `cp -a <skill>/scaffold/outbox .`.
2. **Verify.** Run `python project-vault/scripts/vault.py check` (or `next-id`) to
   confirm the CLI works.
3. **Tracking.** Empty scaffold directories carry a `.gitkeep` placeholder so git
   tracks the full tree; `git clone` reproduces every directory before it receives
   its first file.

### PV.Init:5 - Archetypal Grounding

**Show.** This repository was initialized by copying the scaffold (including
`project-vault/scripts/`) into the repository root and creating `inbox/` and
`outbox/`.

### PV.Init:6 - Bias-Annotation

The temptation is to initialize by hand-creating each directory "as needed", which
drifts from the canonical scaffold; the symmetric temptation is to forget
`inbox/`/`outbox/`, silently missing the intake/output channels. Counterweights:
copy the scaffold, create the channels at init.

### PV.Init:7 - Conformance Checklist

| ID | Requirement |
|---|---|
| CC-IN.1 | Init copies the scaffold (`project-vault/` + `inbox/` + `outbox/`), not a hand-built tree. |
| CC-IN.2 | The CLI comes with the scaffold copy (`project-vault/scripts/vault.py`). |
| CC-IN.3 | `inbox/` and `outbox/` exist at the repository root after init. |

### PV.Init:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
|---|---|
| Hand-built directory tree | Copy the scaffold. |
| Missing `inbox/`/`outbox/` | Create them at init. |

### PV.Init:9 - Consequences

A reproducible init gives every new vault the full schema + channels + CLI in one
copy. The scaffold is fixed by the skill and changes only when the schema itself
changes (edited directly, never derived from a live vault).

### PV.Init:10 - Rationale

`C.33` kind discipline: the scaffold is a carrier template reproducing the schema of
`PV.VaultSchema`. `E.4.DPF` layering D5: the scaffold is an access-facing package
returning to the authoritative subject (the schema).

### PV.Init:11 - SoTA-Echoing

| Source line | Adopt/adapt/reject | Locus in this card | Boundary |
|---|---|---|---|
| FPF `C.33` (kind discipline) | Adopt | Scaffold as a carrier template | Reopen on `C.33` revision |
| FPF `E.4.DPF` (layering D5) | Adopt | Scaffold package → authoritative schema | Reopen on `E.4.DPF` revision |

Best-known line: a reproducible, scaffold-driven init. Rejected rival: "hand-built
directory tree per repository" — rejected due to drift.

### PV.Init:12 - Relations

- **Builds on:** `C.33` (kind discipline), `E.4.DPF` (layering D5).
- **Coordinates with:** `E.11` (practical entry).
- **Applies to:** `PV.VaultSchema` (the schema it reproduces), `PV.Inbox` (creates `inbox/`), `PV.Outbox` (creates `outbox/`).

### PV.Init:End

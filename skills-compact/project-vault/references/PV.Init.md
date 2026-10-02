# PV.Init - Vault initialization: scaffold copy, inbox/outbox creation

> **Trigger:** When a new repository needs a project-vault, or when the scaffold of the skill must be (re)generated after a schema change.

```episteme id="PV.Init" context="ProjectVault"
Grounding (FPF):
  builds_on: C.33, E.4.DPF
  coordinates_with: E.11

UseThisWhen:
  initializing a new project-vault: copy the scaffold tree (repository-root template — project-vault/ + inbox/ + outbox/, incl. project-vault/scripts/) and confirm the intake/output channels exist

Result:
  a new vault with the full schema + channels + CLI in one copy, reproducing PV.VaultSchema

Solution:
  copyScaffold:
    from the repository root, when project-vault/ does not yet exist, copy the three scaffold trees (no README in the scaffold, so nothing overwrites the repo's own files)
    cp -a <skill>/scaffold/project-vault ./project-vault
    cp -a <skill>/scaffold/inbox .
    cp -a <skill>/scaffold/outbox .
    the scaffold already carries the CLI (project-vault/scripts/vault.py, export_dec.py) — no separate step
  verify:
    python project-vault/scripts/vault.py check (or next-id) to confirm the CLI works
  tracking:
    empty scaffold directories carry a .gitkeep placeholder so git tracks the full tree; git clone reproduces every directory before its first file
  offerAGENTS:
    when the LPF is used in skill form in a project, propose adding to the project's AGENTS.md an instruction that the project-vault skill is mandatory for vault work (if none exists); ask, do not write silently — the owner decides

Stop:
  project-vault/ + inbox/ + outbox/ exist at the repo root, the CLI runs, and the AGENTS.md offer is made (asked)

Checks:
  init copies the scaffold (project-vault/ + inbox/ + outbox/), not a hand-built tree
  the CLI comes with the scaffold copy (project-vault/scripts/vault.py)
  inbox/ and outbox/ exist at the repo root after init
  init proposes (asks, does not silently write) an AGENTS.md instruction on mandatory use of the project-vault skill

Antipatterns:
  hand-built directory tree → copy the scaffold
  missing inbox//outbox/ → create them at init
  a vault initialized without anchoring the skill → offer the AGENTS.md mandatory-use instruction (ask the owner)

Continues:
  PV.VaultSchema (the reproduced schema), PV.Inbox / PV.Outbox (the created channels)

Reopen:
  C.33 / E.4.DPF revision, or a vault schema change (regenerate the scaffold)
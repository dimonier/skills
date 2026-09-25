---
id: PV.Migration
title: "Vault migration: retiring legacy directories and entity kinds into the DEC card / artifacts"
status: seed
keywords: [migration, migrate, retirement, schema-change, legacy, DEC, TRK, artifacts, Q, RISK, CON, reports, state, constraints]
dependencies:
  builds_on:
    - A.7
    - C.32.ADR
    - E.4.DPF
  coordinates_with:
    - F.14
    - F.18
---

## PV.Migration - Vault migration: retiring legacy directories and entity kinds

> **Trigger:** When an existing vault predates a schema revision and still carries retired directories or entity kinds — the open-question/risk/contradiction directories, or `reports/`/`state/` — with live files or empty placeholders.
> **Skill dependencies:**
>   → none

---

### PV.Migration:1 - Problem frame

Use this pattern to migrate a pre-revision vault: retire the superseded directories
and entity kinds (the open-question/risk/contradiction directories, and
`reports/`/`state/`) and fold every live entity into the surviving kinds — the
decision card and `artifacts/` — without losing content or breaking the references
that point at the retired IDs. The target schema is defined by `PV.VaultSchema`; the
card-filling rules come from `PV.StateUpdate`.

### PV.Migration:2 - Problem

After the schema revision, an older vault still carries retired directories and
possibly live entities inside them (an open question/risk/contradiction, a report, a
constraint). Leaving them means two schemas coexist and the registry of open
positions fragments. Deleting them blindly means content loss. Rewriting IDs by hand
means dangling references. The migration must move content, re-point references, then
remove the directories — in that order.

### PV.Migration:3 - Forces

| Force | Settlement |
|---|---|
| Content preservation vs clean removal | Migrate every live entity before deleting its directory. |
| Reference integrity vs hand-edit | The retired ID is recorded in the new card's frontmatter `references`; incoming references are re-pointed to the new card ID. |
| Kind vs status | A retired open-position kind maps to a **status** on the decision card (`open`/`proposed`), not to a new entity kind. |
| Analysis vs projection (`reports/`) | A self-contained analysis moves to `artifacts/`; a derived projection (agenda/summary) folds into DEC/TRK as a signal. |
| Constraint vs card (`state/`) | A constraint is a state position → a DEC card, not a track and not a standalone `constraints` file. |
| Machine integrity vs trust | Re-run `vault.py check` after migration; the retired ID prefixes must stop resolving. |

### PV.Migration:4 - Solution

1. **Inventory.** List the three retired open-position directories (open questions,
   risks, contradictions); for each, list its entities (`Get-ChildItem` / `ls`).
2. **Map each live entity to a decision card by its old kind:**
   - **Open question** → decision card, `status: open`; the question goes into "Context and question".
   - **Risk** → decision card, `status: open` (or `proposed` if a response is already formed); the risk goes into "Revisit conditions"/"Consequences".
   - **Contradiction** → decision card, `status: open`; the two incompatible positions go into "Considered options", the tension into "Context and question".
   - If the content is already reflected in an existing card/track → fold it in as a signal, do not create a duplicate.
3. **Allocate and carry over.** New ID only via `vault.py next-id DEC`. Preserve
   status: an old `accepted` stays `accepted`; an old open position → `open` (or
   `proposed`). Record the retired ID in the new card's frontmatter `references`
   (historical trace).
4. **Re-point incoming references.** `grep` the vault for the old ID prefix; update
   each reference to the new decision-card ID.
5. **Remove the retired directories** — only once empty. If a directory still holds a
   file after steps 2–4, migrate that file first; do not delete a non-empty directory.
6. **Verify.** `vault.py check` passes (old prefixes no longer resolve), and the
   migrated cards pass the decision export check (no internal IDs in the body).

**Retiring `reports/` and `state/` (schema removes these two directories).**

When the adopted schema drops `reports/` (derived summaries) and `state/`
(`constraints.md`) in favour of `artifacts/` and the single DEC card:

1. **Map `state/constraints.md` → DEC card(s).** A regulatory/architectural
   constraint is a bounded state position with a long-lived consequence, so each
   constraint becomes one DEC card (`status: open`/`proposed`; `decision_type`: `adr`
   for architectural, `scope`/`process` for regulatory). Record `state/constraints.md`
   in the new card's frontmatter `sources` (historical trace). Not a track — a
   constraint is state, not an operational line.
2. **Map each `reports/*` file by content type:**
   - **Self-contained analysis with lasting value** (a write-up readable standalone) →
     move to `artifacts/YYYY-MM-DD-slug.md` (retitle the slug to its substance); if a
     track clearly matches, bind it and add a "Next moves" item, otherwise flag
     "unbound".
   - **Derived projection** (agenda, status snapshot — a re-statement of the state
     already in the vault) → no standalone entity; fold still-relevant signals into
     the matching DEC ("Related entities"/"External signals") or TRK ("Next moves"),
     then drop the report file.
3. **Re-point, remove, verify.** Re-point incoming references to the new DEC/artifact;
   remove `reports/` and `state/` only when empty; run `vault.py check`.

### PV.Migration:5 - Archetypal Grounding

**Show.** In this repository the retired directories (open questions, risks,
contradictions, `reports/`, `state/`) were empty (only placeholders) at the time of
the revision, so migration was "inventory → nothing to move → remove the
directories"; the pattern exists for the non-empty case.

### PV.Migration:6 - Bias-Annotation

The temptation is to delete the directories first and notice the content loss after;
the symmetric temptation is to keep retired directories "just in case", so the old
schema never fully retires. Counterweights: inventory first, migrate each entity,
re-point references, then delete.

### PV.Migration:7 - Conformance Checklist

| ID | Requirement |
|---|---|
| CC-MG.1 | Every live entity is migrated into its surviving kind (a DEC card or `artifacts/`) before its directory is removed. |
| CC-MG.2 | The retired ID is recorded in the new card's frontmatter `references`. |
| CC-MG.3 | Incoming references to a retired ID are re-pointed to the new card ID. |
| CC-MG.4 | A retired directory is removed only when empty. |
| CC-MG.5 | `vault.py check` passes after migration. |
| CC-MG.6 | A `state/` constraint becomes a DEC card; a `reports/` analysis moves to `artifacts/`, a projection is folded as a signal. |

### PV.Migration:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
|---|---|
| Delete directories first, then discover the content | Inventory + migrate before delete. |
| A contradiction split into two cards | One card; the two positions under "Considered options". |
| Retired directories left "just in case" | Remove when empty; migration is the retire step. |
| A report moved to `artifacts/` but left as a projection | Move analyses; fold projections into DEC/TRK as signals. |
| Reusing the old ID prefix for new cards | New ID only via `vault.py next-id DEC`. |

### PV.Migration:9 - Consequences

A single-kind schema with no retired residue. Migration is cheap when the retired
directories are empty (the common case); when live entities exist, each migrates to
its surviving kind (decision card or artifact) and references must be re-pointed or
they dangle.

### PV.Migration:10 - Rationale

`A.7` — the retired kinds are positions on one entity's status axis, not
separate kinds; migration collapses them onto the status field. `E.4.DPF:4`
(proportionality) — retire, do not keep parallel directories. `F.14` (anti ID
explosion) — no new prefixes; the old prefix is retired, not reused. `C.32.ADR` —
the decision card carries the migrated content in ADR sections.

### PV.Migration:11 - SoTA-Echoing

| Source line | Adopt/adapt/reject | Locus in this card | Boundary |
|---|---|---|---|
| FPF `A.7` (kind vs status) | Adopt | Migrate kinds → status, not new kinds | Reopen on `A.7` revision |
| FPF `E.4.DPF` (proportionality) | Adopt | Retire directories when empty | Reopen on `E.4.DPF` revision |
| FPF `F.14` (anti ID explosion) | Adopt | Retired prefix not reused | Reopen on `F.14` revision |

Best-known line: migrate-then-retire, reference-preserving. Rejected rival: "delete
first, recover later" — rejected as lossy.

### PV.Migration:12 - Relations

The dependency graph (FPF content edges + Specialization) has its single authored home
in this card's frontmatter `dependencies`; it is not repeated here. The readable
intra-LPF map is generated in `references/relations.md`.

### PV.Migration:End
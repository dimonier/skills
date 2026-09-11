# Project Vault — Relation Records

> **Generated projection — do not hand-edit the graph block.** The graph has a single
> authored home: each card's frontmatter `dependencies` — FPF content edges
> (`builds_on`/`coordinates_with`) and local Specialization (`specializes`, authored on
> the **child** side; the inverse `specialized_by` is derived here and is never
> authored). This file is the derived, readable map of the **intra-LPF Specialization
> graph only**; FPF content edges are **not** repeated here — they live only in the
> frontmatter. Rebuilt by `scripts/build_relations.py` (`E.4.PFR:3.2`: derived views
> cite one assertion and are never maintained independently). Run
> `python scripts/build_relations.py` after changing frontmatter; `--check` fails on
> drift. Cards' `:12 Relations` carry only a pointer to the frontmatter.
>
> **Relation functions (canon).** Edges use only `E.4.PFR:3.3` functions:
> `builds_on`, `coordinates_with`, `specializes`/`specialized_by`. `governs` /
> `applies-to` / `→ *all cards*` is **not** an edge — it is a content fact written as
> prose, not a graph row.
>
> **Direction.** `specializes` = child (narrower) → parent.

## Source / edition citation

- **Skill:** `project-vault` (LPF — Local Practices Framework).
- **Authoring scenario (EntryRoute):** outcome (a) "revise framework";
  axes — `FPF-grounded` (relies on FPF Core) and `language-from-scratch`
  (the skill directory is the access-facing carrier; the edition lives in this
  skill's own `references/*.md`; no externally published projection document exists).
- **Field / field boundary:** the practice "managing project state in a
  markdown-vault": capturing state from sources (transcripts/dialogues), binding
  external research, track lifecycle, work records, artifact creation, report
  creation, schema and ID integrity.
- **Dependency chain (unidirectional, `E.5.3`):** `project-vault` → `FPF` → (nothing).
  `create-agent-skill` — a skill dependency on carrier mechanics, not an FPF pattern.
  `pdf2md` — a skill dependency of `PV.Inbox` (PDF conversion).
- **Readiness:** all 10 patterns are `status: seed`; readiness mode `source-faithful`
  (not `case-validated`), declared collectively in `SKILL.md`.
- **Publication-form checks:** `E.11.PFP` `PFM1`–`PFM12` are N/A — there is no
  reader-facing publication form for this skill carrier.

## Refresh triggers (G.11)

Revisit this skill (reopen → refresh per `G.11`) on any of the following:

1. **Source change** (`E.4.PFR`, G.11 `EditionPinChange`): a revision of the FPF Core
   patterns that the cards' frontmatter `dependencies` build on (`A.7`, `A.10`,
   `A.15.1`, `A.15.2`, `C.2.1`, `C.32.ADR`, `C.33`, `E.9`, `F.14`, `F.18`,
   `G.11`).
2. **Vault schema change** (the field boundary of the practice): a new entity kind,
   a new directory, a new carrier or search tool → edit `PV.VaultSchema` and the
   affected neighbouring bodies.
3. **PLAS change** (`E.4.PFAD` revision): the `pattern-language-as-agent-skill` skill
   changes conformance requirements (E.8 sections, EntryRoute, carrier mechanics).
4. **Local-use telemetry** (G.11 `TelemetryDelta`): the owner reports that the skill
   misfired, is ambiguous, or a weak model (`create-agent-skill` weak-model gate)
   does not follow the steps without invention — including a substantive
   method-feedback signal emitted from WRK closure (see `PV.WorkRecord` W.4).
5. **Carrier-mechanics change** (`create-agent-skill`): atomicity, layout, or
   single-surface agreements change.

Minimal revisit route: `E.4.DPF.DA` D1–D12 + `E.21` for the affected bodies
+ `scripts/check_frontmatter.py` + `scripts/build_relations.py --check` — without a
full "tsar-track" rebuild.

## Relation graph

<!-- BEGIN GENERATED GRAPH -->
### Specialization — authored (`specializes`, child → parent)

| From (child) | Relation | To (parent) |
|---|---|---|

### Specialization — derived inverse (`specialized_by`, parent → child)

| From (parent) | Relation | To (child) |
|---|---|---|
<!-- END GENERATED GRAPH -->

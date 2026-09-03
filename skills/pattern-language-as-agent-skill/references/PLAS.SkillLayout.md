---
id: PLAS.SkillLayout
title: "Canonical directory layout of a DPF-skill (single surface, no monolith, no reader-facing form)"
status: seed
keywords: [skill-layout, directory, references, single-surface, access-facing-carrier, edition, monolith]
dependencies:
  builds_on:
    - E.4.DPF
    - C.33
    - C.2.1
    - E.24.PUB
  coordinates_with:
    - E.4.DPF.DA
    - E.11.PFP
---

## PLAS.SkillLayout - Canonical directory layout of a DPF-skill (single surface, no monolith, no reader-facing form)

> **Trigger:** When scaffolding a new DPF-skill directory, reorganizing an existing one, or deciding whether the skill is the single source of truth versus a projection of a separate document.
> **Governing FPF patterns:**
>   → E.4.DPF
>   → C.33
>   → C.2.1
>   → E.24.PUB
> **Skill dependencies:**
>   → create-agent-skill (skill anatomy)

---

### PLAS.SkillLayout:1 - Problem frame

Use this pattern to lay out the files of a DPF-skill and to fix its single-surface
decision: the skill directory is the access-facing carrier that bears the edition,
the edition is the `C.2.1` episteme constituted by the pattern bodies in
`references/`, and there is no separate monolith or reader-facing publication form.

### PLAS.SkillLayout:2 - Problem

A DPF-skill can drift into failures: a mega-`SKILL.md` that carries all subject
knowledge (reproducing a bloated monolith), an `assets/` "canonical" file that
reintroduces a second source, calling the skill "the edition" and collapsing the
carrier into the edition (`C.33`), mirroring an external standard without pinning
it, dropping a source attachment during conversion, or treating version history
as authoring residue. The layout must keep the
dispatcher routing-only, the pattern bodies atomic, the edition/carrier
distinction explicit, and the one dependency graph consistent across its three
views.

### PLAS.SkillLayout:3 - Forces

| Force | Settlement |
|---|---|
| Progressive disclosure vs one file | `SKILL.md` = routing; `references/` = on-demand bodies. |
| Atomicity vs mega-skill | One pattern per reference file (split by action, not domain). |
| Optional machinery vs bloat | `assets/`, `scripts/`, `templates/`, `evals/` appear only when used. |
| Edition vs carrier | The skill directory is the access-facing carrier; the edition is the `C.2.1` episteme recoverable from `references/`, not from the carrier. |
| Single surface vs reader-facing form | No reader-facing `E.11.PFP` form while there is no cold reader; if a reader emerges, it is a separate `E.24.PUB` projection. |
| External source vs projection | An external published standard is canonical; the skill is its derived representation, with a pin record + edition-tied refresh. |
| Three graph views vs drift | Frontmatter (machine), `:12` (human), `relations.md` (canonical map) — one graph, agreed direction. |

### PLAS.SkillLayout:4 - Solution

```
<skill>/
├── SKILL.md          # dispatcher: frontmatter (name + description) + routing table
├── references/       # canonical E.8 pattern bodies, one per file
│   ├── INDEX.md      # one logical pattern index
│   └── relations.md  # canonical home: source/edition citation + dependency graph
├── assets/           # OPTIONAL: heavy resources only; NEVER a monolith
├── scripts/          # OPTIONAL: validators/helpers
├── templates/        # OPTIONAL: output skeletons
└── evals/            # OPTIONAL: dev-only test fixtures (skill-creator); not loaded at runtime
```

1. **`SKILL.md`** is routing-only (see `PLAS.Dispatcher`).
2. **`references/`** holds the canonical bodies (see `PLAS.PatternBody`), plus
   `INDEX.md` (one logical index) and `relations.md`. Both `SKILL.md` and
   `references/*.md` are edited directly; there is no monolith and no "generated →
   do not edit" derived copy. `relations.md` is the **canonical home** for the
   source/edition/dependency citation and the dependency graph; `SKILL.md` carries
   only a one-line pointer to it.
3. **`assets/`** is for logos/data/sample payloads, never a framework monolith.
   **Preserve source attachments:** an artifact the source embeds or references
   (dashboard JSON, sample payload, schema) must be saved under `assets/`, not
   dropped during conversion. Do not discard an example just because it has no
   immediate place in a body.
4. **`scripts/`** and **`templates/`** are added only when there is a real
   validation or output task; empty scaffolding is not added for completeness
   (`E.4.DPF:4`).
5. **Keep edition and carrier distinct.** Say "the skill directory is the
   access-facing `U.PresentationCarrier` bearing the edition", not "the skill is
   the edition" (`E.4.DPF` Plain vocabulary, `C.33`). The `C.2.1` identity is
   recoverable from `references/` and stays independent of the carrier.
6. **No reader-facing publication form** while there is no cold reader. If a
   reader emerges, a separate `E.24.PUB`/`E.11.PFP` projection is assembled from
   `references/` — never a second editable source.
7. **Keep authoring residue out.** DRR text, decision notes, and quality proofs are
   maintainer evidence, not skill content (`E.4.DPF:4` step 11); store them outside
   the skill. A `CHANGELOG.md` is **not** authoring residue — it is version history
   and is allowed inside by `create-agent-skill` — but a DPF-skill does **not
   require** one: version history lives in the project vault (WRK/DEC/digest) and
   the repo's git history.
8. **`evals/` is dev-only.** Test fixtures and `evals/evals.json` (per
   `skill-creator`) live inside the skill directory but are never loaded at runtime
   and are not part of the edition; the runtime surface stays `SKILL.md` +
   `references/`.
9. **External-standard representation.** When the DPF mirrors an already-published
   external standard (`representation-of-external-standard` from `PLAS.EntryRoute`),
   the external document is canonical and the skill is a derived projection — never
   "the standard". Declare a pin record (URL + edition + status) in `relations.md`
   and tie refresh to the source's edition, not to internal signals. `SKILL.md`
   states "this skill is a representation, not the standard" in one line.
10. **One dependency graph, three views.** The graph lives in three places with a
    division of labor: frontmatter `dependencies` (machine-readable), section
    `:12 Relations` (human-readable), `relations.md` (the global map — canonical).
    All three must agree; change one → change all three. `relations.md` fixes the
    edge direction (e.g. `builds_on` as "dependent → what it builds on") with
    unambiguous column headers.

### PLAS.SkillLayout:5 - Archetypal Grounding

**Show.** `pattern-language-as-agent-skill/` itself follows this layout: `SKILL.md` +
`references/` with `INDEX.md`, `relations.md`, and eight `PLAS.*` bodies; no
`assets/` monolith. The skill directory is the access-facing carrier; the `C.2.1`
edition is recoverable from `references/`.

### PLAS.SkillLayout:6 - Bias-Annotation

The layout is easy to over-fit by adding empty `scripts/`/`templates/`/`assets/`
"for completeness" — premature apparatus that looks mature but adds maintenance
surface without a task. Symmetrically, "the skill is the edition" is a tempting
collapse: the access-facing carrier becomes the edition and the `C.2.1` identity is
lost (`C.33`). The proportionality rule (`E.4.DPF:4`) and the explicit
edition/carrier wording are the two counterweights.

### PLAS.SkillLayout:7 - Conformance Checklist

| ID | Requirement |
|---|---|
| CC-SL.1 | `SKILL.md` contains no subject knowledge beyond the routing table and context. |
| CC-SL.2 | Each pattern body lives in its own `references/*.md`. |
| CC-SL.3 | No `assets/` monolith or generated publication form is present. |
| CC-SL.4 | `INDEX.md` lists every pattern body exactly once. |
| CC-SL.5 | Edition and carrier stay distinct: the skill is the access-facing carrier bearing the edition, not the edition itself. |
| CC-SL.6 | Authoring residue (DRR, review notes, draft, ledger) is outside the skill; version history (CHANGELOG) is not authoring residue and is optional. |
| CC-SL.7 | `relations.md` is the canonical home for the source/edition/dependency citation and the dependency graph; its column headers fix the edge direction. |
| CC-SL.8 | An external-standard DPF declares a pin record (URL + edition + status) and edition-tied refresh; it is stated to be a representation, not the standard. |
| CC-SL.9 | A source attachment the standard references (dashboard JSON, sample payload, schema) is preserved under `assets/`, not dropped. |

### PLAS.SkillLayout:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
|---|---|
| Mega-SKILL.md with all patterns inline | Move bodies to `references/`; keep SKILL.md routing-only. |
| `assets/` monolith as "source of truth" | Remove it; author directly in `references/`. |
| Empty `scripts/`/`templates/` for completeness | Add only when a real task needs them. |
| "Skill is the edition" collapses carrier into edition | Say "access-facing carrier bearing the edition"; keep `C.2.1` identity recoverable from `references/`. |
| Generated publication form drifted from references | Remove the form, or mark it a separate `E.24.PUB` projection with its own check. |
| Source/edition citation duplicated across files | Keep it once in `relations.md`; other files point to it. |
| External standard without a pin record | Pin URL + edition + status in `relations.md`; refresh on edition. |
| CHANGELOG treated as authoring residue | Classify as version history; not required, but allowed inside. |
| Source attachment dropped during conversion | Preserve it under `assets/`; do not drop referenced examples. |

### PLAS.SkillLayout:9 - Consequences

Keeping `SKILL.md` routing-only and bodies atomic gives one-hop loading and no
monolith. The single-surface decision removes drift and duplication but costs the
reader-facing form: while there is no cold reader, no `E.11.PFP` volume exists; if
a reader emerges, it becomes a separate `E.24.PUB` projection, never a second
editable source.

### PLAS.SkillLayout:10 - Rationale

The split mirrors `create-agent-skill` anatomy (`SKILL.md` + `references/`), with
`assets/`/`scripts/`/`templates/` optional so no second source or monolith sneaks
back in. FPF keeps edition and carrier distinct (`E.4.DPF`, `C.33`, `C.2.1`): a
skill-pack is an access-facing carrier that must return to an authoritative
subject, so classifying the skill directory as that carrier — with the `C.2.1`
edition recoverable from `references/` — satisfies the `D5` layering requirement
without a monolith. Proportionality follows `E.4.DPF`: more files do not make a
framework more mature.

### PLAS.SkillLayout:11 - SoTA-Echoing

| Source line | Adopt/adapt/reject | Locus in this card | Boundary |
|---|---|---|---|
| `create-agent-skill` "Anatomy of a Skill" (`SKILL.md` + `references/` + `scripts/` + `templates/` + `assets/`) | Adopt | Becomes the canonical directory tree; `assets/` is resource-only | Reopen when skill-anatomy guidance changes |
| `create-agent-skill` progressive disclosure (metadata → body → resources) | Adopt | `SKILL.md` routing-only; bodies load on demand from `references/` | Reopen when the loading model changes |
| FPF `E.4.DPF`/`C.33` edition-carrier separation | Adopt | Skill directory = access-facing carrier; edition = `C.2.1` episteme in `references/` | Reopen on FPF `E.4.DPF`/`C.33` revision |

Best-known line: single-surface skill anatomy. Rejected rival: "monolith + derived skill" (the
`assets/` "source of truth" pattern) — dropped to avoid fork/drift.

### PLAS.SkillLayout:12 - Relations

- **Builds on:** `E.4.DPF` (carrier assembly, edition/carrier/form separation), `C.33` (carrier vs. overread), `C.2.1` (edition identity), `E.24.PUB` (publication is a separate later relation).
- **Coordinates with:** `E.4.DPF.DA` (package adequacy, D5 layering), `E.11.PFP` (reader-facing form out of scope while no cold reader), `create-agent-skill` (anatomy).
- **Specialized by:** `PLAS.Dispatcher`, `PLAS.PatternBody`, `PLAS.SelfSufficient`.

### PLAS.SkillLayout:End

---
id: PLAS.Naming
title: "Naming the skill and PatternIDs"
status: seed
keywords: [naming, skill-name, patternid, F.18, F.14]
dependencies:
  builds_on:
    - F.18
    - F.14
    - E.4.DPF
  coordinates_with:
    - E.10
---

## PLAS.Naming - Naming the skill and PatternIDs

> **Trigger:** When naming a new DPF-skill or assigning PatternIDs before public references accumulate.
> **Skill dependencies:**
>   → create-agent-skill (skill naming)

---

### PLAS.Naming:1 - Problem frame

Use this pattern to name a DPF-skill and its PatternIDs so the name is a handle for
use, not a hidden ontology, and so addresses stay stable while publication order
changes.

### PLAS.Naming:2 - Problem

Names drift into two failures: a tempting head word smuggles in a wrong prototype
(`F.18`), or a PatternID is treated as position/title and renumbered when the body
moves (`E.4.DPF:4.0.3`). A local skill name still requires the full
governed-value-first candidate comparison — visible and conformance-checkable, not
skipped or filled in after the fact.

### PLAS.Naming:3 - Forces

| Force | Settlement |
|---|---|
| Local vs durable | A local skill name still runs the full F.18 candidate comparison; "local" bounds only the reference scope, not the process. |
| Tech vs Plain | `name` (kebab-case) is the Tech label; folder/AGENTS wording is the Plain label. |
| Stability vs reorder | PatternID stays while the pattern's answer continues; position is shown separately. |

### PLAS.Naming:4 - Solution

1. **Skill name.** Recover the governed value first, then run a candidate
   comparison (≥2 head families, each rejected candidate with its own rationale)
   exactly as `F.18:4` prescribes, and record it *before* the choice — never after
   the fact. Follow `create-agent-skill`: kebab-case, atomic, WHAT+WHEN in the
   `description`.
2. **Plain label.** Use `<Name>` as the human-facing folder/AGENTS wording.
3. **DPF code + local locator.** Declare a short stable DPF code and a local
   locator per pattern; together they form the `PatternID` (`<Code>.<Name>`).
4. **Keep address stable.** Keep a PatternID while the recurring problem, working
   move, useful result, and stop/return still describe the same answer. Splits,
   merges, replacements get new IDs; old references get a migration note or stop.
5. **Reopen condition.** Name the smallest change (scope or carrier) that reopens
   the naming settlement.

### PLAS.Naming:5 - Archetypal Grounding

**Show.** `pattern-language-as-agent-skill`: governed value = "authoring a DPF or
LPF whose sole carrier is an agent skill — the pattern language lives in the skill";
candidates `pattern-language-as-agent-skill`, `pattern-language-as-skill`,
`framework-as-skill`, `dpf-as-skill`; chose the first as neutral and FPF-accurate
("pattern language" names the edition, "agent skill" names the carrier), rejected
`framework-as-skill` for reintroducing the carrier-as-edition conflation and
`dpf-as-skill` as a cryptic acronym; reopen if the scope ever grows beyond the
skill carrier.

### PLAS.Naming:6 - Bias-Annotation

The author decides the name first and justifies it second: the candidate
comparison is fabricated after the fact (a "rejected" list invented to support a
foregone choice), or a name is chosen before the governed value is recovered. The
bias is toward a foregone name dressed up as a comparison.

### PLAS.Naming:7 - Conformance Checklist

| ID | Requirement |
|---|---|
| CC-NM.1 | Governed value recovered before the name. |
| CC-NM.2 | ≥2 head families compared; rejected candidates recorded. |
| CC-NM.3 | PatternIDs stable; position shown separately; migration note on split/merge. |
| CC-NM.4 | The candidate comparison is recorded before the choice, with a per-candidate rejection rationale — no post-hoc "rejected" list. |

### PLAS.Naming:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
|---|---|
| PatternID used as position or renumbered on move | Keep address stable; show `§` separately. |
| Name smuggles ontology (e.g. `reviewer` as a role) | Recover the governed value; split before naming. |
| Candidate comparison fabricated after the choice | Run the comparison first and record it before choosing; each rejected candidate gets its own rationale. |

### PLAS.Naming:9 - Consequences

A stable PatternID survives reordering, but a rename later costs a migration note
for every old reference, and the candidate comparison must be redone if the scope
or carrier changes. The comparison, once required to be visible and checkable,
cannot be skipped silently.

### PLAS.Naming:10 - Rationale

`F.18` requires recovering the governed value before the name and running a
visible, checkable candidate comparison. `E.4.DPF:4.0.3` keeps addresses stable
while publication order changes, so a PatternID is an address, not a position.

### PLAS.Naming:11 - SoTA-Echoing

| Source line | Adopt/adapt/reject | Locus in this card | Boundary |
|---|---|---|---|
| FPF `F.18` local-first naming | Adopt | Skill name = local name; PatternID = stable address, not position | Reopen on `F.18` revision |
| FPF `F.14` anti-explosion | Adopt | No proliferation of alias IDs; one ID per pattern | Reopen on `F.14` revision |
| `create-agent-skill` atomic naming (kebab-case, WHAT+WHEN) | Adopt | Applied to the skill name; the `PLAS.*` PatternID prefix is local | Reopen when skill-naming guidance changes |

Best-known line: local-first naming. Rejected rival: tech-cryptonym / acronym head (e.g.
`dpf-as-skill`) — dropped in favor of a Plain head.

### PLAS.Naming:12 - Relations

The dependency graph (FPF content edges + Specialization) has its single authored home
in this card's frontmatter `dependencies`; it is not repeated here. The readable
intra-LPF map is generated in `references/relations.md`.

### PLAS.Naming:End

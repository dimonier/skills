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
> **Governing FPF patterns:**
>   → F.18
>   → F.14
>   → E.4.DPF
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
moves (`E.4.DPF:4.0.3`). Local skill names do not need the full `NameCard`/UTS-row
apparatus — but they still need a governed-value-first candidate comparison.

### PLAS.Naming:3 - Forces

| Force | Settlement |
|---|---|
| Local vs durable | A local skill name uses the F.18 discipline lightly; no `NameCard`, no `F.17` row (`F.18:0`, `F.14`). |
| Tech vs Plain | `name` (kebab-case) is the Tech label; folder/AGENTS wording is the Plain label. |
| Stability vs reorder | PatternID stays while the pattern's answer continues; position is shown separately. |

### PLAS.Naming:4 - Solution

1. **Skill name.** Recover the governed value first, then run a candidate
   comparison (≥2 head families, rejected candidates, rationale) exactly as
   `F.18:4` prescribes — but stop before minting a `NameCard`/`F.17` row (local
   name). Follow `create-agent-skill`: kebab-case, atomic, WHAT+WHEN in the
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

The author over-invests in naming: a full `NameCard`/`F.17` row for a local name
that does not need it (`F.14` explosion), or a name chosen before the governed
value is recovered. The bias is toward durable apparatus for a name that will
never carry cross-framework reference.

### PLAS.Naming:7 - Conformance Checklist

| ID | Requirement |
|---|---|
| CC-NM.1 | Governed value recovered before the name. |
| CC-NM.2 | ≥2 head families compared; rejected candidates recorded. |
| CC-NM.3 | No `NameCard`/`F.17` row minted for a local name. |
| CC-NM.4 | PatternIDs stable; position shown separately; migration note on split/merge. |

### PLAS.Naming:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
|---|---|
| Full NameCard/UTS row for a local skill name | Stop at the candidate comparison (`F.14`). |
| PatternID used as position or renumbered on move | Keep address stable; show `§` separately. |
| Name smuggles ontology (e.g. `reviewer` as a role) | Recover the governed value; split before naming. |

### PLAS.Naming:9 - Consequences

A stable PatternID survives reordering, but a rename later costs a migration note
for every old reference, and the candidate comparison must be redone if the scope
or carrier changes. A local name that stops before the durable apparatus avoids
the `F.14` naming explosion but gives up cross-framework addressability.

### PLAS.Naming:10 - Rationale

`F.18` requires recovering the governed value before the name; local skill names
stop before the durable `NameCard`/`F.17` apparatus (`F.14`). `E.4.DPF:4.0.3` keeps
addresses stable while publication order changes, so a PatternID is an address,
not a position.

### PLAS.Naming:11 - SoTA-Echoing

| Source line | Adopt/adapt/reject | Locus in this card | Boundary |
|---|---|---|---|
| FPF `F.18` local-first naming | Adopt | Skill name = local name; PatternID = stable address, not position | Reopen on `F.18` revision |
| FPF `F.14` anti-explosion | Adopt | No proliferation of alias IDs; one ID per pattern | Reopen on `F.14` revision |
| `create-agent-skill` atomic naming (kebab-case, WHAT+WHEN) | Adopt | Applied to the skill name; the `PLAS.*` PatternID prefix is local | Reopen when skill-naming guidance changes |

Best-known line: local-first naming. Rejected rival: tech-cryptonym / acronym head (e.g.
`dpf-as-skill`) — dropped in favor of a Plain head.

### PLAS.Naming:12 - Relations

- **Builds on:** `F.18` (local-first naming), `F.14` (anti-explosion), `E.4.DPF:4.0.3` (PatternID stability).
- **Coordinates with:** `E.10` (kind discipline before naming), `create-agent-skill` (skill naming).

### PLAS.Naming:End

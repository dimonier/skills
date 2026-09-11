---
id: PLAS.GoverningCues
title: "Recording FPF dependencies in card frontmatter (single home)"
status: seed
keywords: [governing-cues, dependency, FPF, unidirectional]
dependencies:
  builds_on:
    - E.5.3
    - E.4.PFR
  coordinates_with:
    - E.4.DPF
  specializes:
    - PLAS.PatternBody
---

## PLAS.GoverningCues - Recording FPF dependencies in card frontmatter (single home)

> **Trigger:** When recording a card's FPF dependencies in frontmatter or auditing the dependency chain of a DPF-skill.

---

### PLAS.GoverningCues:1 - Problem frame

Use this pattern to record each DPF-skill pattern's link to the FPF Core pattern that
governs it — as frontmatter `dependencies`, the single home — so the agent can navigate
up the dependency chain without guessing and without duplicating a cue list in the body.

### PLAS.GoverningCues:2 - Problem

A DPF-skill whose cards do not cite their governing FPF patterns is ungrounded: the
agent cannot tell which Core pattern constrains the local move, and the framework
reads as free-floating domain advice. Cues must name the current FPF patterns (the
right pattern IDs), not stale or guessed names — and must be recorded **once**, in the
frontmatter `dependencies`. A second cue list in the body (or in `:12`) drifts from the
frontmatter and is the same duplication removed elsewhere.

### PLAS.GoverningCues:3 - Forces

| Force | Settlement |
|---|---|
| Precision vs drift | Cue names an exact FPF pattern ID (e.g. `E.4.DPF`), not a vague name. |
| Single home vs repeated cue lists | FPF dependencies are recorded once in frontmatter `dependencies`; the body carries no cue block. |
| One-way dependency | `pattern-language-as-agent-skill → FPF → (nothing)`; no upward edit, no cycle (`E.5.3`). |
| Skill vs FPF | `create-agent-skill` is a skill dependency, not an FPF governing pattern; keep the two kinds distinct. |

### PLAS.GoverningCues:4 - Solution

1. **Record FPF dependencies in the frontmatter `dependencies`** — `builds_on` /
   `coordinates_with` with the exact PatternID of each FPF pattern that defines or
   constrains the card's move. This is the **single home**: do **not** repeat a
   `Governing FPF patterns` cue block in the body. No filesystem path leaves this
   skill. The exception is a self-sufficient body (`PLAS.SelfSufficient`): it carries
   no FPF edges by design and states its self-sufficiency boundary in prose.
2. **Use the exact current pattern IDs** (e.g. `E.4.DPF`, `E.8`, `E.4.PFR`,
   `G.11`), not aliases; verify the pattern ID is current in FPF Core.
3. **Keep the chain unidirectional** (`E.5.3`): a DPF-skill depends on FPF and
   on other DPFs/LPFs only through explicit dependencies; it never edits FPF.
4. **Record every edge in frontmatter, using FPF relation functions.** Relation
   functions come from FPF `E.4.PFR:3.3`; never invent one. The single authored home
   of the graph is the card frontmatter `dependencies`: `builds_on`, `coordinates_with`
   (FPF codes); `specializes` (local/DPF codes — the parents this card narrows).
   Specialization is authored on the **child** side only: the child is the local card
   and always exists, whereas the parent may be an external DPF/FPF pattern. The
   inverse `specialized_by` is **derived**, never authored (a rare "external child
   specializes our card" case is stated in prose, not as a key). This matches
   `E.4.PFR:3.3` ("child narrows parent") and `E.4.PFR:3.2` (one assertion, derived
   view). `:12 Relations` carries only a **one-line pointer** to the frontmatter and
   does **not** repeat the edges (no duplication). `relations.md` is a **generated**
   projection (`scripts/build_relations.py`), never hand-edited. "Governs /
   applies-to / *all cards*" is **not** an edge — it is a content fact written as prose
   (`E.4.PFR:3.3` closes the relation-function list; no governor/owner relation
   exists).
5. **List skill dependencies separately** in a `Skill dependencies` block (e.g.
   `create-agent-skill`) — they are not FPF governing patterns and are not cited
   as FPF pattern references.

### PLAS.GoverningCues:5 - Archetypal Grounding

**Show.** `PLAS.SkillLayout` records `builds_on` (`E.4.DPF`, `C.33`, `C.2.1`,
`E.24.PUB`) and `coordinates_with` (`E.4.DPF.DA`, `E.11.PFP`) in its frontmatter — each a
current FPF pattern ID — and its body header carries only the Trigger and the
`create-agent-skill` skill dependency, with no cue block. `relations.md` is generated
from those frontmatter edges.

### PLAS.GoverningCues:6 - Bias-Annotation

Recording FPF dependencies drifts into citing whatever FPF pattern sounds relevant
rather than the pattern that actually constrains the move, and the author is tempted
to guess IDs from memory. A second failure is re-listing the cues in the body "for
readability" and letting that list drift from the frontmatter. The honest record names
the governing pattern verified against current FPF Core, once, in the frontmatter.

### PLAS.GoverningCues:7 - Conformance Checklist

| ID | Requirement |
|---|---|
| CC-GC.1 | Every FPF-grounded card records its FPF dependencies in the frontmatter `dependencies` (single home); no card repeats a `Governing FPF patterns` cue block in its body. A self-sufficient body states its boundary in prose. |
| CC-GC.2 | Every cue names a current FPF pattern ID. |
| CC-GC.3 | The graph has one authored home — frontmatter `dependencies`: `builds_on`/`coordinates_with` (FPF codes) and `specializes` (local codes, authored on the **child** side); `specialized_by` is derived, never authored; relation functions come only from `E.4.PFR:3.3`; `:12` is a pointer and `relations.md` is generated. |
| CC-GC.4 | Skill dependencies are not mislabeled as FPF patterns. |

### PLAS.GoverningCues:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
|---|---|
| Cards with no governing cues | Record the FPF patterns that govern each move in the frontmatter `dependencies`. |
| Broken/guessed pattern IDs | Verify the ID against FPF Core. |
| DPF-skill edits FPF | Block it; chain is one-way (`E.5.3`). |
| `Governing FPF patterns` cue block repeated in the body | Remove it; the cues live only in the frontmatter `dependencies`. |
| Invented relation function (`governs`/`applies-to`, `→ *all cards*`) | Use only `E.4.PFR:3.3` functions; a "lives in all cards" fact is content prose, not a graph edge. |
| Edges duplicated in frontmatter and `:12` | Keep them only in frontmatter; `:12` is a pointer; generate `relations.md`. |

### PLAS.GoverningCues:9 - Consequences

Correct records make the dependency chain navigable and auditable, but they
must be re-verified against current FPF Core on every FPF edition change, or they
silently stale. A one-way chain prevents cycles but also forbids upstreaming
improvements except through FPF's own amendment path. Recording them once (frontmatter)
removes the body-block drift at the cost of the body no longer listing its own
governing patterns inline — the reader opens the frontmatter.

### PLAS.GoverningCues:10 - Rationale

The chain must be unidirectional (`E.5.3`) so a DPF-skill never edits FPF; skill
dependencies (`create-agent-skill`) are kept separate because they are carrier
mechanics, not governing patterns. Exact IDs (not names) keep the constraint
verifiable.

### PLAS.GoverningCues:11 - SoTA-Echoing

| Source line | Adopt/adapt/reject | Locus in this card | Boundary |
|---|---|---|---|
| FPF `E.5.3` unidirectional dependency | Adopt | `DPF-skill → FPF → (nothing)`; the skill never edits FPF | Reopen on `E.5.3` revision |
| FPF `E.4.PFR` relation records | Adopt | `builds_on`/`coordinates_with` + `relations.md` | Reopen on `E.4.PFR` revision |
| `create-agent-skill` "Four Layers" (rules / skills / MCP / memory) | Adapt | FPF dependencies (frontmatter) vs `create-agent-skill` (a `Skill dependencies` block) stay distinct | Reopen when the layer model changes |

Best-known line: FPF unidirectional cues. Rejected rival: "cite any FPF pattern that sounds
relevant" (alias/guessed IDs) — dropped.

### PLAS.GoverningCues:12 - Relations

The dependency graph (FPF content edges + Specialization) has its single authored home
in this card's frontmatter `dependencies`; it is not repeated here. The readable
intra-LPF map is generated in `references/relations.md`.

### PLAS.GoverningCues:End

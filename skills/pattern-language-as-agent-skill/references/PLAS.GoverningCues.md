---
id: PLAS.GoverningCues
title: "Governing-pattern cues to FPF and the dependency chain"
status: seed
keywords: [governing-cues, dependency, FPF, unidirectional]
dependencies:
  builds_on:
    - E.5.3
    - E.4.PFR
  coordinates_with:
    - E.4.DPF
---

## PLAS.GoverningCues - Governing-pattern cues to FPF and the dependency chain

> **Trigger:** When filling the `Governing FPF patterns` block of a pattern body or auditing the dependency chain of a DPF-skill.
> **Governing FPF patterns:**
>   → E.5.3
>   → E.4.PFR
>   → E.4.DPF

---

### PLAS.GoverningCues:1 - Problem frame

Use this pattern to wire each DPF-skill pattern back to the FPF Core pattern that
governs it, so the agent can navigate up the dependency chain without guessing.

### PLAS.GoverningCues:2 - Problem

A DPF-skill whose cards do not cite their governing FPF patterns is ungrounded: the
agent cannot tell which Core pattern constrains the local move, and the framework
reads as free-floating domain advice. Citations must name the current FPF
patterns (the right pattern IDs), not stale or guessed names.

### PLAS.GoverningCues:3 - Forces

| Force | Settlement |
|---|---|
| Precision vs drift | Cue names an exact FPF pattern ID (e.g. `E.4.DPF`), not a vague name. |
| One-way dependency | `pattern-language-as-agent-skill → FPF → (nothing)`; no upward edit, no cycle (`E.5.3`). |
| Skill vs FPF | `create-agent-skill` is a skill dependency, not an FPF governing pattern; keep the two kinds distinct. |

### PLAS.GoverningCues:4 - Solution

1. **Fill the `Governing FPF patterns` block** of every FPF-grounded body with the
   name of each FPF pattern (its PatternID) that defines or constrains the card's
   move. No filesystem path leaves this skill. The exception is a self-sufficient
   body (`PLAS.SelfSufficient`): it carries no FPF cues by design and declares its
   self-sufficiency boundary statement instead.
2. **Use the exact current pattern IDs** (e.g. `E.4.DPF`, `E.8`, `E.4.PFR`,
   `G.11`), not aliases; verify the pattern ID is current in FPF Core.
3. **Keep the chain unidirectional** (`E.5.3`): a DPF-skill depends on FPF and
   on other DPFs/LPFs only through explicit dependencies; it never edits FPF.
4. **Record dependencies by namespace.** FPF-dependency edges go in the card
   frontmatter `dependencies` (`builds_on`, `coordinates_with`) — FPF codes only.
   LPF-specialization edges go in `specialized_by` — local (`PLAS.*`/`PV.*`) codes
   only. `relations.md` holds the intra-LPF graph (specialization + applies-to),
   never FPF edges. The three views must agree in membership and direction.
5. **List skill dependencies separately** in a `Skill dependencies` block (e.g.
   `create-agent-skill`) — they are not FPF governing patterns and are not cited
   as FPF pattern references.

### PLAS.GoverningCues:5 - Archetypal Grounding

**Show.** `PLAS.SkillLayout` cites `E.4.DPF`, `C.33`, `C.2.1`, `E.24.PUB`,
`E.4.DPF.DA`, `E.11.PFP` — each a current FPF pattern ID. The
frontmatter records `builds_on`/`coordinates_with`; `create-agent-skill` appears in
the `Skill dependencies` block, not as an FPF reference.

### PLAS.GoverningCues:6 - Bias-Annotation

Cue-filling drifts into citing whatever FPF pattern sounds relevant rather than
the pattern that actually constrains the move, and the author is tempted to guess
IDs from memory. The honest cue names the governing pattern verified against
current FPF Core, not a remembered alias.

### PLAS.GoverningCues:7 - Conformance Checklist

| ID | Requirement |
|---|---|
| CC-GC.1 | Every FPF-grounded body carries a filled `Governing FPF patterns` block; a self-sufficient body declares its boundary statement instead. |
| CC-GC.2 | Every cue names a current FPF pattern ID. |
| CC-GC.3 | FPF-dependency (`builds_on`/`coordinates_with`) is recorded separately from LPF-specialization (`specialized_by`); `relations.md` holds intra-LPF edges only. |
| CC-GC.4 | Skill dependencies are not mislabeled as FPF patterns. |

### PLAS.GoverningCues:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
|---|---|
| Cards with no governing cues | Name the FPF patterns that govern each move. |
| Broken/guessed pattern IDs | Verify the ID against FPF Core. |
| DPF-skill edits FPF | Block it; chain is one-way (`E.5.3`). |

### PLAS.GoverningCues:9 - Consequences

Correct governing cues make the dependency chain navigable and auditable, but they
must be re-verified against current FPF Core on every FPF edition change, or they
silently stale. A one-way chain prevents cycles but also forbids upstreaming
improvements except through FPF's own amendment path.

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
| `create-agent-skill` "Four Layers" (rules / skills / MCP / memory) | Adapt | FPF governing patterns vs `create-agent-skill` (a skill dependency) stay in separate blocks | Reopen when the layer model changes |

Best-known line: FPF unidirectional cues. Rejected rival: "cite any FPF pattern that sounds
relevant" (alias/guessed IDs) — dropped.

### PLAS.GoverningCues:12 - Relations

- **Builds on (FPF):** `E.5.3` (unidirectional dependency), `E.4.PFR` (relation records).
- **Coordinates with (FPF):** `E.4.DPF` (external dependency naming).

### PLAS.GoverningCues:End

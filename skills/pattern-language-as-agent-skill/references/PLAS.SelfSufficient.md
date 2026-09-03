---
id: PLAS.SelfSufficient
title: "Authoring a DPF-skill with no FPF dependency (self-sufficient variant)"
status: seed
keywords: [self-sufficient, no-fpf, boundary-statement, inline-semantics, readiness-mode]
dependencies:
  builds_on:
    - PLAS.EntryRoute
  coordinates_with:
    - PLAS.SkillLayout
    - PLAS.PatternBody
---

## PLAS.SelfSufficient - Authoring a DPF-skill with no FPF dependency (self-sufficient variant)

> **Trigger:** When the authoring scenario fixed in `PLAS.EntryRoute` selects `self-sufficient`: a DPF-skill that must carry no external dependency of the FPF kind.
> **Governing FPF patterns:** none by design — this variant deliberately carries no FPF governing cues (the self-sufficiency boundary).
> **Skill dependencies:**
>   → create-agent-skill (skill carrier mechanics — the governing frame in place of FPF)

---

### PLAS.SelfSufficient:1 - Problem frame

Use this pattern to author a DPF-skill whose customer explicitly requires no
external framework dependency (the `self-sufficient` scope selected in
`PLAS.EntryRoute`). It owns the elements that a normal FPF-grounded DPF gets from
FPF for free — section semantics, status semantics, and governing cues — and
keeps them from drifting.

### PLAS.SelfSufficient:2 - Problem

A self-sufficient DPF has no FPF to lean on, so the author invents by hand what FPF
would supply: an inlined rendering of the `E.8` section semantics (a bloated
12-line table), a local status ladder, a hand-rolled `builds_on`/`coordinates_with`
vocabulary, and a vague "single external source" claim. None of these is governed,
so they drift and balloon — the exact failure observed in `sfera-std-tracing`.

### PLAS.SelfSufficient:3 - Forces

| Force | Settlement |
|---|---|
| No FPF vs no drift | FPF-governing layer is dropped, not silently re-cited; a boundary statement takes its place. |
| Full section semantics vs compact | Inline only a one-line purpose per section in `SKILL.md`, never the full 12-line `E.8` table. |
| Status honesty vs over/under-claim | Reuse the two readiness modes (source-faithful vs case-validated), grounded on the declared source. |
| Carrier mechanics vs reinvention | Directory layout, description trigger, atomicity stay with `create-agent-skill`. |

### PLAS.SelfSufficient:4 - Solution

1. **Declare the self-sufficiency boundary.** A single explicit statement naming
   (a) that the skill carries no FPF dependency and no FPF governing cues, and
   (b) its one source of truth — an approved external document, or "none / from
   scratch" for a language opened independently. This statement lives in `SKILL.md`
   and replaces the governing-cue block.
2. **Inline section semantics compactly.** With no FPF to reference, state the
   canonical sections and their meaning as a one-line-per-section list in
   `SKILL.md` — not a full 12-line `E.8` table. The reader needs enough to author
   and load bodies, nothing more.
3. **Reuse the two readiness modes.** Follow `PLAS.PatternBody`'s `source-faithful`
   vs `case-validated` distinction, but ground it on the declared source rather
   than `E.21`; `status` always names its mode.
4. **Record dependencies without FPF.** `builds_on`/`coordinates_with` name only
   the skills/documents this DPF actually depends on (the source standard, other
   self-sufficient skills); no FPF pattern IDs. A `Skill dependencies` block
   (`create-agent-skill`, etc.) takes the place of the governing-cue block.
5. **Keep the carrier-independent cards.** `PLAS.SkillLayout`, `PLAS.Dispatcher`,
   and `PLAS.PatternBody` still govern the rules that do not require FPF
   (routing-only `SKILL.md`, one body per file, YAML-safe description, readiness
   modes). Only the FPF-governing layer (`PLAS.GoverningCues`, `E.8` semantics,
   `E.21` status) is replaced.

### PLAS.SelfSufficient:5 - Archetypal Grounding

**Show.** `sfera-std-tracing` (a self-sufficient regulatory skill for the Т1.ОП.08
standard) triggered this card by inlining section semantics, inventing a local
`seed`/`stable` ladder, hand-rolling `builds_on`/`coordinates_with`, and declaring a
single external source. Had this card existed, each of those four would have been
governed: one boundary statement, a compact inline list, the two readiness modes,
and dependencies naming only Т1.ОП.08 + `create-agent-skill`.

### PLAS.SelfSufficient:6 - Bias-Annotation

The strongest drift is "self-sufficient but still citing FPF by habit" — the author
keeps FPF section semantics and status words while claiming no dependency, which
reintroduces the dependency it denied. Symmetrically, "reinvent carrier mechanics"
rebuilds what `create-agent-skill` already gives. The boundary statement and the
"carrier mechanics stay in `create-agent-skill`" rule are the two counterweights.

### PLAS.SelfSufficient:7 - Conformance Checklist

| ID | Requirement |
|---|---|
| CC-SS.1 | An explicit self-sufficiency boundary statement names the single source of truth (or "none"). |
| CC-SS.2 | No FPF pattern ID appears as a governing cue; dependencies name only real dependencies. |
| CC-SS.3 | Section semantics are inlined compactly (one line per section), not as a full `E.8` table. |
| CC-SS.4 | `status` carries an explicit readiness mode (`source-faithful` vs `case-validated`). |
| CC-SS.5 | Carrier-mechanics rules (routing-only `SKILL.md`, one body per file, YAML-safe description) still hold. |

### PLAS.SelfSufficient:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
|---|---|
| Self-sufficient but still citing FPF | Drop FPF cues; declare the boundary statement instead. |
| Full 12-line `E.8` table inlined | Compact one-line-per-section list in `SKILL.md`. |
| No boundary statement (dependencies drift) | Declare the single source of truth in `SKILL.md`. |
| `status` without a mode | Name `source-faithful` vs `case-validated`. |
| Reinventing `create-agent-skill` mechanics | Delegate layout/trigger/atomicity to `create-agent-skill`. |

### PLAS.SelfSufficient:9 - Consequences

The boundary statement and compact inline semantics stop the drift and bloat that a
self-sufficient DPF otherwise accumulates, but they cost the interop FPF gives: no
governing cues, no `E.8`/`E.21` comparability, no upstream correction path. The
author re-implements only the thin slice of that machinery the skill actually needs.

### PLAS.SelfSufficient:10 - Rationale

A self-sufficient DPF is a legitimate customer constraint, but "self-sufficient"
must not mean "ungoverned": the elements FPF normally supplies still need a home.
`create-agent-skill` is the correct governing frame for carrier mechanics; the
elements it does not cover (section semantics, status semantics, source pinning)
are owned here in the lightest form that still prevents drift.

### PLAS.SelfSufficient:11 - SoTA-Echoing

| Source line | Adopt/adapt/reject | Locus in this card | Boundary |
|---|---|---|---|
| `create-agent-skill` (skill anatomy, description trigger, atomicity) | Adopt | Carrier mechanics stay in `create-agent-skill`; only the FPF-governing layer is dropped | Reopen when skill-anatomy guidance changes |
| FPF `E.8`/`E.21` (section semantics + status ladder) | Reject (for this variant) | Replaced by compact inline semantics + two readiness modes grounded on the declared source | Reopen if the DPF re-grounds on FPF |
| `sfera-std-tracing` run (G.11 misuse telemetry, finding #1) | Adopt | The drift this card prevents | Reopen on new self-sufficient misuse signals |

Best-known line: `create-agent-skill` as the carrier frame for a self-sufficient DPF. Rejected
rival: "silently re-cite FPF while claiming self-sufficiency" — dropped.

### PLAS.SelfSufficient:12 - Relations

- **Builds on:** `PLAS.EntryRoute` (routes here), `create-agent-skill` (carrier mechanics).
- **Coordinates with:** `PLAS.SkillLayout` (layout), `PLAS.PatternBody` (one body per file + readiness modes), `PLAS.Dispatcher` (routing + YAML-safe description).

### PLAS.SelfSufficient:End

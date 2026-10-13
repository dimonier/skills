---
id: PLAS.SelfSufficient
title: "Authoring a DPF-skill with no FPF dependency (self-sufficient variant)"
status: stable
keywords: [self-sufficient, no-fpf, boundary-statement, inline-semantics, readiness-mode]
dependencies:
  specializes:
    - PLAS.EntryRoute
    - PLAS.SkillLayout
---

## PLAS.SelfSufficient - Authoring a DPF-skill with no FPF dependency (self-sufficient variant)

> **Trigger:** When the authoring scenario fixed in `PLAS.EntryRoute` selects `self-sufficient`: a DPF-skill that must carry no external dependency of the FPF kind.
> **Self-sufficiency boundary:** this variant deliberately carries no FPF governing cues.
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
so they drift and balloon — the exact failure observed in a crafted skill.

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
   in place of any FPF-dependency record. When the skill represents **more than one**
   external document (a standard plus an added directive), the statement enumerates them
   under a count-neutral heading — "External sources" / «Внешние источники» — and makes no
   uniqueness or count claim, so adding a document never falsifies the text
   (`PLAS.SkillLayout:4` item 2).
2. **Inline section semantics compactly.** With no FPF to reference, state the
   canonical sections and their meaning as a one-line-per-section list in
   `SKILL.md` — not a full 12-line `E.8` table. The reader needs enough to author
   and load bodies, nothing more.
3. **Reuse the two readiness modes.** Follow `PLAS.PatternBody`'s `source-faithful`
   vs `case-validated` distinction, but ground it on the declared source rather
   than `E.21`; a self-sufficient card **carries the mode explicitly in `status`**
   (`status: source-faithful` / `status: case-validated`). This is the documented
   exception to `CC-PB.5`: the card has no FPF-governed pattern-status level
   (`Stable`/`Draft`) to name, so the mode stands in for it.
4. **Record dependencies without FPF.** `builds_on`/`coordinates_with` name only
   the skills/documents this DPF actually depends on (the source standard, other
   self-sufficient skills); no FPF pattern IDs. A `Skill dependencies` block
   (`create-agent-skill`, etc.) takes the place of FPF dependencies.
5. **Keep the carrier-independent cards.** `PLAS.SkillLayout`, `PLAS.Dispatcher`,
   and `PLAS.PatternBody` still govern the rules that do not require FPF
   (routing-only `SKILL.md`, one body per file, YAML-safe description, readiness
   modes). Only the FPF-governing layer (`PLAS.GoverningCues`, `E.8` semantics,
   `E.21` status) is replaced.
6. **Cite wording discipline as a craft rule, not as a dependency.** Dropping FPF removes
   the governing **content** layer; it does not remove the obligation to write readable,
   name-consistent prose. FPF `F.18` (naming) and `F.19` (plain technical rewriting) are
   craft rules of the carrier — the same layer as `create-agent-skill` mechanics — and are
   not governing cues. Cite them in exactly **one** declared craft-rule line placed next to
   the `Skill dependencies` block in `SKILL.md`, naming FPF as the origin and denying the
   dependency, e.g. "Wording follows the craft rules FPF `F.18`/`F.19` (naming, plain
   technical rewriting); this skill carries no FPF dependency." Cite the source as FPF, not
   as the skill that carries it (`PLAS.GoverningCues:4` item 6). No other FPF ID may appear
   in that carrier, and the line takes no frontmatter edge (item 4).
7. **Carry no authoring-infrastructure citations.** The skill is a representation
   of an external standard, not the author's project vault: no vault-internal
   entity ids (`DEC-`, `TRK-`, `WRK-`, `Q-`, `CON-`, `RISK-`), no "inbox"/"outbox"
   as a source-data notion, and no `project-vault/…`/`sources/…` path as a source
   `location` — in the card bodies, `INDEX.md`, and any generated `relations.md`.
   Cite sources only by bare filename or a reader-meaningful descriptor
   (e.g. `2026-09-21_dir-workshop1-transcript.txt`); a source `location` is a bare
   filename, never a vault path. This keeps the skill portable and self-contained.

### PLAS.SelfSufficient:5 - Archetypal Grounding

**Show.** Feedback from a crafted skill triggered this card by inlining section semantics, inventing a local
`seed`/`stable` ladder, hand-rolling `builds_on`/`coordinates_with`, and declaring a
single external source. Had this card existed, each of those four would have been
governed: one boundary statement, a compact inline list, the two readiness modes,
and dependencies naming only its reference + `create-agent-skill`. A later run supplied the
counter-case for the count claim itself: a logging skill that had declared «единственный
внешний источник» received a second normative document (a corporate directive), and the
statement became false on the day it was falsified rather than on the day it was written —
the count-neutral enumeration of item 1 is what should have been authored.

### PLAS.SelfSufficient:6 - Bias-Annotation

The strongest drift is "self-sufficient but still citing FPF by habit" — the author
keeps FPF section semantics and status words while claiming no dependency, which
reintroduces the dependency it denied. Symmetrically, "reinvent carrier mechanics"
rebuilds what `create-agent-skill` already gives. The boundary statement and the
"carrier mechanics stay in `create-agent-skill`" rule are the two counterweights. A third
drift runs the other way: over-cleaning, where the author drops wording discipline together
with the dependency and leaves structurally clean bodies whose prose still flips the
source's meaning. The declared craft-rule line (item 6) is the counterweight there — it
keeps the discipline without keeping the dependency.

### PLAS.SelfSufficient:7 - Conformance Checklist

| ID | Requirement |
|---|---|
| CC-SS.1 | An explicit self-sufficiency boundary statement names its source of truth (or "none"); where more than one external document is represented, they are enumerated under a count-neutral heading ("External sources" / «Внешние источники») with no uniqueness or count claim. |
| CC-SS.2 | No FPF pattern ID appears as a governing cue; dependencies name only real dependencies. Exception: FPF `F.18`/`F.19` are craft rules of the carrier and may be cited, but only inside the one declared craft-rule line (item 6). |
| CC-SS.3 | Section semantics are inlined compactly (one line per section), not as a full `E.8` table. |
| CC-SS.4 | `status` carries an explicit readiness mode (`source-faithful` vs `case-validated`) — the self-sufficient exception to `CC-PB.5`. |
| CC-SS.5 | Carrier-mechanics rules (routing-only `SKILL.md`, one body per file, YAML-safe description) still hold. |
| CC-SS.6 | No authoring-infrastructure citations leak into card bodies, `INDEX.md`, or `relations.md`: no vault-internal entity ids (`DEC-`/`TRK-`/`WRK-`/`Q-`/`CON-`/`RISK-`), no "inbox"/"outbox" source-data terms, no `project-vault/…`/`sources/…` source paths; sources are cited by bare filename or reader-meaningful descriptor. A combined leak grep also exempts exactly the IDs named in the declared craft-rule line (`CC-SS.2`); every other FPF ID, anywhere else, is a leak. |

### PLAS.SelfSufficient:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
|---|---|
| Self-sufficient but still citing FPF | Drop FPF cues; declare the boundary statement instead. |
| Full 12-line `E.8` table inlined | Compact one-line-per-section list in `SKILL.md`. |
| No boundary statement (dependencies drift) | Declare the single source of truth in `SKILL.md`. |
| `status` without a mode | Name `source-faithful` vs `case-validated`. |
| Reinventing `create-agent-skill` mechanics | Delegate layout/trigger/atomicity to `create-agent-skill`. |
| Vault internals (entity ids, "инбокс", vault paths) leaked into a skill body | Cite sources by bare filename/descriptor; ban ids and vault paths (`CC-SS.6`). |
| Prose left unproofed because "this skill has no FPF dependency" | Self-sufficiency drops the governing **content** layer, not wording discipline: declare the craft-rule line (item 6) and read the bodies as prose (`PLAS.QualityAndRefresh:4` item 3). |
| A "single external source" statement falsified by the next directive | Enumerate the sources under a count-neutral heading (`CC-SS.1`). |

### PLAS.SelfSufficient:9 - Consequences

The boundary statement and compact inline semantics stop the drift and bloat that a
self-sufficient DPF otherwise accumulates, but they cost the interop FPF gives: no
governing cues, no `E.8`/`E.21` comparability, no upstream correction path. The
author re-implements only the thin slice of that machinery the skill actually needs. The
craft-rule line is the single FPF citation this variant keeps: it costs one documented
allow-list in the leak grep (`CC-SS.6`) and buys prose that survives a downstream review.

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
| Feedback from a crafted skill: run (G.11 misuse telemetry, finding #1) | Adopt | The drift this card prevents | Reopen on new self-sufficient misuse signals |
| Owner ruling on wording discipline in a self-sufficient carrier (Variant A) | Adopt | Item 6: `F.18`/`F.19` are craft rules of the carrier, cited in one declared line; `CC-SS.2` exception, `CC-SS.6` grep exemption | Reopen if `F.18`/`F.19` change, or a self-sufficient carrier cannot reach FPF at all (then inline a wording checklist and attribute it in `:11`) |
| Feedback from a crafted skill: prose review of a nine-card LPF (every structural check passed, wording still flipped the source's meaning) | Adopt | Item 6 plus the anti-pattern row: self-sufficiency drops the governing layer, not the obligation to proof prose | Reopen when `PLAS.QualityAndRefresh` wording-pass (item 3) is revised |
| Feedback from a crafted skill: second normative document (a directive added to a skill that declared a single external source) | Adopt | Item 1 count-neutral enumeration, `CC-SS.1`, counter-case in `:5` | Reopen when the source surface becomes a reading obligation for the consumer |

Best-known line: `create-agent-skill` as the carrier frame for a self-sufficient DPF. Rejected
rivals: "silently re-cite FPF while claiming self-sufficiency" — dropped; and "ban wording
discipline together with the dependency" — dropped, because it produced clean-structured
bodies whose prose reversed the source.

### PLAS.SelfSufficient:12 - Relations

This card carries no FPF content edges by design (self-sufficiency boundary). Its
Specialization edges (it narrows `PLAS.EntryRoute` and `PLAS.SkillLayout`) have their
single authored home in this card's own frontmatter `dependencies.specializes`; the
readable intra-LPF map is generated in `references/relations.md`.

### PLAS.SelfSufficient:End

---
id: PLAS.PatternBody
title: "One E.8 pattern body per reference file"
status: seed
keywords: [pattern-body, E.8, atomicity, reference-file]
dependencies:
  builds_on:
    - E.8
    - E.4.DPF
  coordinates_with:
    - E.21
  specializes:
    - PLAS.SkillLayout
---

## PLAS.PatternBody - One E.8 pattern body per reference file

> **Trigger:** When drafting or revising a single pattern in `references/`.
> **Skill dependencies:**
>   → create-agent-skill (atomicity)

---

### PLAS.PatternBody:1 - Problem frame

Use this pattern to write each `references/*.md` as one `E.8`-conformant pattern
body, so the agent can load exactly the pattern the situation needs.

### PLAS.PatternBody:2 - Problem

Pattern files drift into failures: a file that bundles several patterns (a
mini-monolith), a "skeleton" with headings but no usable Solution, a body that
mirrors the source's redundancy or redraws its diagrams, or — in an FPF-grounded
card — a readiness mode declared per card in a way that conflicts with the
package-level declaration, so a body is read as more validated than the package
actually is. All break atomic loading or honesty.

### PLAS.PatternBody:3 - Forces

| Force | Settlement |
|---|---|
| Atomic load vs coverage | One pattern per file; split by action, not domain (`create-agent-skill`). |
| E.8 completeness vs skeleton | Canonical sections present with a usable Solution, not empty headings. |
| Seed honesty vs overclaim | Mark a body `seed` until it passes its declared readiness threshold. |
| Faithful vs validated | `source-faithful` readiness ≠ `case-validated` readiness; for FPF-grounded cards the mode is declared collectively in `SKILL.md` and `status` names only the level; a self-sufficient card (`PLAS.SelfSufficient`) carries the mode in `status`. |
| Source fidelity vs de-dup | Mirror the source's meaning, not its redundancy; delegate repeats by reference. |

### PLAS.PatternBody:4 - Solution

1. **One pattern per file**, named `<DPFCode>.<PatternName>.md`.
2. **Frontmatter:** `id`, `title`, `status`, `keywords`, `dependencies` — the **single
   authored home of the dependency graph**: `builds_on`, `coordinates_with` (FPF
   codes); `specializes` (local/DPF codes: the parents this card narrows — authored on
   the **child** side, the side that is always local). The inverse `specialized_by` is
   **never authored** — it is generated in `relations.md`. `status` names only the
   **level** (`seed`/`stable`); the readiness mode is declared collectively in
   `SKILL.md` (see item 6). `:12 Relations` is a one-line pointer to the frontmatter and
   does not repeat the edges (`PLAS.GoverningCues`). **Exception — compacted carrier:**
   a card of a compacted runtime projection (`PLAS.CompactedProjection`) carries **no**
   frontmatter at all; identity is the filename stem + body H1, local links are the
   `Continues`/`Reopen` slots, and the FPF link (non-self-sufficient carriers only) is a
   single `Grounding (FPF)` slot inside the `episteme` block — the canonical source owns
   the graph.
3. **E.8 canonical sections 1–13**, all mandatory, in order: Problem frame,
   Problem, Forces, Solution, Archetypal Grounding, Bias-Annotation, Conformance
   Checklist, Common Anti-Patterns and How to Avoid Them, Consequences, Rationale,
   SoTA-Echoing, Relations, and the Footer marker (`:End`). Every section carries
   content; a thin section still states its smallest grounding, boundary, or
   reduced case. **Exception — compacted carrier:** a card of a compacted runtime
   projection (`PLAS.CompactedProjection`) replaces sections 1–13 with the sanctioned
   method/procedural `episteme` block and carries no `:11 SoTA-Echoing`; the affected
   `E.8`-section CCs are N/A for that carrier.
4. **Fill Trigger** (unlike auto-decomposed FPF refs): state the situation that loads
   the card. Do **not** repeat the FPF governing cues in the body — they have their
   single home in the frontmatter `dependencies` (`PLAS.GoverningCues`). A
   `Skill dependencies` block lists non-FPF skill deps (e.g. `create-agent-skill`).
5. **Keep the body header free of duplicated links.** No `Governing FPF patterns`
   block and no `→ E.*` cue list in the body (`PLAS.GoverningCues`); no filesystem
   path leaves this skill. A self-sufficient body states its boundary in prose
   instead of a cue block (`PLAS.SelfSufficient`).
6. **Mark status honestly — level per card, readiness mode per package.** A card's
   `status` names only the **level** — `seed` (not yet evaluated) or `stable` (reaches
   the package's declared threshold). The **readiness mode** is declared **collectively
   in `SKILL.md`**, not in each card: `source-faithful` (threshold read against the
   **declared carrier form** — for a full `E.8` carrier: full structure + item binding +
   link consistency + Conformance Checklist; for a compacted carrier
   (`PLAS.CompactedProjection`): runtime allow-list + LEAK/DROP-free split + intact
   frontmatter graph + source/edition citation + complete routing; faithful to an
   approved source) vs `case-validated` (additionally heterogeneous cases, per `E.21`
   `CaseCountercaseAndTransferCoverage`). This follows FPF: a card's frontmatter
   `status` is the pattern status (`Stable`/`Draft`), while package adequacy is a
   separate aggregate result (`E.4.DPF.DA:4.5` `DPFPackageAdequacyStatus`); no
   `readiness:` key is introduced. `stable` always means "reaches the threshold for
   the package's declared mode", never another mode silently. **Exception —
   self-sufficient cards.** A card of the `self-sufficient` variant
   (`PLAS.SelfSufficient`) has no FPF-governed pattern status to name the level, so it
   carries the explicit readiness mode in `status` (`status: source-faithful` /
   `status: case-validated`) instead. The level-only + collective rule above applies to
   FPF-grounded cards; the exception is local to `PLAS.SelfSufficient`. A compacted
   carrier (`PLAS.CompactedProjection`) keeps the level-only + collective rule and only
   swaps the `source-faithful` **threshold** to its carrier profile (item 3).
7. **Non-overlapping patterns.** A DPF organizes the source's content into
   disjoint patterns; if the source repeats a fact, record it once and delegate
   from the neighbour by reference (`E.8` neighbour contribution, `E.21`
   `NeighborContributionAndUseFit`), rather than mirroring the source's redundancy.
8. **Do not reconstruct source artifacts — but do not lose them.** Do not redraw
   the source's diagrams/tables/ASCII schematics in the body; reduce them to the
   conformance-relevant rules and leave source detail in `:11 SoTA-Echoing` or
   drop it. An artifact the source embeds or references (dashboard JSON, sample
   payload, schema) is preserved under `assets/` (`PLAS.SkillLayout`), not
   dropped. An embedded draw.io `<svg>` is recovered from its `content` attribute
   and saved only as `.drawio` in `assets/` (wrapper dropped, SVG/PNG not
   regenerated) — see `PLAS.SkillLayout:4` item 3. The pattern's EntityOfConcern is
   the rule, not a rendering of the source.
9. **Keep `:11 SoTA-Echoing` per-row reopen condition.** The reopen condition is
   mandatory per row even when it looks externally homogeneous; a single condition
   may move to a footer only when homogeneity is proven. All-"Принято" is
   legitimate for a single-approved-source DPF — do not fabricate "отклонено"
   rows; the column exists for the moment adaptation/rejection actually happens
   (e.g. a new source edition).

### PLAS.PatternBody:5 - Archetypal Grounding

**Show.** `pattern-language-as-agent-skill/references/PLAS.SkillLayout.md` is one body with the
13 E.8 sections filled, its Trigger present, its FPF dependencies only in the frontmatter, and a
conformance checklist; it is marked `seed` (first-seed, not yet `E.21`-evaluated).

### PLAS.PatternBody:6 - Bias-Annotation

Heading presence is easy to mistake for maturity: a body with all 13 headings but
a thin Solution is still a seed. The checklist can be gamed by filling sections
with placeholders; the honest test is whether the Solution actually guides the
declared reader, not whether the headings are present.

### PLAS.PatternBody:7 - Conformance Checklist

| ID | Requirement |
|---|---|
| CC-PB.1 | One pattern per file; no second pattern or mini-monolith. |
| CC-PB.2 | E.8 canonical sections 1–13 present with a usable Solution. **N/A** for a compacted carrier (`PLAS.CompactedProjection`), whose body is the sanctioned `episteme` block. |
| CC-PB.3 | Trigger is filled, not TODO; FPF governing cues live only in the frontmatter `dependencies` and are **not** repeated as a body cue block. Exception: a compacted card (`PLAS.CompactedProjection`) has no frontmatter and carries the FPF link as the single `Grounding (FPF)` slot inside the `episteme` block. |
| CC-PB.4 | Status is honest (`seed` until the package's declared readiness threshold is met). |
| CC-PB.5 | For an FPF-grounded card the readiness mode (`source-faithful` vs `case-validated`) is declared collectively in `SKILL.md`, the card's `status` names only the level, and no `readiness:` frontmatter key is used. Exception: a self-sufficient card (`PLAS.SelfSufficient`) carries the explicit readiness mode in `status`. A compacted carrier (`PLAS.CompactedProjection`) keeps the collective rule and swaps only the `source-faithful` threshold to its carrier profile. |
| CC-PB.6 | Patterns are disjoint; a repeated source fact is recorded once and delegated by reference, not mirrored. |
| CC-PB.7 | Source diagrams/artifacts are reduced to conformance-relevant rules, not reconstructed in the body; source-referenced attachments are preserved in `assets/`; an embedded draw.io `<svg>` is recovered from `content` and saved as `.drawio` (wrapper dropped, SVG/PNG not regenerated). |
| CC-PB.8 | `:11 SoTA-Echoing` has a per-row reopen condition; all-"Принято" for a single-approved source is legitimate. **N/A** for a compacted carrier (`PLAS.CompactedProjection`), where provenance moves to the `relations.md` citation + `NOTICE.md`. |

### PLAS.PatternBody:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
|---|---|
| Several patterns in one file | Split into one file per pattern. |
| Skeleton with empty sections | Fill Solution + worked case, or mark `seed`. |
| TODO trigger/governing FPF patterns | Fill the Trigger; FPF dependencies live in frontmatter, not a body cue block. |
| FPF governing-cues block repeated in the body | Remove it; the cues live only in the frontmatter `dependencies`. |
| Source redundancy mirrored into two patterns | Record once; delegate by neighbour reference. |
| ASCII/diagram reconstruction of the source in the body | Reduce to rules; keep detail in `:11 SoTA-Echoing`. |
| Embedded draw.io-SVG kept as-is (unreadable wrapper) | Recover the mxfile from `content`; save only `.drawio` in `assets/`; drop the wrapper; do not regenerate SVG/PNG. |
| `status` restating the readiness mode per card (FPF-grounded card) | Declare the mode collectively in `SKILL.md`; keep card `status` to the level (`seed`/`stable`). A self-sufficient card is the exception — it carries the mode in `status`. |
| Fabricated "отклонено" rows to avoid all-"Принято" | All-"Принято" is legitimate for a single-approved source. |
| Forcing `E.8` sections into a compacted card | Use the sanctioned `episteme` block; mark the `E.8`-section CCs N/A (`PLAS.CompactedProjection`). |
| Declaring `source-faithful` unreachable for a compacted card | Read the threshold against the compacted carrier profile (item 6), not full structure. |
| Deciding an ambiguous judgment silently | Ask the owner before acting (drop source content, place an attachment, translate/rename markers). |

### PLAS.PatternBody:9 - Consequences

The full 13-section frame guarantees comparability and atomic loading, but it
costs authoring effort per body and risks "skeleton" bodies if the Solution is not
filled first. Bodies are comparable across the framework only while the numbering
and canonical titles are kept stable.

### PLAS.PatternBody:10 - Rationale

`E.8` makes sections 1–13 mandatory so patterns stay comparable and cold-readable;
the frame is a minimum authoring seed, not maturity — an `E.21` result is required
before reliance. One pattern per file preserves atomic loading and progressive
disclosure.

### PLAS.PatternBody:11 - SoTA-Echoing

| Source line | Adopt/adapt/reject | Locus in this card | Boundary |
|---|---|---|---|
| FPF `E.8` canonical body (13 sections, H-1…H-10) | Adopt | One `E.8` body per `references/` file, verbatim section order | Reopen on FPF `E.8` revision |
| `create-agent-skill` "Atomicity: split by action, not by domain" | Adapt | "One pattern per file" (action split), not "one domain per file" | Reopen when the atomicity guidance changes |
| FPF `E.21` pattern quality | Adopt | Bodies stay `seed` until the named readiness mode's threshold is met; for FPF-grounded cards the mode (`source-faithful` vs `case-validated`) is declared collectively in `SKILL.md`, a self-sufficient card carries it in `status` | Reopen on `E.21` revision |
| `agent-skill-builder` `ASB.Compaction` (compacted carrier; episteme-block bodies) | Adapt | Sections 1–13 / `:11` CCs marked N/A; no card frontmatter; FPF link as an in-block `Grounding (FPF)` slot; readiness threshold read against the compacted carrier profile (`PLAS.CompactedProjection`) | Reopen if the compaction/PLAS boundary changes |

Best-known line: `E.8` bodies with atomic skill loading. Rejected rival: "several patterns per
file" (mini-monolith body) — dropped.

### PLAS.PatternBody:12 - Relations

The dependency graph (FPF content edges + Specialization) has its single authored home
in this card's frontmatter `dependencies`; it is not repeated here. The readable
intra-LPF map is generated in `references/relations.md`.

### PLAS.PatternBody:End

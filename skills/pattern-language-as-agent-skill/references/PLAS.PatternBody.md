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
---

## PLAS.PatternBody - One E.8 pattern body per reference file

> **Trigger:** When drafting or revising a single pattern in `references/`.
> **Governing FPF patterns:**
>   → E.8
>   → E.4.DPF
>   → E.21
> **Skill dependencies:**
>   → create-agent-skill (atomicity)

---

### PLAS.PatternBody:1 - Problem frame

Use this pattern to write each `references/*.md` as one `E.8`-conformant pattern
body, so the agent can load exactly the pattern the situation needs.

### PLAS.PatternBody:2 - Problem

Pattern files drift into failures: a file that bundles several patterns (a
mini-monolith), a "skeleton" with headings but no usable Solution, a body that
mirrors the source's redundancy or redraws its diagrams, or a `status` that does
not say whether readiness means "faithful to the source" or "validated on cases".
All break atomic loading or honesty.

### PLAS.PatternBody:3 - Forces

| Force | Settlement |
|---|---|
| Atomic load vs coverage | One pattern per file; split by action, not domain (`create-agent-skill`). |
| E.8 completeness vs skeleton | Canonical sections present with a usable Solution, not empty headings. |
| Seed honesty vs overclaim | Mark a body `seed` until it passes its declared readiness threshold. |
| Faithful vs validated | `source-faithful` readiness ≠ `case-validated` readiness; `status` names which is claimed. |
| Source fidelity vs de-dup | Mirror the source's meaning, not its redundancy; delegate repeats by reference. |

### PLAS.PatternBody:4 - Solution

1. **One pattern per file**, named `<DPFCode>.<PatternName>.md`.
2. **Frontmatter:** `id`, `title`, `status`, `keywords`, `dependencies`
   (`builds_on`, `coordinates_with` — FPF codes only; `specialized_by` — local
   pattern codes, present only when this card is specialized by other local
   patterns). `status` names a **readiness mode** plus a level (see item 6).
3. **E.8 canonical sections 1–13**, all mandatory, in order: Problem frame,
   Problem, Forces, Solution, Archetypal Grounding, Bias-Annotation, Conformance
   Checklist, Common Anti-Patterns and How to Avoid Them, Consequences, Rationale,
   SoTA-Echoing, Relations, and the Footer marker (`:End`). Every section carries
   content; a thin section still states its smallest grounding, boundary, or
   reduced case.
4. **Fill Trigger + Governing FPF patterns** (unlike auto-decomposed FPF refs):
   state the situation that loads the card and the governing-pattern cues.
5. **Governing-pattern cues** name the FPF patterns — no filesystem path leaves
   this skill (`PLAS.GoverningCues`). A self-sufficient body carries none by
   design (`PLAS.SelfSufficient`).
6. **Mark status honestly — two readiness modes.** `status` names which readiness
   is claimed: `source-faithful` (threshold: full structure + item binding + link
   consistency + Conformance Checklist, faithful to an approved source) vs
   `case-validated` (threshold additionally requires heterogeneous cases, per
   `E.21` `CaseCountercaseAndTransferCoverage`). `stable` always means "reaches
   the threshold for the named mode", never the other mode silently.
7. **Non-overlapping patterns.** A DPF organizes the source's content into
   disjoint patterns; if the source repeats a fact, record it once and delegate
   from the neighbour by reference (`E.8` neighbour contribution, `E.21`
   `NeighborContributionAndUseFit`), rather than mirroring the source's redundancy.
8. **Do not reconstruct source artifacts — but do not lose them.** Do not redraw
   the source's diagrams/tables/ASCII schematics in the body; reduce them to the
   conformance-relevant rules and leave source detail in `:11 SoTA-Echoing` or
   drop it. An artifact the source embeds or references (dashboard JSON, sample
   payload, schema) is preserved under `assets/` (`PLAS.SkillLayout`), not
   dropped. The pattern's EntityOfConcern is the rule, not a rendering of the
   source.
9. **Keep `:11 SoTA-Echoing` per-row reopen condition.** The reopen condition is
   mandatory per row even when it looks externally homogeneous; a single condition
   may move to a footer only when homogeneity is proven. All-"Принято" is
   legitimate for a single-approved-source DPF — do not fabricate "отклонено"
   rows; the column exists for the moment adaptation/rejection actually happens
   (e.g. a new source edition).

### PLAS.PatternBody:5 - Archetypal Grounding

**Show.** `pattern-language-as-agent-skill/references/PLAS.SkillLayout.md` is one body with the
13 E.8 sections filled, its Trigger and Governing FPF patterns present, and a
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
| CC-PB.2 | E.8 canonical sections 1–13 present with a usable Solution. |
| CC-PB.3 | Trigger and Governing FPF patterns are filled, not TODO. |
| CC-PB.4 | Status is honest (`seed` until the declared readiness threshold is met). |
| CC-PB.5 | `status` names a readiness mode (`source-faithful` vs `case-validated`); `stable` means the named mode's threshold. |
| CC-PB.6 | Patterns are disjoint; a repeated source fact is recorded once and delegated by reference, not mirrored. |
| CC-PB.7 | Source diagrams/artifacts are reduced to conformance-relevant rules, not reconstructed in the body; source-referenced attachments are preserved in `assets/`, not dropped. |
| CC-PB.8 | `:11 SoTA-Echoing` has a per-row reopen condition; all-"Принято" for a single-approved source is legitimate. |

### PLAS.PatternBody:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
|---|---|
| Several patterns in one file | Split into one file per pattern. |
| Skeleton with empty sections | Fill Solution + worked case, or mark `seed`. |
| TODO trigger/governing FPF patterns | Fill them; they are the load contract. |
| Source redundancy mirrored into two patterns | Record once; delegate by neighbour reference. |
| ASCII/diagram reconstruction of the source in the body | Reduce to rules; keep detail in `:11 SoTA-Echoing`. |
| `status` without a readiness mode | Name `source-faithful` vs `case-validated`. |
| Fabricated "отклонено" rows to avoid all-"Принято" | All-"Принято" is legitimate for a single-approved source. |
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
| FPF `E.21` pattern quality | Adopt | Bodies stay `seed` until the named readiness mode's threshold is met; `source-faithful` vs `case-validated` are declared per body | Reopen on `E.21` revision |

Best-known line: `E.8` bodies with atomic skill loading. Rejected rival: "several patterns per
file" (mini-monolith body) — dropped.

### PLAS.PatternBody:12 - Relations

- **Builds on (FPF):** `E.8` (pattern authoring convention), `E.4.DPF` (pattern drafting step 6).
- **Coordinates with (FPF):** `E.21` (pattern quality).

### PLAS.PatternBody:End

---
id: PV.ExternalResearch
title: "External research: two-way binding of reference material to entities"
status: seed
readiness: source-faithful
keywords: [external-research, two-way-binding, signal, reference, orphan]
dependencies:
  builds_on:
    - E.4.PFR
    - C.11
    - G.11
  coordinates_with:
    - A.3.2
---

## PV.ExternalResearch - External research: two-way binding of reference material to entities

> **Trigger:** When a material is neither a meeting transcript nor dialog news — an independent study (Knowy), a narrativization, an article, a talk, a tutorial — and it must be taken into account in decision-making rather than left as an orphan.
> **Governing FPF patterns:**
>   → E.4.PFR (recording links between frameworks/entities)
>   → C.11 (fidelity and source reference)
>   → G.11 (freshness/currency of external material)
> **Skill dependencies:**
>   → none

---

### PV.ExternalResearch:1 - Problem frame

Use this pattern to file reference material so it is taken into account in
decision-making: capture the source, discover affected entities, propagate signals
into their files (two-way), and bind the source to at least one reference-bearing
entity.

### PV.ExternalResearch:2 - Problem

External material easily stays an "orphan": the source is saved, but the signals
never reach the entities, and at a future decision the material is not taken into
account. One-way capture (only in the capture, not in the entities) is incomplete
processing: a link in one direction does not make the material findable from the
entity.

### PV.ExternalResearch:3 - Forces

| Force | Settlement |
|---|---|
| Considered in decisions vs orphan | Two-way binding: a signal in the entity's file + the source in its `sources`/"Related entities". |
| One vs many entities | Bind to ≥1 reference-bearing entity (Q/RISK/CON/DEC/TRK). |
| New vs reference | Atomic entities — only if the material introduces a new decision/risk/question/contradiction. |
| Inside vs outside scope | If the material is outside the scope of all entities — explicitly "not bound — outside the project scope". |

### PV.ExternalResearch:4 - Solution

1. Save the source into `project-vault/sources/captures/`; if needed, write 2–3
   lines of summary (what the material is about) into the capture header.
2. Discover the active entities by searching the vault: `grep` for exact matches
   across the directories (`grep -l "^status: open" project-vault/open-questions/`,
   `grep -l "^status: open" project-vault/risks/`, `grep -l "^status: open"
   project-vault/contradictions/`) and `SocratiCode codebase_search` for the
   semantic search of relevant DEC/Q/RISK/CON/TRK by topic. Determine which
   entities accept references and are relevant to the topic.
3. **Propagate signals into the entity files themselves (mandatory, two-way
   binding):** for each affected entity (Q, RISK, CON, DEC — with a
   `sources`/`source` field or a "Related entities" section) append the signal to
   the file.
   - **DEC:** the signal — as an item in the body's "External signals" subsection —
     only the gist + a readable source name (e.g. "Temporal AI Cookbook"), without
     paths and without vault file names. The source — in the `sources:` frontmatter
     list. In the body only DEC-IDs and web-URLs are allowed.
   - **Q / RISK / CON:** the signal — via a `signal_YYYY-MM-DD` frontmatter field or
     a "Signal YYYY-MM-DD" note in the body with a reference to the capture.
4. **Bind the source to at least one reference-bearing entity:** add the capture to
   a track's "Related entities" → "Sources"/"Artifacts", or to the
   `sources`/`source`/"Related entities" of a fitting Q/RISK/CON/DEC (by topic).
5. Atomic entities (DEC/Q/RISK/CON) — only if the material introduces a **new**
   decision/risk/question/contradiction. Purely reference material does not require them.
6. If the material is genuinely outside the scope of all entities — explicitly write
   "not bound — outside the project scope" in the capture header (a deliberate decision, not an omission).
7. On a substantial contribution — check integrity: all created entities are formed
   and linked; no separate index is needed (discovery via `grep`/`SocratiCode`).

### PV.ExternalResearch:5 - Archetypal Grounding

**Show.** Binding an article in this project: signals in the files of open questions
and risks + the source in a DEC's `sources:`, so that at the next decision the
material is found.

### PV.ExternalResearch:6 - Bias-Annotation

The temptation is to save the source and consider the processing done: one side of
the link looks like complete processing, but the material is not findable from the
entity. Two-way binding is not cosmetics — it is the criterion of being taken into
account.

### PV.ExternalResearch:7 - Conformance Checklist

| ID | Requirement |
|---|---|
| CC-ER.1 | The signal is written into the file of every affected entity (two-way binding). |
| CC-ER.2 | The source is bound to ≥1 reference-bearing entity. |
| CC-ER.3 | In the DEC body — only the gist + a readable source name; the source only in the frontmatter. |
| CC-ER.4 | Atomic entities are created only for a new decision/risk/question/contradiction. |
| CC-ER.5 | Out of scope — an explicit "not bound — outside the project scope" note. |

### PV.ExternalResearch:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
|---|---|
| One-way capture without writing into entities | Append the signals to the entity files. |
| A capture orphan without a binding | Bind to an entity/track. |
| A capture/file path in the DEC body | Only the gist + a readable name; the path in the frontmatter. |

### PV.ExternalResearch:9 - Consequences

Two-way binding makes external material taken into account at future decisions, but
requires signals in every affected entity. Out-of-scope material is recorded
explicitly, not silently skipped.

### PV.ExternalResearch:10 - Rationale

`E.4.PFR` — links are recorded as entries, not implied; `C.11` — a signal with a
source reference; `G.11` — the currency of external material. Two-way binding is a
consequence: a signal must be findable from both sides (entity ↔ material).

### PV.ExternalResearch:11 - SoTA-Echoing

| Source line | Adopt/adapt/reject | Locus in this card | Boundary |
|---|---|---|---|
| FPF `E.4.PFR` (link recording) | Adopt | Two-way binding source ↔ entity | Reopen on `E.4.PFR` revision |
| FPF `C.11` (source reference) | Adopt | Signals with a readable source name | Reopen on `C.11` revision |
| FPF `G.11` (freshness) | Adopt | Material currency in the binding | Reopen on `G.11` revision |

Best-known line: two-way binding of external material. Rejected rival: "one-way
capture without signals in the entity" — rejected as incomplete processing.

### PV.ExternalResearch:12 - Relations

- **Builds on:** `E.4.PFR` (link recording), `C.11` (source), `G.11` (freshness).
- **Coordinates with:** `A.3.2` (method description).
- **Applies to:** `PV.StateUpdate` (new decision/risk from a signal), `PV.VaultSchema` (signals written into entities).
- **Applied by:** `PV.Inbox` (entry for external material).

### PV.ExternalResearch:End

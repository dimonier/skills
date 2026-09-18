---
id: PLAS.CompactedProjection
title: "Compacted runtime projection carrier (episteme-block bodies, no card frontmatter)"
status: seed
keywords: [compacted-projection, runtime-projection, minified, episteme, allow-list, delete-list, readiness-profile, consumer-surface]
dependencies:
  builds_on:
    - E.4.DPF
    - C.2.3
  coordinates_with:
    - A.6.3
    - E.4.PFR
  specializes:
    - PLAS.SkillLayout
    - PLAS.PatternBody
---

## PLAS.CompactedProjection - Compacted runtime projection carrier (episteme-block bodies, no card frontmatter)

> **Trigger:** When a DPF/LPF must ship as a compacted (minified) runtime projection — the `references/*.md` bodies rendered as `episteme` blocks (F3 hybrid) per `ASB.Compaction` instead of full `E.8` bodies — and you must fix what that projection keeps, drops, and how its readiness is declared without `E.8` structure.
> **Skill dependencies:**
>   → `agent-skill-builder` (`ASB.Compaction` — delete-then-render mechanics; opt-in)
>   → `episteme-compaction` (`ECPF.1`/`ECPF.2` — the notation; referenced, not restated)

---

### PLAS.CompactedProjection:1 - Problem frame

Use this pattern to author or evaluate a DPF/LPF whose carrier is a **compacted
runtime projection**: a legitimate, deliberately chosen form in which the canonical
bodies are `episteme` blocks (F3 hybrid) rather than `E.8` bodies, with the dropped
material living in the canonical source. This card fixes the projection's runtime
allow-list and delete-list, how an FPF-grounded projection keeps its link to FPF
patterns without card frontmatter, the readiness profile that replaces the
full-structure threshold, and the surface a reading consumer is actually required to
read.

### PLAS.CompactedProjection:2 - Problem

A compacted projection is legitimate (`ASB.Compaction`, opted in by the owner) but
PLAS has no carrier card for it, so it fails every readiness mode by construction:
`CC-PB.2` (no `E.8` sections 1–13), `CC-PB.8` (no `:11 SoTA-Echoing`), and the
`source-faithful` threshold ("full structure … + Conformance Checklist"). Three
secondary failures follow. First, the delete-list is applied half-way: card
frontmatter is kept "because the generator needs it" — but a runtime projection's
allow-list is method + trigger + router, so generating and checking consumer-unused
fields is itself the defect. Second, the method/procedural slot template looks like
the forbidden "single universal template" of free-form section naming. Third, an
FPF-grounded projection needs to keep its link to the governing FPF patterns, but the
usual home (frontmatter) is gone; and "who must read what" is undefined, so the
consumer is handed reconstruction-only material.

### PLAS.CompactedProjection:3 - Forces

| Force | Settlement |
|---|---|
| Legitimate carrier vs PLAS conformance | The compacted form is an approved projection; PLAS governs it per its own profile, not by forcing `E.8` structure back in. |
| Runtime allow-list vs frontmatter | A projection keeps only method + trigger + router; card frontmatter is not in it and is **not carried**. |
| FPF grounding vs no frontmatter | A non-self-sufficient (FPF-grounded) card carries its FPF link as a `Grounding (FPF)` slot **inside** the `episteme` block; a self-sufficient card carries the boundary line instead. |
| Per-card status vs package integrity | The skill is one integral package; readiness is declared **only collectively** in `SKILL.md`, never per card. |
| Readiness vs carrier form | Decouple them: the mode states fidelity to the source; the carrier form supplies the meeting threshold. |
| Compact vs reconstruct | A skill is read to apply the method, not reconstructed into prose; `ECPF.7` is not required. |
| Fixed procedural template vs free-form naming | A named method/procedural slot template is sanctioned for compacted DPF-skill cards. |
| One contract vs carrier-specific CCs | `E.8`-section CCs are marked N/A for this carrier; routing and split CCs stay mandatory. |
| Projection vs canonical source | The projection points to the canonical carrier; the dependency graph and provenance live there, not in the projection. |

### PLAS.CompactedProjection:4 - Solution

1. **Declare the carrier and its canonical source.** State in `SKILL.md` that the
   skill is a **compacted runtime projection** (a representation, not the canonical
   source) and name the canonical source — a repo DPF/LPF carrier, or a published
   external standard (see `PLAS.SkillLayout:4` item 9). The canonical source owns the
   dependency graph and provenance.
2. **Order the moves.** Move 1 (delete/externalize) **precedes** Move 2 (render
   `episteme`); the mechanics are `ASB.Compaction` (referenced, not restated). The
   projection is **opt-in**: the owner must have explicitly accepted the trade-offs
   (`ASB.Compaction:4` Gate 0).

3. **Runtime allow-list — the projection MUST keep:** `SKILL.md` (frontmatter
   `name`+`description` YAML-safe, `Depends on`, bounded context, source-of-truth
   pointer, **collective** readiness declaration, complete routing table, single-surface
   note); each card's `Trigger`, its method body as a single `episteme` block, and —
   for an FPF-grounded (non-self-sufficient) carrier only — the `Grounding (FPF)` slot
   inside that block. **No per-card frontmatter.** `INDEX.md`, `assets/`, and
   `LICENSE`/`NOTICE` are kept only when used; `relations.md` and its generator are not
   shipped (item 5).

4. **Delete-list — the projection MUST NOT keep:** the `E.8` canonical sections 1–13
   (replaced by the `episteme` slots); `:11 SoTA-Echoing`; **all card frontmatter**
   (`id`/`title`/`status`/`keywords`/`dependencies`) — identity is the filename stem +
   the body H1, cross-card links are the `Continues`/`Reopen` slots, and the graph and
   provenance live in the canonical source; `relations.md` and its generator;
   production/derivation meta-description; provenance/readiness duplication. One
   pointer to the canonical source, not an explanation.

5. **No card frontmatter; identity and links live in the body.** A compacted card is
   not the carrier's machine graph home — the canonical source is — so it carries no
   `id`/`title`/`status`/`keywords`/`dependencies` frontmatter. Instead:
   - **identity** — the filename stem (`SYSE.1.md`) plus the body H1 (`## SYSE.1 - …`);
   - **local cross-pattern links** — the `Continues` / `Reopen` slots of the block
     (already the navigation surface);
   - **FPF grounding (non-self-sufficient only)** — a `Grounding (FPF)` slot inside the
     block listing the governing patterns, e.g.

     ```episteme id="SYSE.1" context="SystemsEngineering"
     Grounding (FPF):
       builds_on: A.15.6, A.1.SCR
       coordinates_with: C.11, A.1.STM, C.30, C.32
     ```

     For a **self-sufficient** compacted carrier (no FPF dependency,
     `PLAS.SelfSufficient`) this slot is omitted; the self-sufficiency boundary
     statement in `SKILL.md` replaces it.
   This is not a "cue block repeated from frontmatter": in this carrier there **is no**
   frontmatter, so the slot is the projection's single home for the FPF link. The
   canonical source stays authoritative.

6. **Readiness is collective only.** Declare the mode once in `SKILL.md` against the
   **compacted** `source-faithful` threshold (runtime allow-list present + LEAK/DROP-free
   split + complete routing + FPF `Grounding` slot where applicable + source/edition
   citation). The skill is one integral package: there is **no** per-card `status`,
   because cards cannot diverge from the package's single declared mode. `E.8` full
   structure is the **full-carrier** threshold and does not apply here; `case-validated`
   keeps its `E.21` meaning. No new readiness mode is invented.

7. **Sanction the method/procedural slot template.** A compacted DPF-skill card is
   procedural, so it renders under an explicit **named domain template**
   (`UseThisWhen` / `Result` / `Solution` / `Stop` / `Checks` / `Antipatterns` /
   `Continues` / `Reopen`, plus the optional `Grounding (FPF)` slot) with a stated
   boundary and condition: it applies to method/procedural cards in a compacted carrier
   only. The free-form section-naming rule (`ASB.Compaction` / `ECPF.2`) is therefore
   **not** violated; the notation itself stays owned by `episteme-compaction` and is not
   restated here.

8. **Name the consumer-normative surface.** The reading agent's obligatory surface is
   `SKILL.md` (routing + collective readiness) + the `episteme` block of the card it
   routes to (the method, `Continues`/`Reopen`, and — where present — `Grounding (FPF)`).
   `INDEX.md`, the source citation, and any authoring material are reference-only;
   reverse-render (`ECPF.7`) is out of scope for a skill consumer
   (`PLAS.SkillLayout:4` item 13).

9. **A shipped graph is optional and scoped.** A compacted projection does not ship
   `relations.md` by default. If a carrier **does** opt to ship a generated graph, the
   generator contract and the empty-graph stub rule apply
   (`PLAS.SkillLayout:4` item 10).

10. **Ask the owner.** The decision to compact is the owner's (`ASB.Compaction` Gate 0);
    when the allow-list/delete-list boundary is ambiguous for a given carrier, ask
    before dropping.

### PLAS.CompactedProjection:5 - Archetypal Grounding

**Show.** `dpf-systems-engineering` (the minified SYSE DPF) is the motivating case: its
`SKILL.md` declares a minified runtime projection and names the published source, and
41 sibling cards carry an `episteme` block instead of `E.8` bodies. Under this card the
projection's target form drops the per-card frontmatter it currently carries: identity
from the filename + H1, local links from `Continues`/`Reopen`, and the FPF link moved
into a `Grounding (FPF)` slot inside each block. The case also shows the two traps this
card closes: a zero-Specialization graph shipped without a stub, and a forked
`build_relations.py` (no `--check`) — both now moot in the projection and governed
where a graph is actually shipped (`PLAS.SkillLayout`).

### PLAS.CompactedProjection:6 - Bias-Annotation

Three biases: **"smaller is better"** — compacting without the owner's explicit consent
(`ASB.Compaction` Gate 0 exists for this); **"the generator/check needs it"** — keeping
card frontmatter to feed a projection tool, which is a circular reason to retain
consumer-unused machine data (the projection's allow-list is method + trigger + router);
and **"keep the cue block, it's convenient"** — reintroducing frontmatter duplicated in
the body, when the correct move is a single `Grounding (FPF)` slot because the
projection has no frontmatter at all.

### PLAS.CompactedProjection:7 - Conformance Checklist

| ID | Requirement |
|---|---|
| CC-CPR.1 | The skill declares itself a compacted runtime projection and names its canonical source (repo carrier or external standard) in `SKILL.md`; it is a representation, not the source. |
| CC-CPR.2 | Move 1 (delete/externalize) precedes Move 2 (render); `ASB.Compaction` governs the mechanics by reference, and the owner's opt-in consent is recorded. |
| CC-CPR.3 | The runtime allow-list is present: `SKILL.md` (routing + collective readiness + source pointer), per-card `Trigger` + method `episteme` block, and the `Grounding (FPF)` slot for an FPF-grounded carrier. **No card frontmatter, no `relations.md`.** |
| CC-CPR.4 | The `E.8`-section CCs (`CC-PB.2`, `CC-PB.7`, `CC-PB.8`) are marked **N/A** for this carrier; routing and split CCs remain mandatory. |
| CC-CPR.5 | No card frontmatter is carried: identity = filename stem + body H1; local links = `Continues`/`Reopen`; FPF link = the `Grounding (FPF)` slot (non-self-sufficient) or omitted (self-sufficient). |
| CC-CPR.6 | Readiness is declared **only collectively** in `SKILL.md` against the compacted `source-faithful` threshold; there is no per-card `status` (the package is integral). |
| CC-CPR.7 | The `episteme` split is verified LEAK/DROP-free at authoring; commands/paths/IDs stay verbatim; no load-bearing imperative is flattened. |
| CC-CPR.8 | Method/procedural cards render under the sanctioned named slot template; free-form section naming is not treated as violated. |
| CC-CPR.9 | The consumer-normative surface is named; reconstruction (`ECPF.7`) is not required of the consumer. |
| CC-CPR.10 | `relations.md`/the generator are not shipped by the projection; if a carrier opts to ship a graph, the generator contract + empty-graph stub apply. |

### PLAS.CompactedProjection:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
|---|---|
| Compacting without owner consent | `ASB.Compaction` Gate 0: get explicit minimal-size confirmation + accepted trade-offs. |
| Keeping card frontmatter "because the generator needs it" | Drop it; the projection's allow-list is method + trigger + router; the graph lives in the canonical source. |
| Generating/checking `relations.md` the consumer never reads | Do not ship it in the projection; ship it only where a graph is actually used. |
| FPF-grounded card with no link to its governing patterns | Add the `Grounding (FPF)` slot inside the block. |
| Per-card `status` in a compacted carrier | Declare readiness once, collectively, in `SKILL.md`. |
| Repeating a `Governing FPF patterns` cue block *and* frontmatter | One home only: the slot (there is no frontmatter in this carrier). |
| Declaring `source-faithful` impossible because `E.8` sections are absent | Read the threshold against the compacted carrier profile, not full structure. |
| Forcing `E.8` sections back into a compacted card | Use the sanctioned procedural `episteme` slots; mark the `E.8`-section CCs N/A. |
| Imposing `ECPF.7` reverse-render on the consumer | Name the consumer surface; reconstruction is out of scope for a skill. |

### PLAS.CompactedProjection:9 - Consequences

The compacted carrier becomes conformant in its own form and genuinely runtime-only: a
legitimate projection reaches `source-faithful` without `E.8` structure, without
carrying or checking consumer-unused frontmatter, and without shipping a graph the
reading agent never uses. The cost is that per-card status and the machine graph move
entirely to the canonical source, and an FPF-grounded projection must state its
grounding as a body slot rather than frontmatter — a small, deliberate departure from
the full carrier's single-home-in-frontmatter rule.

### PLAS.CompactedProjection:10 - Rationale

The failures are the same mistake — reading a full-carrier contract onto a projection
carrier. `E.4.DPF`/`C.33` separate the carrier from the edition, so a projection form
is a legitimate carrier whose threshold must be stated per form; the projection's
allow-list (method + trigger + router) excludes card machine metadata, so generating
and checking consumer-unused frontmatter is the defect, not a virtue;
`E.4.PFR:3.2` makes the graph a single authored assertion with derived views, and in
this carrier that assertion lives in the canonical source, not in the projection. For
an FPF-grounded projection the governing link is carried as the single in-block
`Grounding (FPF)` slot; `C.2.3` supplies the F3 hybrid and `A.6.3` the render, owned by
`episteme-compaction`. Decoupling readiness from carrier form lets both forms be honest
without inventing a mode.

### PLAS.CompactedProjection:11 - SoTA-Echoing

| Source line | Adopt/adapt/reject | Locus in this card | Boundary |
|---|---|---|---|
| `agent-skill-builder` `ASB.Compaction` (Move 1 runtime allow-list = method + trigger + router; Move 2 render; opt-in Gate 0) | Adopt | Card frontmatter/`relations.md` dropped as outside the allow-list; the FPF link moves to a body slot | Reopen if the compaction/PLAS boundary changes |
| `episteme-compaction` `ECPF.1`/`ECPF.2` (F3 hybrid, `sourceClaims`/`fpfMetadata`, named template) | Adopt | Notation and split referenced, not restated; procedural template sanctioned | Reopen on an ECPF edition change |
| PLAS `DEC-0019`/`DEC-0020` (single authored graph home) + `DEC-0016` (collective readiness) | Adapt | In the projection the graph home is the canonical source; readiness is collective; FPF link is the in-block slot | Reopen on PLAS graph/status revision |
| FPF `E.4.DPF`/`C.33` (carrier vs edition) + `E.4.PFR:3.2` (one assertion, derived views) | Adopt | Projection → canonical source; per-carrier threshold | Reopen on FPF revision |
| Feedback `feedback-plas-compacted-projection.md` + `-frontmatter.md` (2026-09-13) | Adapt | The carrier card, the no-frontmatter norm, and the FPF-slot for non-self-sufficient carriers | Reopen on new compacted-carrier signals |

Best-known line: a runtime-only projection — method + trigger + router, no card
frontmatter, FPF grounding as an in-block slot. Rejected rivals: "keep frontmatter so
the generator works" (circular) and "drop the FPF link too" (ungrounds a
non-self-sufficient DPF).

### PLAS.CompactedProjection:12 - Relations

The dependency graph (FPF content edges + Specialization) has its single authored home
in this card's frontmatter `dependencies`; it is not repeated here. The readable
intra-LPF map is generated in `references/relations.md`. (This card governs the
no-frontmatter form of a *compacted* card; PLAS's own carrier is a full carrier, so
this card itself keeps its frontmatter.)

### PLAS.CompactedProjection:End

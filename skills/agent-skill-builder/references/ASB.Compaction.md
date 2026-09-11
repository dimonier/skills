---
id: ASB.Compaction
title: "Skill-material compaction: discard the unnecessary first, render the remainder as episteme blocks"
status: seed
keywords: [compaction, token-economy, episteme, sourceClaims, fpfMetadata, hybrid-f3, discard, externalize]
dependencies:
  builds_on:
    - A.6.3
    - C.2.3
  coordinates_with:
    - E.4.PFR
---

## ASB.Compaction - Skill-material compaction: discard the unnecessary first, render the remainder as episteme blocks

> **Trigger:** **Opt-in only.** When the owner has **explicitly** asked for a minimal-size skill and accepted the trade-offs below, and the materials (the `SKILL.md` body and `references/*.md`) must be compacted — discard the unnecessary and render the rest in the compact `episteme` notation. Without that explicit confirmation, do not use this pattern; use `ASB.ProgressiveDisclosure` (prose externalization) instead.
> **Governing patterns:**
>   → `AS.4` (Progressive Disclosure — the deletion/externalization half; conditional → `references/`)
>   → `A.6.3` (Epistemic Viewing — the rendering/compaction operation)
>   → `C.2.3` (Unified Formality Characteristic F — F0…F9; the hybrid F3 target)
> **Skill dependencies:**
>   → `episteme-compaction` (ECPF.1–ECPF.7 — the notation and the forward/reverse render)

---

### ASB.Compaction:1 - Problem frame

Use this pattern in two ordered moves — **delete, then compress** — when a skill's
materials must shrink to a minimal size yet stay understandable to the reading agent.
Move 1 is the ordinary progressive-disclosure externalization
(`ASB.ProgressiveDisclosure`). Move 2 renders what remains as `episteme` blocks
(F3 hybrid) with a strict two-layer split.

**Consumption model (governs what counts as a cost).** A skill is read *by an LLM
agent to understand the method*; it is **not** reconstructed into prose. Reconstruction
is therefore out of scope, and losses that only matter on reconstruction (dropping
`[bracketed]` `fpfMetadata`) are **not** costs here. What still matters is that the
agent can tell a source claim from renderer inference.

**This pattern is opt-in, not a default.** It carries real losses and ongoing costs
(see `:4`). Apply it only when the owner has explicitly confirmed the minimal-size
goal and accepted those trade-offs; otherwise the correct outcome is Move 1 alone
(plain-prose externalization). "Smaller is better" is not, by itself, a mandate to
introduce the notation.

The report `sources/2026-09-11_episteme-notation-test.md` is the grounding: it
measured both the **reading** side (decoding a block needs no preamble) and the
**writing** side (rendering with a lossless round-trip guarantee needs a full
normative preamble).

### ASB.Compaction:2 - Problem

Compacting by compression alone is the wrong order: compressing material that should
have been deleted (or externalized) spends effort on content the skill never needs.
And rendering prose into `episteme` blocks without a discipline silently corrupts it:
an inference the renderer added leaks into the source layer (**LEAK**), or a source
fact is swept into brackets and disappears on reconstruction (**DROP**). Then the
round-trip turns a hypothesis into a "source fact" or loses the fact entirely —
semantic drift. A **short** rendering preamble is worse than none: it tells the
renderer "brackets are inference" but drops the litmus test and the obligation that
facts stay outside, so the model brackets by how section names sound (measured
10/20, below no-preamble 17/20, against full-preamble 20/20).

### ASB.Compaction:3 - Forces

| Force | Settlement |
|---|---|
| Default vs opt-in | Plain-prose externalization is the default; the notation is opt-in on explicit owner consent. |
| Size vs reader cost | Minimal size trades readability and normative force; it does **not** lose the derivation layer — `[bracketed]` content stays readable (prose reconstruction is out of scope for a skill). |
| Delete vs compress | Delete/externalize first (conditional −~90%); compress only the remainder (−~38%). |
| Compression vs comprehension | The `episteme` split (`sourceClaims` vs `fpfMetadata`) must stay disciplined so the reading agent does not mistake renderer inference for a source claim; round-trip reconstruction is not a goal. |
| In-prompt discipline vs a script | The full normative preamble (~424 tokens) works (20/20); a ~60-line marker validator costs 0 tokens and catches both LEAK and DROP. |
| Prose vs slots | Hybrid F3: slots for factual claims, prose for context — not a prose monolith, not full notation. |
| Compact vs imperative | Imperative rules degrade to constatives under full notation; commands, paths, IDs never compress. |

### ASB.Compaction:4 - Solution

**Gate 0 — explicit owner consent (this pattern is opt-in, never a default).**
Do **not** compact because the author judges "smaller is better". Proceed only when
the owner has **explicitly confirmed both**:
(a) the goal is a **minimal-size** skill (token/size saving is a stated priority), and
(b) the owner **accepts the trade-offs** listed below.

Absent that confirmation, **stop at Move 1**: externalize conditional content to
`references/` as ordinary prose and render no `episteme` notation. State the
estimated saving **and** the trade-offs, and let the owner choose. When in doubt —
prose.

**Trade-offs the owner accepts (the price of minimal size).**
Consumption model: a skill is read by an LLM agent to understand the method —
**not** reconstructed into prose. That model reclassifies the costs.

*Real costs at skill-use time:*
1. **Restricted readership.** The notation needs FPF/ECPF literacy. The agent has
   it; a human does not need to read the skill, and a non-literate consumer falls
   back to F0 (`ECPF.1`). Accepted.
2. **Lost normative force.** Imperatives flatten to constatives
   (`Always use ASCII-only path names` → `dir names: ASCII-only on VPS`); the "do it"
   force must be deliberately re-expressed.
3. **Limited, corpus-dependent saving.** Commands, paths, IDs, and proper names do
   **not** compress; measured saving is ~38% on instructional prose (not ~65%).
4. **Dependency, without duplication.** Depends on the `episteme-compaction` skill;
   its instructions must **not** be restated in this skill (duplication is harmful).

*Design-time (authoring) costs — paid once, amortized at use, not runtime:*
5. **Rendering discipline + typing overhead.** The full normative preamble (or a
   validator) and per-claim classification (`ECPF.2`) are authoring-time; skill use
   is read-only and never re-renders. A design-time investment, not a runtime cost.
6. **Split correctness (LEAK/DROP).** An authoring-time discipline: a leak (inference
   outside brackets) or a drop (source fact inside brackets) makes the reading agent
   misclassify a claim. A marker validator catches both at 0 tokens.

*Explicitly NOT a cost for skills:*
- **Lossy round-trip / dropped `[fpfMetadata]`.** Reconstruction to prose is **out of
  scope** for a skill; `[bracketed]` content stays readable in the block.
  `[reasoning]`/`[evidence]` are context for the reading agent, not content that must
  survive a reconstruction. The lossless-round-trip guarantee and the
  prose-reconstruction check (`ECPF.7`) therefore do not apply.

**Move 1 — discard the unnecessary (do this first).**
1. Route conditional/rarely-needed content to `references/` (load on demand), and
   never duplicate always-loaded content (`ASB.ProgressiveDisclosure`, `ASB.Atomicity`).
2. Remove content that is neither procedure nor needed at load time. This is the
   cheapest saving and is *not* replaced by notation — the two **stack**.

**Move 2 — render the remainder as `episteme` blocks (hybrid F3).**
3. **Decide formality** (`ECPF.1`). Target: present the skill materials **as
   `episteme` blocks**. Because a skill is instructional, use **F3 hybrid** —
   `episteme` blocks carry the typed factual claims (the material of the skill),
   ordinary prose carries connective context and the load-bearing imperatives. This
   is the block presentation applied throughout the body, not a single decorative
   block.
4. **Render** (`ECPF.2`): every block is a ```` ```episteme id="…" context="…" ````
   fence. Non-bracketed content is `sourceClaims` (what the source asserts);
   `[bracketed]` sections (`[reasoning]`, `[analysis]`, `[evidence]`, `[assurance]`,
   `[aggregation]`) are `fpfMetadata` — renderer inference/derivation, kept in the
   block as context for the reading agent.
5. **Enforce the split — full normative preamble, not a short one.** The renderer's
   instructions must carry: the layer names; the **litmus test** ("asserted by the
   source, or inferred by the renderer?"); the no-fabricate rule; and the list of
   inference markers ("похоже", "видимо", "вероятно", "рекомендую", "стоит",
   "примерно", percentages) that **always** go into brackets. A short preamble that
   omits the litmus test produces more errors than no preamble at all.
6. **Keep commands, paths, IDs, and proper names verbatim** — they do not compress.
   Keep a load-bearing **imperative** as prose or as an explicit source claim; do not
   let the notation flatten it into a constative.
7. **Prefer the cheap validator when a deterministic check suffices.** A small script
   over the inference markers catches LEAK/DROP at 0 tokens; keep the full preamble
   in the renderer (loaded once per session) as the in-prompt alternative.
8. **Verify the split** (authoring-time). Run the marker validator (or check by
   eye) so there is no LEAK/DROP — the reading agent must be able to tell a source
   claim from renderer inference. Prose **reconstruction is not required** (`ECPF.7`
   is out of scope for a skill).

**Economics (measured on the report's corpus).** On an instructional chapter (1719 B
prose): 444 tokens prose → 274 tokens notation (−38.3%); the full preamble is 424
tokens and pays back after ~2.5 rendered blocks of that size (≈1 block on
medium-verbosity prose). The `episteme-compaction` description's "~65%" was **not**
reproduced on instructional text (see `Q-2026-0001`).

### ASB.Compaction:5 - Archetypal Grounding

**Show.** Take a verbose skill body mixing procedure with rationale. Move 1: the
rationale/history goes to `references/`, duplicated always-on facts are deleted.
Move 2: the factual parts (inputs, outputs, constraints, exact paths) become an
`episteme` block with `sourceClaims` outside brackets; the renderer's inference
("this step is probably the bottleneck", "recommend checking X") goes into
`[reasoning]`. The reading agent gets the procedure with exact commands intact and
the inference clearly separated, so it does not mistake the recommendation for a
method rule.

**Counter-example (from the report).** Rendering an entire instructional skill as
notation is not worth it: `Always use ASCII-only path names` degrades to
`dir names: ASCII-only on VPS`, and the commands/paths stay verbatim anyway.

**Tell (the gate).** An owner says "this skill is too big" without more. The correct
move is `ASB.ProgressiveDisclosure`: externalize to `references/` in prose and report
the saving. Only after the owner says "yes, make it minimal and I accept the
trade-offs" does `ASB.Compaction` Move 2 begin.

### ASB.Compaction:6 - Bias-Annotation

Three biases: **silent compaction** — applying the notation because the author likes
it or assumes "smaller is better", without owner consent (the gate exists for this);
**notation-for-everything** — compressing material that should simply be deleted, or
rendering a whole imperative skill as notation; and **short-preamble confidence** —
believing a one-line note ("brackets are inference") is enough, when it measured
*worse than no preamble*. Get consent, delete before compressing, and use the full
preamble (or the marker validator) at authoring time to keep the split correct.

### ASB.Compaction:7 - Conformance Checklist

| ID | Requirement |
|---|---|
| CC-CP.0 | The owner has **explicitly** confirmed (a) the minimal-size goal and (b) acceptance of the `:4` trade-offs, before any `episteme` rendering. Absent consent, only Move 1 is done. |
| CC-CP.1 | Move 1 precedes Move 2: conditional content is externalized/deleted before any compression. |
| CC-CP.2 | With consent, the skill materials are presented as `episteme` blocks (F3 hybrid: blocks for claims, prose for connective context and imperatives); without consent, plain prose. |
| CC-CP.3 | Every rendered block is an ```` ```episteme id="…" context="…" ```` fence with the `sourceClaims` / `fpfMetadata` split. |
| CC-CP.4 | The split is rendered correctly at authoring: the **full** normative preamble (layer names, litmus test, no-fabricate, marker list) or a deterministic validator — never a short preamble (it is worse than none). |
| CC-CP.5 | Commands, paths, IDs, and proper names are kept verbatim; no load-bearing imperative is flattened to a constative. |
| CC-CP.6 | The split is verified at authoring (marker validator or review) free of LEAK/DROP — the reading agent can tell source claims from inference. Prose reconstruction is **not** required (out of scope). |
| CC-CP.7 | Token-savings figures are cited only for the measured text class (not generalized from a different corpus). |
| CC-CP.8 | The owner is informed of the accepted trade-offs (restricted readership, lost normative force, limited saving, dependency) — not only of the saving. |

### ASB.Compaction:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
|---|---|
| Compaction applied without owner consent | Gate 0: get explicit minimal-size confirmation + accepted trade-offs; otherwise stop at Move 1. |
| Reporting only the saving, not the costs | State the `:4` trade-offs (restricted readership, lost imperative force, limited saving, dependency) before applying. |
| Treating the skill as reconstructable prose | Skills are read, not reconstructed — do not require a lossless round-trip or `ECPF.7`. |
| Compress before deleting | Delete/externalize first; then compress the remainder. |
| Whole skill rendered as notation | Use hybrid F3: slots for facts, prose for context and imperatives. |
| Short one-line preamble for rendering | Use the full normative preamble or a marker validator. |
| Inference left outside brackets | Apply the litmus test; move inferred content to `[reasoning]`/`[analysis]`. |
| Source facts swept into brackets | Keep `sourceClaims` non-bracketed; verify with the validator. |
| Generalizing a measured % to "skills in general" | Cite the figure only for its measured text class. |

### ASB.Compaction:9 - Consequences

This pattern is opt-in: the default for an oversized skill is `ASB.ProgressiveDisclosure`
(plain-prose externalization), which carries none of the `:4` costs. When the owner
does consent, compaction reduces token cost by ~38% on instructional prose (far more
combined with deletion/externalization), at the cost of restricted readership,
lost imperative force, kept-verbatim commands/paths, and a design-time rendering
discipline. There is **no** loss of the derivation layer: prose reconstruction is out
of scope for a skill, so `[bracketed]` context stays available to the reading agent.
The notation does **not** replace `references/`; it stacks on top of it.

### ASB.Compaction:10 - Rationale

`A.6.3` (Epistemic Viewing) governs the prose→notation render; `C.2.3` supplies the
F-levels and motivates the F3 hybrid; `AS.4` supplies the delete/externalize half.
The report supplies the empirical split: reading needs no preamble, correct rendering
needs the full one, and the split discipline keeps inference from being read as a
source claim. For a skill the consumer is an agent reading for comprehension, **not**
reconstructing prose — so the lossless-round-trip guarantee is not required, but the
split discipline still is.

### ASB.Compaction:11 - SoTA-Echoing

| Source line | Adopt/adapt/reject | Locus in this card | Boundary |
|---|---|---|---|
| Owner clarification (2026-09-11): compaction only on explicit consent; a **skill is for agent comprehension, not reconstruction**, so round-trip losses do not apply | Adopt | Gate 0 (opt-in consent) + the reclassified `:4` trade-offs | Reopen if the consent requirement or the no-reconstruction premise changes |
| Report "Отчёт: тестирование нотации episteme" (2026-09-11) | Adopt | Delete-then-compress order; full-preamble requirement at authoring; 38.3% measured; hybrid F3 | Reopen on a new experiment/additional runs (n>1) |
| `episteme-compaction` ECPF.1–ECPF.7 (FPF `A.6.3`) | Adopt | `episteme` fence, `sourceClaims`/`fpfMetadata` split, `ECPF.2` typing; `ECPF.7` not required for a skill | Reopen on an ECPF edition change |
| AS-DPF `AS.4` Progressive Disclosure | Adopt | Move-1 externalization to `references/`; the no-consent default | Reopen on `AS.4` revision |

Best-known line: delete first, then compress the remainder — **and only on owner
consent**. Rejected rivals: "compress a whole instructional skill as notation"
(imperatives flatten; commands and paths do not compress) and "compact silently
because smaller is better" (violates the opt-in gate).

### ASB.Compaction:12 - Relations

- **Builds on (DPF):** `AS.4` (progressive disclosure — Move 1).
- **Builds on (FPF):** `A.6.3` (epistemic viewing), `C.2.3` (formality).
- **Coordinates with (DPF):** `AS.3` (atomicity — where shared content goes).
- **Coordinates with (FPF):** `E.4.PFR` (record the notation edition).
- **Coordinates with (LPF):** `ASB.ProgressiveDisclosure` (the **default** when owner consent is absent).
- **Skill dependency:** `episteme-compaction` (ECPF.1–ECPF.7).
- **Reference (vault):** `DEC-0001` (the decision adopting this practice; see its revision history for the opt-in gate).

### ASB.Compaction:End

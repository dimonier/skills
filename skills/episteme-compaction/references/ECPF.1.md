---
id: ECPF.1
title: "Formality-Level Selection for Episteme Compaction"
status: source-faithful
keywords: [formality, F-level, consumer, decision-table, hybrid]
dependencies:
  builds_on:
    - C.2.3
    - A.6.3
  coordinates_with:
    - A.6.3.CR
    - A.6.3.CSC
---

# ECPF.1 — Formality-Level Selection for Episteme Compaction

> **Trigger:** When an agent or FPF author must decide the formality level of an output (F0 plain prose vs F4-F5 compact episteme notation vs F3 hybrid) before rendering, and the wrong choice would waste tokens or hide information.
>
> **Governing FPF patterns:**
>   → C.2.3 (Unified Formality Characteristic F — the F0-F9 scale)
>   → A.6.3 (Epistemic Viewing — umbrella; formality gates the viewing/compaction operation)
>   → A.6.3.CR / A.6.3.CSC (the two rendering modes: conservative fidelity vs controlled loss)
> **Type:** DPF pattern body
> **Status:** source-faithful
> **Normativity:** Normative

> **Primary EntityOfConcern:** `FormalityLevelDecision@Context`, a DPF-local record for selecting the appropriate FPF formality level for one rendering task.

### ECPF.1:1 - Problem frame

Use this pattern when an agent or FPF author must decide at what formality level to render claims — verbose F0 prose, compact F4-F5 episteme notation, or a hybrid mix — and the wrong choice would either waste tokens or hide information needed by downstream consumers.

First useful move: assess the consumer, task type, and auditability requirement against the formality selection table. Write `FormalityLevelDecision@Context`.

What goes wrong if missed: F4-F5 notation used for casual dialogue wastes tokens and alienates non-technical readers. F0 prose used for agent-to-agent diagnostics hides claim types, evidence provenance, and reasoning alternatives behind verbose sentences.

What this buys: a fast decision rule that prevents the two most common rendering-level failures.

Not this pattern when the task is already at a fixed formality level by project convention. Use `ECPF.2` directly when F4-F5 is mandated by context.

### ECPF.1:2 - Problem

FPF formality ranges from F0 (unstructured prose) to F9 (univalent foundations). For agent-generated output, the practical range is F0 (verbose prose), F3-F4 (structured, typed claims), and F4-F5 (compact, typed, executable). A concrete failure: an agent renders a diagnostic as F0 prose for another agent. The downstream agent spends 250 tokens reading "I've analyzed the crash and found that…" and must reconstruct claim types, evidence, and reasoning from sentences — a task it may perform incorrectly, silently dropping the evidence chain or collapsing five hypotheses into one. The opposite failure: an agent renders a casual status update as F4-F5 for a non-technical human, who cannot parse `Status(AuthModule): Progress: 72%` and requests a plain-English re-answer, doubling the token budget.

### ECPF.1:3 - Forces

| Force | Tension |
|---|---|
| Token economy vs human readability | F4-F5 saves ~65% tokens but requires FPF literacy to parse. |
| Auditability vs speed | F4-F5 adds typing overhead but makes every claim traceable. |
| Consumer diversity vs consistency | Output may be read by both agents (need F4-F5) and humans (need F0), forcing hybrid mode decisions. |
| Task urgency vs structural discipline | Fast answers are tempting but hide evidence and reasoning. |

### ECPF.1:4 - Solution

Apply the formality selection decision table. The primary discriminator is the consumer type and the need for audit trail.

| Consumer | Task type | Audit trail needed? | Formality | Rationale |
|---|---|---|---|---|
| AI agent | Diagnostics, architecture, review, trust assessment | Yes | F4-F5 | Agent needs typed slots, evidence, and reasoning trace. |
| AI agent | Status report, work log | Sometimes | F3-F4 | Structured but can use lighter templates. |
| FPF-literate human | Architecture decision, safety case | Yes | F4-F5 | Same audit requirements as agent consumer. |
| FPF-literate human | Status update, casual review | No | F3 (hybrid) | episteme blocks for facts, plain text for context. |
| Non-technical human | Any | No | F0 (plain) | episteme notation is incomprehensible without vocabulary. |
| Mixed consumers | Any | Yes | F4-F5 + plain summary | Full episteme block for agents, one-sentence plain summary for humans. |

**Decision rules (normative):**

1. **Default to F0** — plain language is the safe default. Upgrade only when the table above demands it.
2. **Consumer chain rule** — if any downstream consumer in a multi-hop chain needs F4-F5, render at F4-F5. A downstream agent cannot recover missing types from F0 prose.
3. **Unknown consumer rule** — if the consumer is unknown (e.g., published output), render at F3 hybrid: typed blocks for claims, plain text for context.
4. **Teaching override** — educational material stays at F0-F2 regardless of consumer. Multi-wordiness is a pedagogical feature.

**Hybrid mode rules:**

When hybrid mode (F3) is selected:

- episteme blocks carry typed claims, evidence, reasoning.
- Plain text carries context, explanation, recommendation.
- episteme blocks must be self-contained: a reader should not need the surrounding plain text to parse the episteme block.
- Plain text must not make claims that contradict or broaden the episteme block.

**Fallback table:**

| Situation | Action |
|---|---|
| Consumer is non-technical human | Switch to F0. Do not use episteme notation. |
| Educational or training material | Stay at F0-F2. Multi-wordiness is a feature. |
| Casual dialogue or chat | Stay at F0. episteme notation is inappropriate. |
| Creative or brainstorming task | Stay at F0. FPF is for facts and decisions, not narrative. |
| Consumer rejects episteme notation | Switch to F0 or F3 hybrid. Respect consumer preference. |

**Rendering mode (normative):**

Two orthogonal rendering modes; choose before rendering alongside formality level. Both are instances of the forward render `A.6.3.RT` (prose → typed slots); they differ only in the fidelity discipline applied to the rendered sourceClaims.

| Mode | When | Effect on rendering | Governing fidelity |
|---|---|---|---|
| `retelling-fidelity` | Goal is a rendering recoverable back into source-like text (retelling, faithful summary, narrative) | Preserve source sequence & granularity; **no** cross-episode generalization or added conclusions in sourceClaims; `[bracketed]` analysis optional | `A.6.3.RT` + strict `A.6.3.CR` conservatism (no claim widening, no added linkage) |
| `structural-analysis` | Goal is to expose structure, pattern, or trust (diagnostics, ADR, composition, review) | Abstraction, pattern-compression, and derived conclusions expected — but still in the correct layer (analysis → `[bracketed]`) | `A.6.3.RT` + permitted `A.6.3.CSC` controlled loss (bracketed analysis dropped on reconstruction) |

Rule: if the task asks the output to **reconstruct to something like the source**, select `retelling-fidelity`. Under this mode, pattern-compression that erases source instances and Outcome/strategy generalization are **prohibited in sourceClaims**.

### ECPF.1:5 - Archetypal Grounding

**Tell:** An agent receives a diagnostic question from another agent. The consumer is an AI agent, the task is diagnostics, and an audit trail is needed. The agent selects F4-F5 and renders a `Diag(...)` block with typed claims, ADI reasoning, and evidence references. Token usage: ~80 tokens vs ~250 for equivalent F0 prose.

**Tell:** An agent receives a casual question from a human user: "what does this error mean?" The consumer is non-technical, the task is explanation. The agent stays at F0 and writes plain English. No episteme notation is used.

**Show:** An agent writes a status report consumed by both an AI supervisor (needs F4-F5) and a human PM (needs F0). The agent renders an F4-F5 `Status(...)` block followed by a one-sentence plain summary: "Project is on track at 72% completion, ETA July 10."

### ECPF.1:6 - Bias-Annotation

The first bias is over-upgrading: an agent familiar with episteme notation applies F4-F5 to every output, including casual dialogue. The repair is the decision table — consumer type gates the upgrade.

The second bias is under-upgrading: an agent defaults to verbose F0 for agent-to-agent communication, forcing the downstream agent to spend tokens reconstructing claim types from prose. The repair is the consumer chain rule.

### ECPF.1:7 - Conformance Checklist

| Check | Passing condition |
|---|---|
| CC-ECPF1.1 Consumer identified | The intended consumer type (AI agent, FPF-literate human, non-technical human, mixed) is named. |
| CC-ECPF1.2 Task type identified | The task type (diagnostics, architecture, review, status, trust assessment, explanation, teaching, casual) is named. |
| CC-ECPF1.3 Audit requirement explicit | Whether an audit trail is needed is stated. |
| CC-ECPF1.4 Formality level justified | The selected formality level matches the decision table or a justified override is recorded. |
| CC-ECPF1.5 Fallback condition checked | The output is checked against the fallback table before emission. |
| CC-ECPF1.6 Hybrid mode self-contained | In hybrid mode, episteme blocks are self-contained and plain text does not contradict them. |

### ECPF.1:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | What fails | Repair |
|---|---|---|
| FPF-for-everything | F4-F5 used in casual dialogue, alienating human users. | Run the fallback table check before emission. |
| Default-F0 | Verbose prose used for agent-to-agent diagnostics, hiding claim structure. | Check consumer type: if consumer is an AI agent and audit trail matters, upgrade to F4-F5. |
| Mid-block switch | episteme block starts at F4-F5 but degrades to F0 mid-block. | Keep entire block at declared formality. If switch is intentional, use hybrid mode with explicit blocks. |
| Invisible hybrid | episteme claims and plain text mixed without block boundaries, making parsing ambiguous. | Use explicit block delimiters or clear separation. |
| Override without record | Formality level overridden without justification. | Record the override reason in the output or in a pre-output decision note. |

### ECPF.1:9 - Consequences

Applying ECPF.1 adds a pre-output decision step (~2-3 seconds of table lookup) but prevents the two most common rendering failures. For the downstream consumer chain: correct formality means agents receive parseable, typed claims without reconstruction overhead, and humans receive prose they can read without decoding episteme notation. For reversibility: the formality decision is per-output, not per-session — an agent can switch from F4-F5 to F0 between responses if the consumer changes. The only irreversible cost is when a consumer chain misidentifies its most demanding member, forcing a downgrade that loses information for all downstream consumers — this is prevented by the consumer chain rule.

### ECPF.1:10 - Rationale

Formality selection is the first rendering decision because it gates all subsequent rendering choices. Wrong formality at the start contaminates the entire output. The decision table makes the selection mechanical rather than intuitive, which is essential for agent-generated output where "intuition" is a source of variance and error.

### ECPF.1:11 - SoTA-Echoing

| Source line | Adopt/adapt/reject | Locus in this card | Boundary |
|---|---|---|---|
| Clark & Brennan, "Grounding in Communication," 1991 — audience design in dialogue | Adopt | :4 formality decision table (consumer type gates the level) | Reopen when a new consumer/task taxonomy changes the table |
| JSON Schema, Protocol Buffers — structured data interchange | Adopt | :4 decision table + episteme typed-slot notation as the structured carrier | Reopen when the episteme notation schema changes |

### ECPF.1:12 - Relations

- **Specializes:** `NSTD.1` (Source-Structure Intake and Narrative Purpose) — ECPF.1 adds FPF-specific formality selection rules.
- **Uses:** `C.2.3` (Unified Formality Characteristic F) — for the F0-F9 scale definition.
- **Uses:** `A.6.3` (Epistemic Viewing) — umbrella governing the viewing/compaction operation; formality gates it.
- **Uses:** `A.6.3.CR` / `A.6.3.CSC` — the two rendering modes (`retelling-fidelity` = CR-conservative; `structural-analysis` = CSC-controlled-loss).
- **Precedes:** `ECPF.2` — formality must be selected before typed slot rendering is applied.

### ECPF.1:End

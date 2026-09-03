---
id: PLAS.Dispatcher
title: "SKILL.md as routing-only dispatcher with a trigger description"
status: seed
keywords: [dispatcher, SKILL.md, description, trigger, routing]
dependencies:
  builds_on:
    - E.4.DPF
    - E.11
  coordinates_with:
    - E.11.PFP
---

## PLAS.Dispatcher - SKILL.md as routing-only dispatcher with a trigger description

> **Trigger:** When writing or revising the `SKILL.md` of a DPF-skill.
> **Governing FPF patterns:**
>   → E.4.DPF
>   → E.11
> **Skill dependencies:**
>   → create-agent-skill (description trigger, progressive disclosure)

---

### PLAS.Dispatcher:1 - Problem frame

Use this pattern to write `SKILL.md` so the agent loads the right reference in one
hop and never pulls subject knowledge out of the dispatcher itself.

### PLAS.Dispatcher:2 - Problem

Failures recur: a `SKILL.md` that teaches the domain (reproducing the monolith), a
`description` that is too short to trigger ("Runs tests") or too long to be cheap
(300+ chars), a `description` with a bare `:` that breaks the YAML frontmatter, and
a single linear navigation rule that cannot serve a multi-use-case skill. All break
progressive disclosure or load.

### PLAS.Dispatcher:3 - Forces

| Force | Settlement |
|---|---|
| Trigger precision vs token cost | `description` names WHAT + WHEN + dependency, ~100–300 chars. |
| Routing vs teaching | `SKILL.md` body is a routing table; subject knowledge lives in `references/`. |
| Human vs agent reader | `SKILL.md` addresses the agent; there is no `E.11.PFP` reader form. |
| Single chain vs multi-use | A linear navigation rule holds for one dominant chain; several use-cases get named entry paths instead. |
| Machine parse vs prose | The `description` must stay YAML-safe (block scalar or quotes on `:` + space). |

### PLAS.Dispatcher:4 - Solution

1. **Frontmatter.** `name` (kebab-case, see `PLAS.Naming`) and `description`
   stating WHAT the skill does, WHEN to use it, and key dependencies
   (`create-agent-skill` description trigger). The `description` must be
   **YAML-safe**: use a block scalar (`|`/`>`) or quotes whenever the text
   contains a `:` followed by a space or other significant YAML characters, or
   the whole frontmatter fails to parse.
2. **Bounded context.** One short line naming the domain/use frame.
3. **Routing table.** One row per pattern card: situation → `references/X.md` →
   governing cues (if any). No subject knowledge in the cells beyond enough to
   route. The table is strictly "situation → pattern" (many-to-many, primary
   entry per use-case); columns for dependencies or edition are forbidden — those
   live in `relations.md`.
4. **Navigation rule (only when a single chain dominates).** Name the first card
   to load (the entry card), then the order of the rest. A linear navigation rule
   is valid only when one dominant reading chain exists. When the skill serves
   several use-cases, drop the single linear rule and instead name each use-case's
   entry path in the routing table (e.g. "verify → all `CC-*`", "configure → flags
   + sampling + stack"), keeping the `description` promises consistent with those
   paths.
5. **Single-surface note.** State that `references/` is canonical and no monolith
   exists (`PLAS.SkillLayout`).

### PLAS.Dispatcher:5 - Archetypal Grounding

**Show.** `pattern-language-as-agent-skill/SKILL.md`: the routing table maps eight situations to eight
references, the navigation rule starts at `PLAS.EntryRoute`, and no pattern body
content appears in `SKILL.md`.

### PLAS.Dispatcher:6 - Bias-Annotation

The routing table is easy to bloat: one "helpful" sentence of subject knowledge
per row silently turns the dispatcher into a teaching surface. A `description`
tuned too short ("Runs tests") or too long (300+ chars of narrative) both break
triggering; the bias is toward either under-specifying or over-narrating the
trigger.

### PLAS.Dispatcher:7 - Conformance Checklist

| ID | Requirement |
|---|---|
| CC-DS.1 | `description` names WHAT + WHEN; it is the load trigger, not a summary. |
| CC-DS.2 | `SKILL.md` body is routing-only; no pattern-body content. |
| CC-DS.3 | Every reference in `references/` appears in the routing table or INDEX. |
| CC-DS.4 | The single-surface decision is stated. |
| CC-DS.5 | `description` is YAML-safe (block scalar or quotes when it contains `:` + space or other significant characters). |
| CC-DS.6 | The routing table is strictly "situation → pattern"; no dependency/edition columns. |
| CC-DS.7 | A linear navigation rule is used only for a single dominant chain; multi-use-case skills name one entry path per use-case, consistent with `description`. |

### PLAS.Dispatcher:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
|---|---|
| Domain knowledge in SKILL.md | Move to `references/`; keep routing. |
| "Runs tests"-style name/description | Name WHAT + WHEN + dependency. |
| SKILL.md duplicating INDEX | Routing table points to references; INDEX lists bodies once. |
| Dependency/edition columns in the routing table | Keep "situation → pattern"; move dependencies to `relations.md`. |
| One linear chain for several use-cases | Name one entry path per use-case. |
| `description` breaking YAML (bare `:` + space) | Use a block scalar (`|`/`>`) or quotes. |

### PLAS.Dispatcher:9 - Consequences

A routing-only `SKILL.md` gives cheap, one-hop loading and keeps the `description`
a cheap trigger, but it moves all subject knowledge into `references/` and
requires the routing table and `INDEX.md` to stay in sync when bodies are added or
renamed. A YAML-unsafe `description` breaks the load entirely, and a single linear
navigation rule breaks for multi-use-case skills.

### PLAS.Dispatcher:10 - Rationale

Progressive disclosure (`create-agent-skill`) requires the dispatcher to route,
not teach; `E.11`/`E.11.PFP` reader-facing content is out of scope for an
agent-only skill, so `SKILL.md` addresses the agent alone and every subject claim
lives in the body it routes to.

### PLAS.Dispatcher:11 - SoTA-Echoing

| Source line | Adopt/adapt/reject | Locus in this card | Boundary |
|---|---|---|---|
| `create-agent-skill` "Description is the trigger" (WHAT + WHEN, ~300-char ceiling) | Adopt | `SKILL.md` description states WHAT + WHEN and stays YAML-safe; the routing table is the body | Reopen when the description-trigger guidance changes |
| `create-agent-skill` progressive disclosure | Adopt | `SKILL.md` stays routing-only; bodies load on demand | Reopen when the loading model changes |
| FPF `E.11` practical entry | Adopt | Each table row maps a situation to its card + governing cues | Reopen on FPF `E.11` revision |

Best-known line: description-triggered, routing-only dispatcher. Rejected rival: "SKILL.md as
mini-monolith" (the Mega-Skill anti-pattern) — dropped.

### PLAS.Dispatcher:12 - Relations

- **Builds on:** `E.4.DPF` (dispatcher ≠ pattern bodies), `E.11` (practical entry).
- **Coordinates with:** `E.11.PFP` (out of scope: no reader-facing form), `create-agent-skill` (description trigger).

### PLAS.Dispatcher:End

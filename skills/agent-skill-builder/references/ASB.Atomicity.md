---
id: ASB.Atomicity
title: "Atomicity & decomposition: one skill, one responsibility"
status: seed
keywords: [atomicity, decomposition, mega-skill, split-by-action, chaining, coupling]
dependencies:
  builds_on:
    - E.4
    - E.5.3
---

## ASB.Atomicity - Atomicity & decomposition: one skill, one responsibility

> **Trigger:** When a draft skill is growing past ~500 lines, accumulating exceptions, or covering what is clearly more than one profession.
> **Governing patterns:**
>   → `AS.3` (Atomicity & Decomposition — the AS-DPF pattern this card specializes)
>   → `E.4` (family architecture — sibling artifacts)
>   → `E.5.3` (acyclicity across chained skills)
> **Skill dependencies:**
>   → `create-agent-skill` (atomicity)

---

### ASB.Atomicity:1 - Problem frame

Use this pattern to split a skill by **action, not by domain**, so it does one thing
well, chains with its siblings through triggering, and evolves independently.

### ASB.Atomicity:2 - Problem

A "mega-skill" covering a whole domain (models + migrations + tests + controllers +
OpenAPI + deploy) reproduces, in a different folder, exactly the bloat that drove the
team out of `AGENTS.md`. It is hard to debug (one failure mode among many), hard to
reuse (you cannot pull only the migration part), hard to improve (a change touches
many concerns), and hard to trigger accurately (the `description` must be vague to
cover everything).

### ASB.Atomicity:3 - Forces

| Force | Settlement |
|---|---|
| Coverage vs focus | One skill that "does the domain" feels easier to author; one-skill-per-action feels over-engineered until you evolve it. |
| Chaining vs coupling | Splitting must let the agent chain skills naturally; wiring calls by hand recreates coupling. |
| Reuse vs context | Smaller skills are more reusable and cheaper to load, but more skills raise triggering competition. |
| Shared facts vs deep content | Always-on facts vs on-demand depth must be routed by role, not duplicated. |

### ASB.Atomicity:4 - Solution

1. **Split by action.** An atomic skill does ONE thing well: `model`, `migration`,
   `pest-tests`, `api-resource`, `changelog`. The agent chains them naturally
   (create model → triggers migration skill → triggers test skill). Coupling is
   avoided because chaining happens *through triggering*, not through import.
2. **Apply the atomicity test.** A skill is atomic if you can describe its
   responsibility in one short clause **without "and"**. "Creates and updates
   Eloquent models and their factories and their migrations" fails; "Creates and
   updates Eloquent models" passes (one action, two tenses of it).
3. **Keep together only when it is one procedure** with shared state and fixed order
   (e.g. "deploy to staging" bundles build → test → push → smoke-check as one
   procedure). If the steps vary independently or are reusable elsewhere, split.
4. **Mega-skill repair.** Decompose into atomic siblings, give each its own
   `description` (`ASB.TriggerDesign`), and let the agent chain them. Move shared
   heavy content to `references/` (`ASB.ProgressiveDisclosure`) rather than
   duplicating it.
5. **Shared-content routing.** Disambiguate by role, not content: shared *facts*
   always-on for every task in the repo (stack, naming, paths, env) → `AGENTS.md`
   (`ASB.LayerRouting`); shared *deep content* needed only when a skill fires →
   `references/`. Routing always-on facts into a skill's `references/` recreates
   `AGENTS.md` bloat inside a skill and makes it non-portable.

### ASB.Atomicity:5 - Archetypal Grounding

**Show.** A `mega-laravel-skill` covers models, migrations, tests, controllers,
OpenAPI, deploy. Decompose into `model`, `migration`, `pest-tests`, `api-resource`,
`controller`, `openapi`, `changelog`, `deploy-staging` — each one action, each its own
trigger, each evolving independently. The original "shared framework conventions"
prose moves to `references/framework-conventions.md`, pointed at by several of the
new skills.

### ASB.Atomicity:6 - Bias-Annotation

The temptation is **coverage**: a single skill that "handles the domain" avoids the
authoring cost of splitting. The symmetric temptation is over-splitting into skills
too small to be reusable, raising triggering competition. The atomicity test and the
"one procedure with fixed order" exception are the counterweights.

### ASB.Atomicity:7 - Conformance Checklist

| ID | Requirement |
|---|---|
| CC-AT.1 | The skill's responsibility passes the one-clause-no-"and" test. |
| CC-AT.2 | `SKILL.md` body is under ~500 lines; if it exceeds, decomposition or externalization is applied. |
| CC-AT.3 | Sibling skills cooperate through `description` triggering, not through import or hard-coded calls. |
| CC-AT.4 | Shared facts are routed to `AGENTS.md`, shared deep content to `references/` — not duplicated. |

### ASB.Atomicity:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
|---|---|
| Mega-skill covering a whole domain | Decompose into atomic siblings; chain via triggering. |
| A split that requires hand-wired calls | Split along triggering, not imports. |
| Duplicating shared heavy content across siblings | Move it to `references/` and point at it. |
| Always-on facts buried in a skill's `references/` | Move them to `AGENTS.md`. |

### ASB.Atomicity:9 - Consequences

Atomic skills are easier to debug, reuse, improve, and trigger, and the agent chains
them naturally, at the cost of more artifacts and a shared-content strategy. Chaining
must stay acyclic (`E.5.3`).

### ASB.Atomicity:10 - Rationale

`AS.3` fixes the action-split and the mega-skill anti-pattern; `E.4` treats sibling
skills as family artifacts; `E.5.3` keeps chained skills acyclic. Routing shared
content by role preserves both `AGENTS.md` leanness and skill portability.

### ASB.Atomicity:11 - SoTA-Echoing

| Source line | Adopt/adapt/reject | Locus in this card | Boundary |
|---|---|---|---|
| `agent-skill-builder` "The Atomicity Principle" (split by action, not domain) | Adopt | The atomicity test and the atomic sibling examples | Reopen on a skill-payload edition change |
| AS-DPF `AS.3` Atomicity & Decomposition | Adopt | Mega-skill repair, shared-content routing | Reopen on `AS.3` revision |
| AS-DPF `AS.12` Inter-Skill Composition | Adopt (referenced) | Chaining via natural triggering | Reopen on `AS.12` revision |

Best-known line: one skill, one responsibility; chain via triggering. Rejected rival:
the mega-skill — rejected as `AGENTS.md` bloat in a different directory.

### ASB.Atomicity:12 - Relations

- **Builds on (DPF):** `AS.3` (atomicity).
- **Builds on (FPF):** `E.4` (family architecture), `E.5.3` (acyclicity).
- **Coordinates with (DPF):** `AS.4` (externalize shared content), `AS.12` (composition via chaining), `AS.7` (atomicity improves trigger accuracy).

### ASB.Atomicity:End

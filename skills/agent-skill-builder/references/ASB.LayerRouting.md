---
id: ASB.LayerRouting
title: "Layer routing: is a skill the right guidance layer (vs AGENTS.md, MCP, Memory)?"
status: seed
keywords: [layer-routing, four-layers, when-to-create, when-not, agents-md, mcp, memory, skill]
dependencies:
  builds_on:
    - E.4
    - E.5.3
    - E.11
---

## ASB.LayerRouting - Layer routing: is a skill the right guidance layer (vs AGENTS.md, MCP, Memory)?

> **Trigger:** When a "tell the agent something" need arises and it is unclear whether to write a skill, add a line to `AGENTS.md`, install an MCP server, or store a memory entry — or whether to create a skill at all.
> **Governing patterns:**
>   → `AS.1` (Layer Routing — the AS-DPF pattern this card specializes)
>   → `E.4` (family architecture)
>   → `E.5.3` (unidirectional dependency)
>   → `E.11` (first-practical entry)
> **Skill dependencies:**
>   → none

---

### ASB.LayerRouting:1 - Problem frame

Use this pattern to route one guidance need to the correct layer before authoring
anything. The skill is only one of four layers; choosing the wrong layer creates
always-loaded bloat (rules), ungoverned tools (MCP without a skill), forgotten facts
(memory treated as a skill), or skill bloat (a skill for every one-off).

### ASB.LayerRouting:2 - Problem

Without a routing test, every need becomes a skill, or every need becomes an
`AGENTS.md` line, or MCP servers are installed with no procedure to govern them, or
facts are stored as skills and forgotten. The four layers collapse and disclosure
stops being progressive.

### ASB.LayerRouting:3 - Forces

| Force | Settlement |
|---|---|
| Always-on vs on-demand | `AGENTS.md` is always in context (cheap to write, costly at scale); a skill pays context only when triggered. |
| Procedure vs fact | Skills remember *how*; memory remembers *what was decided*. Both look like "knowledge". |
| Mechanism vs governance | MCP gives hands; a skill tells the agent what to do with them. |
| One-off vs reusable | A need that occurs once does not deserve a skill; one that recurs ≥3 times usually does. |

### ASB.LayerRouting:4 - Solution

Route by the **role** of the guidance, not by its content.

| Layer | Role | Analogy | Routing test |
|---|---|---|---|
| `AGENTS.md` / rules | Project context: build commands, repo layout, naming conventions | "Where I am" | Must be in context for *every* task in this repo → here. |
| **Skill** | Reusable procedure: how to do X | **"Profession"** | Multi-step, repeated (≥3 times manually), with success and failure paths → here. |
| MCP | External system access: GitHub API, DB, browser, filesystem | "Hands" | Need to *call* an external system. No procedure → MCP alone; procedure governing the calls → MCP **and** a skill. |
| Memory | Facts and preferences: "we chose Redis", "tabs over spaces" | "Past" | A fact or past decision, not a procedure → memory. |

**Decision order (stop at the first match):**
1. Fact or preference? → Memory.
2. Always-relevant repo context? → `AGENTS.md`.
3. External access with no procedure? → MCP.
4. Reusable procedure with steps and failure paths? → Skill.
5. Both a procedure and external access? → Skill + MCP (the skill governs the MCP).

**When to create a skill** (recognize any of these):
1. **Repetitive routine** — a multi-step process you repeat often (run tests before
   deploy, generate a migration from a model). The skill guarantees no step is
   skipped.
2. **Bloated `AGENTS.md`** — the rules file has grown exceptions, footnotes,
   "VERY IMPORTANT" clauses; each exception belongs in an on-demand skill.
3. **MCP tool without governance** — an MCP server exists but the agent does not
   know *when*/*how* to use it; the skill provides the procedure.
4. **Architecture docs needed mid-task** — documentation the agent needs only when
   touching that code; package it as a skill so it loads exactly when relevant.
5. **Semantic filtering over URL collection** — dedup/merge/group-by-meaning, which
   a script cannot do (strings and timestamps only).
6. **Same workflow, different configs** — hardcode the procedure in the skill,
   store per-user configuration in each workspace.

**When NOT to create a skill:**

| Situation | Better approach |
|---|---|
| One-off request ("fix this typo") | Just answer; no skill. |
| Fact or preference ("user prefers tabs") | Memory or project rules. |
| External system access without a procedure | Just add an MCP server. |
| You have not done the task manually at least 3 times | You do not yet understand the pattern to encode. |

### ASB.LayerRouting:5 - Archetypal Grounding

**Show.** A team hand-writes migration files and gets column order wrong. Routing
test: reusable procedure (≥3 times, steps, failure paths), not a fact, not
always-on context → a `migration` skill. Separately, they want the agent to read
GitHub issues → MCP; when duplicate-issue grouping becomes a judgment procedure →
add a `triage-issues` skill that governs the MCP.

### ASB.LayerRouting:6 - Bias-Annotation

The temptation is **skills-for-everything**: creating a skill for each one-off,
which bloats the skill list, worsens trigger accuracy, and raises the security
surface. The symmetric temptation is to bury a recurring procedure in `AGENTS.md`
"just in case", bloating always-loaded context. The routing test is the
counterweight in both directions.

### ASB.LayerRouting:7 - Conformance Checklist

| ID | Requirement |
|---|---|
| CC-LR.1 | The chosen layer is named and justified against the four-layer table. |
| CC-LR.2 | A skill is created only when the reusable-procedure test (≥3 manual performances, steps, failure paths) is met. |
| CC-LR.3 | Where MCP is added, a skill is added iff a governing procedure exists; otherwise MCP alone. |
| CC-LR.4 | Facts/preferences are not encoded as skills. |

### ASB.LayerRouting:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
|---|---|
| A skill for a one-off | Route to direct action. |
| A fact stored as a skill | Store in Memory / project rules. |
| MCP installed as governance | MCP is mechanism; add a skill if a procedure governs the calls. |
| A recurring procedure left in `AGENTS.md` | Move it to a skill; keep `AGENTS.md` lean. |

### ASB.LayerRouting:9 - Consequences

Correct routing keeps always-loaded context lean and makes skills the on-demand
layer they are meant to be, but it adds a short decision step before authoring and
requires discipline to resist the "just make a skill" default.

### ASB.LayerRouting:10 - Rationale

`AS.1` routes by role not content; `E.4`/`E.5.3` keep the layers as sibling
artifacts with a unidirectional dependency; `E.11` makes the routing decision the
first practical entry. A skill is a procedure carrier (`C.33` kind discipline), not
a fact store and not a tool endpoint.

### ASB.LayerRouting:11 - SoTA-Echoing

| Source line | Adopt/adapt/reject | Locus in this card | Boundary |
|---|---|---|---|
| `agent-skill-builder` "The Four Layers" + "When to Create" + "When NOT" | Adopt | The four-layer table, decision order, create/not-create tests | Reopen on a skill-payload edition change |
| AS-DPF `AS.1` Layer Routing | Adopt | Role-based routing test and stop conditions | Reopen on `AS.1` revision |
| FPF `E.4`/`E.5.3`/`E.11` | Adopt | Family architecture, unidirectional dependency, practical entry | Reopen on FPF revision |

Best-known line: route by role, not content. Rejected rival: "a skill for every
need" — rejected as skill bloat.

### ASB.LayerRouting:12 - Relations

- **Builds on (DPF):** `AS.1` (layer routing).
- **Builds on (FPF):** `E.4` (family architecture), `E.5.3` (unidirectional dependency), `E.11` (practical entry).
- **Coordinates with (DPF):** `AS.3` (atomicity), `AS.9` (placement).
- **Specialized by (LPF):** `ASB.Atomicity` (routing decides whether to split), `ASB.Placement` (routing decides global vs project-local).

### ASB.LayerRouting:End

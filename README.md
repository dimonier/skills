# Custom Agent Skills Collection

Custom skills for AI agents that provide specialized domain knowledge and structured methodologies.

## How to Use

These skills are designed to be automatically used by an **AI agent** when a user asks for help with a task covered by one of the skills.

### Installation

1. Clone or download `skills` folder and its contents.
2. Add skills from the `skills` folder to your IDE / CLI Code tool:
   - Cursor: `~/.cursor/skills`
   - Cloude Code: `~/.claude/skills/`
   - Other IDE or AI agent: check documentation on where skills are located
3. Ask AI-agent to use the skill during task execution.

### Usage

**Example workflow:**
- User: "Help me plan my bathroom layout"
- AI: Loads `bathroom-planner/SKILL.md` srom `skills` and applies the 10-stage methodology
- AI guides user through measurements, zone planning, ergonomics, and implementation

The skills transform the AI into a specialized assistant that follows proven methodologies rather than ad-hoc responses.

## Table of Contents

- [Frameworks \& Methodologies](#frameworks--methodologies)
  - [First Principles Framework (FPF Core)](#-first-principles-framework-fpf-core)
  - [FPF Narrative Prose](#-fpf-narrative-prose)
  - [FPF Literacy \& DPF Authoring](#-fpf-literacy--dpf-authoring)
  - [Layered Framework Workspace Architecture](#-layered-framework-workspace-architecture)
- [Business Analysis \& Requirements Engineering](#business-analysis--requirements-engineering)
  - [Business Analysis \& Requirements Engineering](#-business-analysis--requirements-engineering)
- [Text Analysis \& Writing](#text-analysis--writing)
  - [Reverse-Engineering Texts](#-reverse-engineering-texts)
- [Development Tools](#development-tools)
  - [Spec Decomposer](#-spec-decomposer)
  - [Agent Skill Builder](#-agent-skill-builder)
- [Project Management](#project-management)
  - [Project Vault](#-project-vault)
- [Space Planning \& Organization](#space-planning--organization)
  - [Bathroom Planner](#-bathroom-planner)
  - [Wardrobe Planner](#-wardrobe-planner)


## Frameworks & Methodologies

Structured reasoning frameworks and domain-specific methodologies for systematic problem-solving.

### 🧠 First Principles Framework (FPF Core)

Root framework providing auditable thinking, evidence chains, and systematic problem-solving patterns. Serves as the governing foundation for all DPF and LPF skills.

**Use when:**
- Guiding reasoning on engineering, research, and management tasks
- Requiring systematic evidence-based problem-solving
- Building structured, verifiable solutions with traceable evidence

**Reference:** [GitHub Repository of the original First Principles Framework by Anatoly Levenchuk](https://github.com/ailev/FPF)

**Location:** `skills/fpf-core/`

### ⚡ FPF Narrative Prose

Generates compact, unambiguous FPF-structured output at F4-F5 formality level using typed-slot notation. Designed for AI agent consumers and FPF-literate humans where token economy and auditability matter — diagnostics, architecture decisions, code reviews, status reports, trust assessments, system compositions. Replaces verbose prose (~65% token savings, lossless).

**Depends on:** `fpf-core`

**Use when:**
- Writing diagnostics, ADRs, code reviews, or status reports for AI agent consumers
- Composing trust/assurance assessments with F-G-R-CL tuples
- Building Γ (gamma) system/epistemic compositions with Quintet invariants
- Reconstructing clean prose from FPF blocks (removing all metadata)
- Any context where token economy AND auditability matter

**Do NOT use for:** casual chat, teaching, non-technical audiences, creative tasks.

**Location:** `skills/fpf-narrative/`

### 📖 FPF Literacy & DPF Authoring

Helps agents understand the FPF/DPF/LPF stack, create new domain practical frameworks (DPFs), load domain knowledge, distinguish FPF-grounded answers from generic AI responses, and choose the right carrier for publication.

**Depends on:** `fpf-core`

**Use when:**
- Teaching an agent the FPF ecosystem and its layers
- Creating a new DPF from scratch (~1 hour draft)
- Distinguishing vanilla AI answers from FPF-grounded reasoning
- Deciding whether to publish in-chat vs as a file

**Location:** `skills/dpf-fpf-literacy/`

### 🏗️ Layered Framework Workspace Architecture

Manages the FPF/DPF/LPF workspace structure: where to place frameworks, how to organize skill carriers, dependency chains, and LPF vs Project boundaries.

**Depends on:** `fpf-core`, `dpf-fpf-literacy`

**Use when:**
- Organizing the FPF/DPF/LPF workspace layout
- Deciding where a new framework belongs in the ecosystem
- Setting up skill-carrier structure for a DPF/LPF
- Resolving LPF vs Project boundary questions
- Packaging a DPF/LPF as a distributable skill

**Location:** `skills/dpf-lfw-architecture/`

## Business Analysis & Requirements Engineering

Domain practical framework for structured business analysis and requirements engineering in engineering projects.

### 📋 Business Analysis & Requirements Engineering

Covers the full requirements lifecycle: stakeholder identification, elicitation, specification, prioritization, validation, traceability, and change management. Includes business process modeling, use case modeling, and data/security requirements.

**Depends on:** `fpf-core`

**Use when:**
- Identifying and managing stakeholders
- Eliciting, specifying, or prioritizing requirements
- Validating or tracing requirements
- Managing requirements changes
- Modeling business processes or use cases
- Defining data or security requirements

**Location:** `skills/dpf-business-analysis/`

## Text Analysis & Writing

Skills for analyzing existing texts and extracting reusable structure, argumentation, and rhetorical patterns.

### 🔍 Reverse-Engineering Texts

Reverse-engineer texts into a reusable structural blueprint (reverse outlining, argument mining, copy teardown).

**Use when:**
- Analyzing a text's thesis, hook, and macro-structure
- Extracting argument maps and support/evidence moves
- Mapping rhetoric (Ethos/Pathos/Logos)
- Converting "text → structure/blueprint" to reuse patterns in writing, specs, prompts, or marketing

**Location:** `skills/reverse-engineering-texts/`

## Development Tools

Tools for creating and managing AI agent skills and FPF/DPF/LPF documentation.

### 📚 Spec Decomposer

Splits monolithic framework specifications (FPF/DPF/LPF) into atomic skill reference files. Includes Python scripts for automated decomposition of FPF (`:End`-delimited patterns) and DPF (sections 1–10 structure) monoliths.

**Depends on:** `fpf-core`, `dpf-fpf-literacy`, `dpf-lfw-architecture`

**Use when:**
- Decomposing a framework monolith into skill references
- Updating references/ after monolith specification changes
- Setting up a new DPF/LPF skill from a monolith spec

**Location:** `skills/spec-decomposer/`

### 🔧 Agent Skill Builder

Guide for deciding when to create agent skills, how to design them well, and what anti-patterns to avoid. Covers the four-layer agent guidance stack (AGENTS.md, Skills, MCP, Memory), atomicity principles, and quality gates.

**Use when:**
- Creating a new skill or reviewing an existing one
- Deciding between skills vs AGENTS.md vs MCP vs Memory
- Designing atomic, reusable skills with progressive disclosure
- Unsure if a skill is needed at all

**Location:** `skills/create-agent-skill/`

## Project Management

Skills for tracking project state, decisions, risks, and dependencies in a structured markdown vault.

### 🗂️ Project Vault

Maintains project state in a markdown vault (tasks, dependencies, risks, key decisions, open questions, agendas, reports) from meeting transcripts, structured notes, or owner chat updates.

**Use when:**
- Initializing a project vault in a new repository
- Updating project state from meeting transcripts or user briefings
- Managing stakeholders and responsibilities
- Generating status reports, open question lists, or meeting agendas
- Surfacing contradictions and risks across project canon

**Location:** `skills/project-vault/`

## Space Planning & Organization

Skills for optimizing physical spaces and organizing belongings with systematic methodologies.

### 🚿 Bathroom Planner

Structured 10-stage methodology for planning bathroom layouts with focus on ergonomics, functionality, and safety.

**Use when:**
- Planning bathroom furniture placement
- Optimizing bathroom space
- Arranging bathroom fixtures (toilet, sink, bathtub, washing machine)
- Solving bathroom layout challenges

**Applicable to:** Large bathrooms (10+ square meters) with flexible plumbing.

**Location:** `skills/bathroom-planner/`

### 🧥 Wardrobe Planner

Structured 7-stage methodology for planning wardrobe/closet organization based on First Principles Framework.

**Use when:**
- Organizing closet space
- Planning wardrobe storage
- Arranging clothing and accessories
- Optimizing closet layout
- Solving wardrobe organization challenges

**Location:** `skills/wardrobe-planner/`

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

- [Custom Agent Skills Collection](#custom-agent-skills-collection)
  - [How to Use](#how-to-use)
    - [Installation](#installation)
    - [Usage](#usage)
  - [Table of Contents](#table-of-contents)
  - [Frameworks \& Methodologies](#frameworks--methodologies)
    - [🧠 First Principles Framework (FPF Core)](#-first-principles-framework-fpf-core)
    - [⚡ FPF Narrative Prose](#-fpf-narrative-prose)
    - [📖 Pattern Language as Agent Skill (PLAS)](#-pattern-language-as-agent-skill-plas)
    - [🏗️ Layered Framework Workspace Architecture](#️-layered-framework-workspace-architecture)
  - [Business Analysis \& Requirements Engineering](#business-analysis--requirements-engineering)
    - [📋 Business Analysis \& Requirements Engineering](#-business-analysis--requirements-engineering)
  - [Text Analysis \& Writing](#text-analysis--writing)
    - [🔍 Reverse-Engineering Texts](#-reverse-engineering-texts)
  - [Document Processing](#document-processing)
    - [📄 PDF to Markdown (pdf2md)](#-pdf-to-markdown-pdf2md)
  - [Development Tools](#development-tools)
    - [🔄 FPF Sync](#-fpf-sync)
    - [🔧 Agent Skill Builder](#-agent-skill-builder)
  - [Project Management](#project-management)
    - [🗂️ Project Vault](#️-project-vault)
  - [Space Planning \& Organization](#space-planning--organization)
    - [🚿 Bathroom Planner](#-bathroom-planner)
    - [🧥 Wardrobe Planner](#-wardrobe-planner)


## Frameworks & Methodologies

Structured reasoning frameworks and domain-specific methodologies for systematic problem-solving.

### 🧠 First Principles Framework (FPF Core)

Root framework and pattern library providing auditable thinking, evidence chains, and systematic problem-solving patterns. Serves as the governing foundation for all DPF and LPF skills. Patterns are loaded individually from `references/` (pattern reference files + INDEX + context sections) via a fast index — never the full spec.

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

### 📖 Pattern Language as Agent Skill (PLAS)

Author and improve a Domain Principle Framework (DPF) or Local Practices Framework (LPF) directly in Agent-skill form (SKILL.md + references/). The edition carrier is the skill itself: `references/*.md` are the canonical pattern bodies — no monolith, no reader-facing publication form.

**Depends on:** `fpf-core`, `create-agent-skill`

**Use when:**
- Deciding whether and what to author as a DPF-skill (cold start)
- Authoring a DPF or LPF as an agent skill (FPF-grounded or self-sufficient variant)
- Evaluating, improving, refreshing a DPF or LPF as a skill

**Location:** `skills/pattern-language-as-agent-skill/`

### 🏗️ Layered Framework Workspace Architecture

Manages the FPF/DPF/LPF workspace structure: where to place frameworks, how to organize skill carriers, dependency chains, and LPF vs Project boundaries.

**Depends on:** `fpf-core`, `pattern-language-as-agent-skill`

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

## Document Processing

Skills for converting and extracting content from document formats.

### 📄 PDF to Markdown (pdf2md)

Extracts PDF content into clean Markdown: text via pdfplumber + image/diagram descriptions via a local vision-language model (LM Studio, Ollama, or any OpenAI-compatible endpoint). Supports recursive batch processing, resume/retry, and custom VL prompts.

**Use when:**
- Converting presentation decks (slides, diagrams) to text
- Extracting conference talks, workshops, or technical reports from PDF
- Transcribing PDFs where plain text extraction is garbled
- Batch-processing directories of PDFs with automatic skip of already-processed files

**Do NOT use for:** pure-text PDFs (use pdfplumber directly), filling PDF forms (use the `pdf` skill), scanned documents without selectable text.

**Dependencies:** `pip install pdfplumber pypdfium2 pillow requests` + local VL model (default: `qwen/qwen3-vl-8b` via LM Studio).

**Location:** `skills/pdf2md/`

## Development Tools

Tools for creating and managing AI agent skills and FPF/DPF/LPF documentation.

### 🔄 FPF Sync

Keeps the `fpf-core` skill in sync with the canonical FPF monolith (`FPF-Spec.md`). Self-contained tool that pulls the latest spec, decompiles it into atomic reference files, and updates the skill metadata.

**Use when:**
- The FPF specification has been updated (new commits upstream)
- The `fpf-core` skill references are stale or show wrong counts
- Running scheduled maintenance on layered framework workspace skills

**Dependencies:** Python 3.10+, `git` in PATH.

**Location:** `skills/fpf-sync/`

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

Local Practices Framework (LPF) for managing project state in a structured markdown vault: atomic cards for decisions, open questions, risks, contradictions, operational tracks, and work records. Governs working tracks as the mandatory container for all productive activity (research, analysis, synthesis). Routing `SKILL.md` + 10 `PV.*` patterns covering vault init, inbox/outbox processing, state updates, external research binding, track-bound work, and report generation.

**Depends on:** `fpf-core`

**Use when:**
- Initializing a project vault from scaffold (`PV.Init`)
- Processing the inbox (transcripts, PDFs, articles, research) into atomic decision/question/risk/contradiction cards (`PV.Inbox`)
- Updating project state from dialogue briefings or meeting transcripts (owner chat updates) (`PV.StateUpdate`)
- Processing external research with two-way binding to project entities (`PV.ExternalResearch`)
- Managing track-bound productive work (track lifecycle, artifacts, work records) (`PV.Track`, `PV.Artifact`, `PV.WorkRecord`)
- Generating reports and next-meeting agendas from open questions, blockers, and contradictions (`PV.Report`)
- Sending outgoing feedback or proposals to another system or skill (`PV.Outbox`)
- Reconciling new information against the open question registry and archiving closed entities

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

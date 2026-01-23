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

- [Space Planning & Organization](#space-planning--organization)
  - [Bathroom Planner](#-bathroom-planner)
  - [Wardrobe Planner](#-wardrobe-planner)
- [Development Tools](#development-tools)
  - [Spec Decomposer](#-spec-decomposer)
- [Thinking Methodologies](#thinking-methodologies)
  - [First Principles Framework](#-first-principles-framework-fpf)

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

## Development Tools

Tools for creating and managing AI agent skills and documentation.

### 📚 Spec Decomposer

Decompose large unified specifications into agent skills with progressive disclosure.

**Use when:**
- Converting documentation, frameworks, or knowledge bases exceeding 50KB
- Creating properly structured skills that Claude can navigate efficiently
- Implementing multi-level progressive disclosure for large content

**Location:** `skills/spec-decomposer/`

## Thinking Methodologies

Frameworks for structured reasoning and systematic problem-solving.

### 🧠 First Principles Framework (FPF)

Structured reasoning skill for any task requiring auditable thinking, evidence chains, systematic problem-solving, or holonic composition.

**Use when:**
- Guiding reasoning on engineering, research, and management tasks
- Requiring systematic evidence-based problem-solving
- Building structured, verifiable solutions

**Reference:** [FPF GitHub Repository](https://github.com/dimonier/FPF/tree/skill)

**Location:** `skills/fpf/`

---
name: reverse-engineering-texts
description: Reverse-engineer texts into a reusable structural blueprint (reverse outlining, argument mining, copy teardown). Use when the user asks to analyze a text’s thesis, hook, framework (AIDA/PAS/PASTOR/BAB), argument map, rhetoric (Ethos/Pathos/Logos), or when they want to convert “text → structure/blueprint” to reuse patterns in writing, specs, prompts, or marketing.
---

# Reverse-Engineering Texts

## Goal
Turn a finished text into a **TeardownBlueprint** (a “drawing”) that is reusable: structure, argument moves, and rhetorical patterning.

## Core disciplines (FPF-aligned)
- **Strict distinction**: TextArtifact (the text) ≠ Blueprint (your description) ≠ Output (new draft/prompt).
- **Evidence first**: Every non-trivial claim in the blueprint must include a short **quote** from the text (an “evidence anchor”).
- **Parsimony**: Prefer the simplest structure/framework that explains the whole text.
- **Uncertainty**: Mark low-confidence inferences explicitly.

## Quick workflow (text → blueprint)
1. **Ingest**: Copy the raw text verbatim as `TextArtifact`.
2. **Segment**: Split into semantic blocks; name each block with a one-line intent.
3. **Spine**: Infer the thesis and macro-structure (framework hypothesis).
4. **Hook**: Classify the hook type + target emotion.
5. **Argument map**: For each block, extract Claim + Support/Evidence type + relation to previous block.
6. **Rhetoric**: Map Ethos/Pathos/Logos and where each is used.
7. **Pattern extraction**: Capture reusable micro-patterns (openings, transitions, proof moves).
8. **Reconstruct forward outline**: Produce a forward scaffold (thesis → hook → outline → arguments).
9. **Audit**: Ensure coverage + evidence anchors + note alternatives when ambiguous.

## Output contract
Produce a `TeardownBlueprint` using the template in [references/blueprint-template.md](references/blueprint-template.md).

### Minimum QA checklist
- [ ] Every major block is represented in `segments`.
- [ ] Thesis and framework claims include quotes.
- [ ] Each argument block has (claim, evidence_type, relation) + quote(s).
- [ ] At least one reusable pattern is extracted.
- [ ] Any guesswork is labeled with `confidence: low` and an alternative hypothesis is listed.

## Next actions (optional)
- Generate a new draft *from the blueprint* (structure-first).
- Build a personal `PatternLibrary` (swipe/teardown file) from repeated blueprints.

## Additional resources
- Blueprint schema: [references/blueprint-template.md](references/blueprint-template.md)
- Framework markers: [references/frameworks-and-markers.md](references/frameworks-and-markers.md)
- End-to-end examples: [references/examples.md](references/examples.md)

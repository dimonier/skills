# VL Prompt for PDF -> Markdown Extraction

This prompt is sent to the VL model for each PDF page.
Edit it here — the script reads it from the `VL_PROMPT` variable in `scripts/extract_pdfs.py`.

## Current Prompt

```
You are extracting meaning from a presentation slide. Your task is to convey CONTENT, not appearance.

RULES:
1. NEVER describe fonts, colors, margins, backgrounds, alignment, "visual design",
   "element placement", "styling".
2. DO NOT write intros like "This slide shows...", "This is a title slide...",
   "The slide features..." — go straight to the content.
3. DO NOT invent "Overall assessment", "Conclusions", "Meaning of elements" —
   only what IS on the slide.

WHAT TO DO:
A. Extract ALL visible text verbatim (titles, subtitles, bullets, captions, numbers, dates).
B. If there is a diagram / schema / chart / table — describe WHAT IT COMMUNICATES:
   what data it compares, what trend it shows, what relationship or structure it illustrates.
   Do not describe how it looks — describe its meaning.
C. If the slide contains a code screenshot — reproduce the code verbatim.
D. Convey the logical structure: thesis -> arguments -> examples -> implications —
   if traceable on the slide.

FORMAT: concise, dense, no filler. Every line must carry information.
```

## Iteration History

### v1 (failed)
Problem: prompt asked for "maximum detail" -> model produced 80% font/color/design descriptions.

### v2 (fixed)
- Added strict prohibitions on visual design descriptions
- Removed token limit (was 1500 — cut off content)
- Focus on verbatim text extraction and diagram meaning

## Tuning Tips

- **Too much filler** -> strengthen "concise, dense, no filler" wording
- **Missing text in images** -> add "extract ALL text, even small print"
- **Not understanding diagrams** -> add an example: "e.g.: 'funnel: 1000 leads -> 200 qualified -> 50 sales, 5% conversion'"
- **Paraphrasing instead of extracting** -> add "extract text VERBATIM, do not paraphrase"

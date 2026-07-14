---
name: pdf2md
description: Convert PDF files to Markdown — extracts text with pdfplumber and describes images/diagrams via a local vision-language model. Use when the user asks to extract PDF content, convert presentation slides to text, transcribe conference talks from PDFs, or OCR diagrams and charts from documents.
---

# PDF -> Markdown (pdf2md)

Extracts PDF content into Markdown: text as-is + image/diagram meaning via a Vision Language Model.

## When to Use

- User asks to "extract from PDF", "convert PDF to text/Markdown", "transcribe slides"
- Presentation decks (text + graphics + diagrams)
- Conference talks, workshops, technical reports
- PDFs where plain text extraction produces garbled output

## When NOT to Use

- PDFs that are purely text (use pdfplumber directly — faster, no VL needed)
- One-page forms or invoices (use pdfplumber tables)
- Filling PDF forms (use well known `pdf` skill instead)
- Scanned documents without selectable text (this skill works, but OCR-only tools may be faster)

## Dependencies

Install once per environment:

```bash
pip install pdfplumber pypdfium2 pillow requests
```

## VL Model Setup

Default: **LM Studio** with `qwen/qwen3-vl-8b` loaded on `localhost:1234`.

Any OpenAI-compatible endpoint works — Ollama, vLLM, cloud providers. To switch:

```bash
python scripts/extract_pdfs.py --source "<path>" --model "llama3.2-vision" --api-url "http://localhost:11434/v1/chat/completions"
```

## Workflow

### Step 1: Verify VL model is reachable

```bash
python -c "import requests; r = requests.get('http://localhost:1234/v1/models'); print([m['id'] for m in r.json()['data']])"
```

If you don't see your VL model, load it in LM Studio before proceeding.

### Step 2: Test on 1-2 PDFs first

```bash
python scripts/extract_pdfs.py --source "<path-to-pdfs>" --first 2
```

Check the output in `_markdown/`. If quality is poor (too much "water", missing text, or style descriptions leaking through), edit the prompt in `references/vl-prompt.md` and the `VL_PROMPT` variable in the script, then re-run with `--force`.

### Step 3: Run on everything

```bash
python scripts/extract_pdfs.py --source "<path-to-pdfs>"
```

Already-processed PDFs are skipped automatically. Use `--force` to overwrite.

### Step 4: If something fails

- **VL call fails (3 retries exhausted)**: page is left with fallback text from pdfplumber, or marked `[VL error]`
- **Rendering fails**: page is skipped, counted as error
- **Output file corrupted**: delete the `.md` and re-run — the script will re-process it
- **Model runs out of VRAM**: reduce `RENDER_SCALE` in the script (1.5 or 1.0)

## Script Arguments

| Argument | Default | Description |
|----------|---------|-------------|
| `--source` | *(required)* | Directory with PDF files (recursive) |
| `--output` | `_markdown/` inside source | Output directory for .md files |
| `--model` | `qwen/qwen3-vl-8b` | VL model ID |
| `--api-url` | `http://localhost:1234/v1/chat/completions` | API endpoint |
| `--first N` | *(all)* | Process only first N PDFs |
| `--files "s1,s2"` | *(all)* | Filter by filename substring |
| `--force` | `false` | Overwrite existing output |

## Output Structure

```
_source/
  _markdown/
    subfolder/
      presentation1.md
      presentation2.md
```

Folder structure mirrors the source. Each `.md` file:

```markdown
# Presentation Title

---
## Page 1 / 40

**[VL slide description]**

<content extracted by VL model>

---
## Page 2 / 40
...
```

## VL Prompt Rules (hard-won lessons)

1. **Never** describe fonts, colors, margins, backgrounds — only content
2. **Never** write intros like "This slide shows..." — start with content
3. **Never** invent "Conclusions" or "Overall assessment" sections
4. Extract ALL text verbatim
5. For diagrams/charts: describe MEANING, not appearance
6. Concise, dense, no filler — every sentence must carry information
7. Do NOT limit output tokens — let the model decide

See `references/vl-prompt.md` for the full prompt template and tuning guide.

## Performance

| GPU | Sec/page | 1000 pages |
|-----|---------|------------|
| RTX 3090/4090 | ~7-10s | ~2 hours |
| M1/M2 Mac (LM Studio) | ~15-20s | ~4-5 hours |
| CPU-only | ~60-120s | Not recommended |

## See Also

- [VL Prompt (references/vl-prompt.md)](references/vl-prompt.md) — prompt template + iteration history + tuning tips
- [Script (scripts/extract_pdfs.py)](scripts/extract_pdfs.py) — the extraction tool

---

> **Evolution rule:** If you are dissatisfied with the extraction quality or the workflow, identify what to change (prompt, script parameters, dependencies) and offer to update this skill. The prompt lives in `references/vl-prompt.md`; the extraction logic in `scripts/extract_pdfs.py`.

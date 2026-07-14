"""
PDF -> Markdown extraction pipeline.
Renders each page as image, VL model describes content, assembles into .md.

Usage:
  python extract_pdfs.py --source "D:\PDFs" [--output "D:\Output"] [--model "qwen/qwen3-vl-8b"]
  python extract_pdfs.py --source "D:\PDFs" --first 2           # test on 2 PDFs
  python extract_pdfs.py --source "D:\PDFs" --files "speaker"   # filter by filename
  python extract_pdfs.py --source "D:\PDFs" --force             # re-process existing

Requirements:
  pip install pdfplumber pypdfium2 pillow requests
"""

import argparse
import base64
import io
import json
import os
import sys
import time
import traceback
from pathlib import Path

try:
    import pdfplumber
    import pypdfium2 as pdfium
    import requests
except ImportError as e:
    print(f"Missing dependency: {e}")
    print("Install: pip install pdfplumber pypdfium2 pillow requests")
    sys.exit(1)

# ── Defaults ──────────────────────────────────────────
DEFAULT_MODEL = "qwen/qwen3-vl-8b"
DEFAULT_API_URL = "http://localhost:1234/v1/chat/completions"
RENDER_SCALE = 2.0       # ~144 DPI
DELAY_BETWEEN_VL = 1.5   # seconds between VL calls
VL_TIMEOUT = 120         # seconds per VL call
VL_RETRIES = 3
VL_RETRY_DELAY = 5

VL_PROMPT = (
    "You are extracting meaning from a presentation slide. Convey CONTENT, not appearance.\n\n"
    "RULES:\n"
    "1. NEVER describe fonts, colors, margins, backgrounds, alignment, 'visual design', "
    "'element placement', 'styling'.\n"
    "2. DO NOT write intros like 'This slide shows...', 'This is a title slide...', "
    "'The slide features...' — go straight to the content.\n"
    "3. DO NOT invent 'Overall assessment', 'Conclusions', 'Meaning of elements' sections — "
    "only what IS on the slide.\n\n"
    "WHAT TO DO:\n"
    "A. Extract ALL visible text verbatim (titles, subtitles, bullets, captions, numbers, dates).\n"
    "B. If there is a diagram / schema / chart / table — describe WHAT IT COMMUNICATES: "
    "what data it compares, what trend it shows, what relationship or structure it illustrates. "
    "Do not describe how it looks — describe its meaning.\n"
    "C. If the slide contains a code screenshot — reproduce the code verbatim.\n"
    "D. Convey the logical structure: thesis -> arguments -> examples -> implications — "
    "if traceable on the slide.\n\n"
    "FORMAT: concise, dense, no filler. Every line must carry information.\n"
    "IMPORTANT: Write your response in the SAME LANGUAGE as the slide content."
)


def log(msg: str) -> None:
    print(f"[{time.strftime('%H:%M:%S')}] {msg}", flush=True)


def vl_describe_image(image, api_url: str, model: str) -> str | None:
    """Send PIL image to VL model, return description or None."""
    buf = io.BytesIO()
    image.save(buf, format="PNG")
    img_b64 = base64.b64encode(buf.getvalue()).decode("utf-8")

    body = {
        "model": model,
        "messages": [{
            "role": "user",
            "content": [
                {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{img_b64}"}},
                {"type": "text", "text": VL_PROMPT},
            ]
        }],
    }

    for attempt in range(1, VL_RETRIES + 1):
        try:
            resp = requests.post(api_url, json=body, timeout=VL_TIMEOUT)
            resp.raise_for_status()
            data = resp.json()
            return data["choices"][0]["message"]["content"]
        except Exception as e:
            log(f"  VL attempt {attempt}/{VL_RETRIES} failed: {e}")
            if attempt < VL_RETRIES:
                time.sleep(VL_RETRY_DELAY)
    return None


def process_pdf(pdf_path: str, out_path: str, api_url: str, model: str) -> dict:
    """Process one PDF file, write markdown to out_path."""
    pdf_name = os.path.splitext(os.path.basename(pdf_path))[0]
    log(f"Processing: {pdf_name}")

    stats = {"pages": 0, "vl_calls": 0, "vl_success": 0, "errors": 0}

    try:
        pdfium_pdf = pdfium.PdfDocument(pdf_path)
        total = len(pdfium_pdf)
        stats["pages"] = total
    except Exception as e:
        log(f"  ERROR opening PDF: {e}")
        stats["errors"] += 1
        return stats

    md_lines = [f"# {pdf_name}\n"]

    with pdfplumber.open(pdf_path) as pdf:
        for i, page in enumerate(pdf.pages):
            text = (page.extract_text() or "").strip()

            try:
                bitmap = pdfium_pdf[i].render(scale=RENDER_SCALE)
                pil_img = bitmap.to_pil()
            except Exception as e:
                log(f"  Page {i+1}/{total}: render FAILED: {e}")
                stats["errors"] += 1
                continue

            log(f"  Page {i+1}/{total} VL ({pil_img.size[0]}x{pil_img.size[1]}) {len(text)}c text")
            time.sleep(DELAY_BETWEEN_VL)
            stats["vl_calls"] += 1

            desc = vl_describe_image(pil_img, api_url, model)
            md_lines.append(f"\n---\n## Страница {i+1} / {total}\n")

            if desc:
                stats["vl_success"] += 1
                md_lines.append(f"**[VL-описание слайда]**\n\n{desc.strip()}")
            else:
                stats["errors"] += 1
                if text:
                    md_lines.append(text)
                else:
                    md_lines.append(f"*[VL ошибка — содержимое не извлечено]*")
            md_lines.append("")

    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(md_lines))

    log(f"  -> {out_path}  |  {stats['pages']}p, {stats['vl_calls']}VL, {stats['vl_success']}OK, {stats['errors']}err")
    return stats


def collect_pdfs(src_dir: str) -> list[str]:
    """Find all PDF files recursively, excluding _prefixed dirs."""
    pdf_files = []
    for root, dirs, files in os.walk(src_dir):
        if os.path.basename(root).startswith("_"):
            continue
        for f in sorted(files):
            if f.lower().endswith(".pdf"):
                pdf_files.append(os.path.join(root, f))
    return pdf_files


def main():
    parser = argparse.ArgumentParser(
        description="PDF -> Markdown extraction with VL model",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""Examples:
  %(prog)s --source "D:\\Conference"                          # all PDFs in folder
  %(prog)s --source "D:\\Conference" --first 2                # test on first 2 PDFs
  %(prog)s --source "D:\\Conference" --files "speaker"        # filter by filename
  %(prog)s --source "D:\\Conference" --force                  # re-process existing
  %(prog)s --source "D:\\Conference" --api-url "http://localhost:11434/v1/chat/completions"
        """
    )
    parser.add_argument("--source", required=True, help="Source directory with PDF files")
    parser.add_argument("--output", default=None, help="Output directory (default: _markdown inside source)")
    parser.add_argument("--model", default=DEFAULT_MODEL, help=f"VL model ID (default: {DEFAULT_MODEL})")
    parser.add_argument("--api-url", default=DEFAULT_API_URL, help=f"API endpoint (default: {DEFAULT_API_URL})")
    parser.add_argument("--first", type=int, help="Process only first N PDFs (sorted by name)")
    parser.add_argument("--files", type=str, help="Comma-separated substrings to match file names")
    parser.add_argument("--force", action="store_true", help="Re-process even if output exists")
    args = parser.parse_args()

    src_dir = args.source
    if not os.path.isdir(src_dir):
        log(f"ERROR: Source directory not found: {src_dir}")
        sys.exit(1)

    out_dir = args.output or os.path.join(src_dir, "_markdown")

    log(f"Source: {src_dir}")
    log(f"Output: {out_dir}")
    log(f"Model: {args.model}")
    log(f"API:   {args.api_url}")
    if args.first:
        log(f"Limit: first {args.first} PDFs")
    if args.files:
        log(f"Filter: '{args.files}'")
    log("=" * 60)

    pdf_files = collect_pdfs(src_dir)
    total_available = len(pdf_files)

    # Filter by name
    if args.files:
        filters = [s.strip() for s in args.files.split(",")]
        pdf_files = [f for f in pdf_files if any(filt in os.path.basename(f) for filt in filters)]
        log(f"Filtered: {len(pdf_files)}/{total_available} PDFs match")
    if args.first:
        pdf_files = pdf_files[:args.first]
        log(f"Limited to first {len(pdf_files)} PDFs")

    if not pdf_files:
        log("No PDFs to process!")
        return

    total_stats = {"pages": 0, "vl_calls": 0, "vl_success": 0, "errors": 0}
    start_time = time.time()

    for idx, pdf_path in enumerate(pdf_files):
        log(f"\n[{idx+1}/{len(pdf_files)}] {os.path.basename(pdf_path)}")

        rel_path = os.path.relpath(pdf_path, src_dir)
        out_rel = os.path.splitext(rel_path)[0] + ".md"
        out_path = os.path.join(out_dir, out_rel)

        if os.path.exists(out_path) and not args.force:
            log(f"  SKIP: already exists (use --force to re-process)")
            continue

        stats = process_pdf(pdf_path, out_path, args.api_url, args.model)
        for k in total_stats:
            total_stats[k] += stats[k]

    elapsed = time.time() - start_time
    log(f"\n{'='*60}")
    log(f"TOTAL: {total_stats['pages']} pages, {total_stats['vl_calls']} VL calls, "
        f"{total_stats['vl_success']} OK, {total_stats['errors']} errors")
    log(f"Time: {elapsed/60:.1f} min")


if __name__ == "__main__":
    main()

"""Build the full-wrap paperback cover for Amazon KDP (back cover + spine + front cover, with bleed).

    python kdp/build_cover.py --pages 252                       # the defaults: 8.5 x 11 in, premium color, white paper
    python kdp/build_cover.py --pages 252 --ink bw              # black-and-white interior (thinner spine)
    python kdp/build_cover.py --pages 252 --trim 7x10 --paper cream

Writes to kdp/out/:
    cover-wrap.pdf                  the print-ready cover (vector text), upload this to KDP
    cover-wrap-flattened.pdf        the same cover as one 300-dpi image, use it if KDP complains about transparency
    cover-template-guides.pdf/.png  your cover with the bleed, trim, safe, spine, and barcode guides drawn on
    cover-template-blank.pdf/.png   an empty template with the same guides, for designing a cover in another tool
    book-info.md                    the listing sheet with the paperback author name filled in
    front-cover.png / .jpg          the front cover alone, for your book's Amazon page and for sharing

The spine width depends on the page count, so build the interior first and pass its page count.
KDP's spine numbers can change. Check them at kdp.amazon.com (Cover Calculator) before you upload.
"""

from __future__ import annotations

import argparse
import html
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "scripts"))
from build_pdf import font_css  # noqa: E402
from guide import BOOK_SUBTITLE, BOOK_TAGLINE, BOOK_TITLE, SITE, kdp_author  # noqa: E402

# Inches of spine per page, as published by KDP (verify before uploading).
SPINE_PER_PAGE = {
    ("white", "bw"): 0.002252,
    ("cream", "bw"): 0.0025,
    ("white", "standard-color"): 0.002252,
    ("white", "premium-color"): 0.002347,
}
BLEED = 0.125  # inches, on every outside edge
SAFE = 0.375   # inches inside the trim edge where text and faces should stay (KDP's minimum is 0.25)
BARCODE = (2.0, 1.2)  # KDP puts the ISBN barcode in a 2 x 1.2 inch box
MIN_SPINE_TEXT_PAGES = 79  # KDP only allows spine text above this page count

BLURB = (
    "You've heard “just put it on GitHub” a hundred times. This book finally explains what that means, "
    "without a single command to type."
)
INSIDE = [
    "What Git and GitHub really are, in plain English",
    "GitHub Desktop and the website, one click at a time",
    "Branches, pull requests, issues, and teamwork",
    "How to undo almost any mistake",
    "Publish a free website and build a profile",
    "Four guided projects, quizzes, and a 30-day plan",
]


def cover_html(pages: int, trim_w: float, trim_h: float, spine: float, mode: str) -> str:
    """mode: 'art' (the finished cover), 'guides' (art + guides), 'blank' (guides only)."""
    total_w = 2 * trim_w + spine + 2 * BLEED
    total_h = trim_h + 2 * BLEED
    front_x = BLEED + trim_w + spine           # left edge of the front cover's trim
    spine_x = BLEED + trim_w                   # left edge of the spine
    show_art = mode in ("art", "guides")
    show_guides = mode in ("guides", "blank")
    show_spine_text = pages > MIN_SPINE_TEXT_PAGES and spine >= 0.25

    title = html.escape(BOOK_TITLE)
    sub = html.escape(BOOK_SUBTITLE)
    author = html.escape(kdp_author())
    bullets = "".join(f"<li>{html.escape(t)}</li>" for t in INSIDE)

    # The branching-lines illustration on the front cover. Lines and tiny commit marks, not dots.
    art_svg = """
<svg viewBox="0 0 850 640" preserveAspectRatio="none" xmlns="http://www.w3.org/2000/svg" style="transform: scaleX(-1)">
  <defs>
    <linearGradient id="g1" x1="0" y1="1" x2="1" y2="0">
      <stop offset="0" stop-color="#6d28d9"/><stop offset="0.55" stop-color="#a855f7"/><stop offset="1" stop-color="#f0abfc"/>
    </linearGradient>
    <linearGradient id="g2" x1="0" y1="1" x2="1" y2="0">
      <stop offset="0" stop-color="#4c1d95"/><stop offset="0.5" stop-color="#8b5cf6"/><stop offset="1" stop-color="#c4b5fd"/>
    </linearGradient>
    <linearGradient id="g3" x1="0" y1="1" x2="1" y2="0">
      <stop offset="0" stop-color="#7c3aed"/><stop offset="0.6" stop-color="#d946ef"/><stop offset="1" stop-color="#fbcfe8"/>
    </linearGradient>
  </defs>
  <g fill="none" stroke-linecap="round">
    <!-- soft glow underlays -->
    <g opacity="0.16" stroke="#a855f7" stroke-width="22">
      <path d="M-40 600 C 140 600, 230 520, 330 470 S 520 360, 610 290 S 760 170, 900 130"/>
      <path d="M180 566 C 250 470, 330 400, 420 380 S 560 372, 610 290"/>
    </g>
    <g opacity="0.10" stroke="#e879f9" stroke-width="18">
      <path d="M330 470 C 380 540, 470 560, 560 520 S 700 430, 760 360"/>
    </g>
    <!-- trunk -->
    <path d="M-40 600 C 140 600, 230 520, 330 470 S 520 360, 610 290 S 760 170, 900 130" stroke="url(#g1)" stroke-width="5"/>
    <!-- a branch that leaves early and merges back -->
    <path d="M180 566 C 250 470, 330 400, 420 380 S 560 372, 610 290" stroke="url(#g2)" stroke-width="4"/>
    <!-- a second branch that leaves later and runs on -->
    <path d="M330 470 C 380 540, 470 560, 560 520 S 700 430, 760 360" stroke="url(#g3)" stroke-width="4"/>
    <!-- a short side thread -->
    <path d="M610 290 C 650 240, 700 230, 760 238 S 840 262, 900 250" stroke="url(#g2)" stroke-width="3" opacity="0.8"/>
  </g>
  <!-- commit marks sit on the lines: a small ring around a bright center -->
  <g stroke="#0b0614" stroke-width="3">
    <g fill="#f5d0fe">
      <circle cx="330" cy="470" r="9"/><circle cx="610" cy="290" r="9"/><circle cx="760" cy="360" r="8"/>
    </g>
    <g fill="#ddd6fe">
      <circle cx="180" cy="566" r="8"/><circle cx="420" cy="380" r="8"/><circle cx="560" cy="520" r="8"/>
    </g>
    <g fill="#c4b5fd">
      <circle cx="760" cy="238" r="7"/><circle cx="470" cy="408" r="7"/>
    </g>
  </g>
</svg>"""

    guides = ""
    if show_guides:
        bw = BARCODE[0]
        bh = BARCODE[1]
        guides = f"""
<div class="g bleedline"></div>
<div class="g trim"></div>
<div class="g safe back"></div>
<div class="g safe front"></div>
<div class="g foldl"></div><div class="g foldr"></div>
<div class="g barcode"><span>ISBN barcode area<br>{bw} × {bh} in<br>(leave clear; KDP adds the barcode)</span></div>
<div class="g lab lback">BACK COVER<br>{trim_w} × {trim_h} in trim</div>
<div class="g lab lspine" style="left:{spine_x}in;width:{spine}in"><span>SPINE {spine:.3f} in</span></div>
<div class="g lab lfront">FRONT COVER<br>{trim_w} × {trim_h} in trim</div>
<div class="g lab lbleed">Bleed {BLEED} in (trimmed off)</div>
<div class="g lab lsafe">Keep text and faces inside the green line</div>
"""

    art = ""
    if show_art:
        spine_text = ""
        if show_spine_text:
            spine_text = f"""
<div class="spine-text" style="left:{spine_x}in;width:{spine}in">
  <div class="s-title">{title}</div>
  <div class="s-author">{author}</div>
</div>"""
        art = f"""
<div class="wrap-bg"></div>
<div class="spine-band" style="left:{spine_x}in;width:{spine}in"></div>
<div class="front-art" style="left:{front_x}in;width:{trim_w + BLEED}in">{art_svg}</div>

<!-- FRONT -->
<div class="front" style="left:{front_x}in;width:{trim_w}in">
  <div class="kicker">A beginner’s guide</div>
  <h1><span class="big">GitHub</span><span class="small">for Complete<br>Beginners</span></h1>
  <p class="sub">{sub}</p>
  <div class="tag">{html.escape(BOOK_TAGLINE)}</div>
  <div class="author">{author}</div>
</div>

<!-- SPINE -->
{spine_text}

<!-- BACK -->
<div class="back" style="left:{BLEED}in;width:{trim_w}in">
  <div class="kicker">Start here</div>
  <h2>Finally, GitHub that makes sense.</h2>
  <p class="lead">{html.escape(BLURB)}</p>
  <p>Written for complete beginners, this friendly guide teaches Git, GitHub Desktop, and the GitHub website step by step, in plain English. Make your account, save your work, try ideas without fear, work with other people, publish a website, and make your first open-source contribution.</p>
  <h3>Inside you’ll find</h3>
  <ul>{bullets}</ul>
  <h3>Perfect for</h3>
  <p class="who">Writers, students, designers, researchers, teachers, teams, and anyone who has ever been told to “just use GitHub.”</p>
  <p class="foot">Learn more and read it free online: <b>{html.escape(SITE.replace('https://', '').rstrip('/'))}</b></p>
</div>
"""

    return f"""<!doctype html><html><head><meta charset="utf-8">
<style>{font_css()}
@page {{ size: {total_w}in {total_h}in; margin: 0; }}
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
html, body {{ width: {total_w}in; height: {total_h}in; overflow: hidden; background: {'#e9e7ef' if mode == 'blank' else '#07040d'}; -webkit-print-color-adjust: exact; print-color-adjust: exact; }}
body {{ position: relative; font-family: "Plus Jakarta Sans", "Segoe UI", sans-serif; color: #e9e4f5; }}
.wrap-bg {{ position: absolute; inset: 0;
  background:
    radial-gradient(60% 55% at 92% 4%, rgba(168, 85, 247, 0.55) 0%, rgba(168, 85, 247, 0) 70%),
    radial-gradient(50% 45% at 78% 100%, rgba(217, 70, 239, 0.28) 0%, rgba(217, 70, 239, 0) 70%),
    radial-gradient(55% 50% at 8% 96%, rgba(109, 40, 217, 0.42) 0%, rgba(109, 40, 217, 0) 70%),
    radial-gradient(45% 40% at 20% 6%, rgba(76, 29, 149, 0.45) 0%, rgba(76, 29, 149, 0) 70%),
    #07040d; }}
.spine-band {{ position: absolute; top: 0; bottom: 0; background: linear-gradient(180deg, rgba(10, 6, 20, 0.55), rgba(10, 6, 20, 0.2) 50%, rgba(10, 6, 20, 0.55)); }}
.front-art {{ position: absolute; bottom: 1.55in; height: 4.7in; opacity: 0.95; }}
.front-art svg {{ width: 100%; height: 100%; display: block; }}

/* front */
.front {{ position: absolute; top: {BLEED}in; height: {trim_h}in; padding: {SAFE + 0.2}in {SAFE + 0.15}in {SAFE}in {SAFE + 0.25}in; }}
.front .kicker {{ font-size: 10.5pt; letter-spacing: 0.34em; text-transform: uppercase; color: #f0abfc; font-weight: 800; margin-top: 0.15in; }}
.front h1 {{ font-family: "Fraunces", Georgia, serif; font-weight: 800; color: #fff; letter-spacing: -0.03em; line-height: 0.92; margin-top: 0.3in; }}
.front h1 .big {{ display: block; font-size: 128pt; }}
.front h1 .small {{ display: block; font-size: 53pt; line-height: 1.02; margin-top: 0.08in; color: #f3e8ff; }}
.front .sub {{ margin-top: 0.34in; max-width: 5.4in; font-size: 14.5pt; line-height: 1.5; color: #d9d0ee; font-weight: 500; }}
.front .tag {{ position: absolute; left: {SAFE + 0.25}in; bottom: {SAFE + 0.78}in; font-size: 9.5pt; letter-spacing: 0.22em; text-transform: uppercase; color: #c4b5fd; font-weight: 700; }}
.front .author {{ position: absolute; left: {SAFE + 0.25}in; bottom: {SAFE + 0.12}in; font-size: 21pt; letter-spacing: 0.3em; text-transform: uppercase; color: #fff; font-weight: 700; }}
.front .author::before {{ content: ""; display: block; width: 0.8in; height: 4pt; border-radius: 2pt; background: linear-gradient(90deg, #a855f7, #f0abfc); margin-bottom: 0.16in; }}

/* spine (text reads top to bottom, as US books do) */
.spine-text {{ position: absolute; top: {BLEED}in; height: {trim_h}in; }}
.spine-text .s-title, .spine-text .s-author {{ position: absolute; left: 50%; transform: translateX(-50%); writing-mode: vertical-rl; white-space: nowrap; }}
.spine-text .s-title {{ top: 0.6in; font-family: "Fraunces", Georgia, serif; font-weight: 800; color: #fff; letter-spacing: -0.01em; font-size: {min(28, max(13, spine * 72 * 0.48)):.1f}pt; }}
.spine-text .s-author {{ bottom: 0.6in; font-family: "Plus Jakarta Sans", sans-serif; font-weight: 700; color: #e9d5ff; letter-spacing: 0.26em; text-transform: uppercase; font-size: {min(13, max(9, spine * 72 * 0.26)):.1f}pt; }}

/* back */
.back {{ position: absolute; top: {BLEED}in; height: {trim_h}in; padding: {SAFE + 0.45}in {SAFE + 0.35}in {SAFE}in {SAFE + 0.45}in; }}
.back .kicker {{ font-size: 10pt; letter-spacing: 0.34em; text-transform: uppercase; color: #f0abfc; font-weight: 800; }}
.back h2 {{ font-family: "Fraunces", Georgia, serif; font-weight: 800; color: #fff; font-size: 37pt; line-height: 1.05; letter-spacing: -0.02em; margin: 0.16in 0 0.26in; max-width: 5.6in; }}
.back p {{ font-size: 12.5pt; line-height: 1.6; color: #d4cbe8; margin-bottom: 0.16in; max-width: 5.7in; font-weight: 500; }}
.back p.lead {{ font-size: 14pt; line-height: 1.5; color: #fff; font-weight: 600; }}
.back h3 {{ font-family: "Plus Jakarta Sans", sans-serif; font-size: 10pt; letter-spacing: 0.26em; text-transform: uppercase; color: #c4b5fd; font-weight: 800; margin: 0.3in 0 0.12in; }}
.back ul {{ list-style: none; max-width: 5.6in; }}
.back li {{ position: relative; padding-left: 0.3in; font-size: 12pt; line-height: 1.45; color: #e9e4f5; margin: 0.07in 0; font-weight: 600; }}
.back li::before {{ content: ""; position: absolute; left: 0; top: 0.09in; width: 0.16in; height: 3pt; border-radius: 2pt; background: linear-gradient(90deg, #a855f7, #f0abfc); }}
.back .foot {{ position: absolute; left: {SAFE + 0.45}in; bottom: {SAFE + 0.15}in; max-width: 4in; font-size: 9.5pt; color: #a99fc7; line-height: 1.5; }}
.back .foot b {{ color: #e9d5ff; }}

/* guides */
.g {{ position: absolute; pointer-events: none; }}
.bleedline {{ inset: 0; border: 1.5pt solid #ef4444; }}
.trim {{ left: {BLEED}in; top: {BLEED}in; width: {total_w - 2 * BLEED}in; height: {trim_h}in; border: 1.2pt dashed #22d3ee; }}
.safe.back {{ left: {BLEED + SAFE}in; top: {BLEED + SAFE}in; width: {trim_w - 2 * SAFE}in; height: {trim_h - 2 * SAFE}in; border: 1.2pt dashed #4ade80; }}
.safe.front {{ left: {front_x + SAFE}in; top: {BLEED + SAFE}in; width: {trim_w - 2 * SAFE}in; height: {trim_h - 2 * SAFE}in; border: 1.2pt dashed #4ade80; }}
.foldl {{ left: {spine_x}in; top: 0; bottom: 0; border-left: 1.2pt solid #e879f9; }}
.foldr {{ left: {front_x}in; top: 0; bottom: 0; border-left: 1.2pt solid #e879f9; }}
.barcode {{ left: {BLEED + trim_w - 0.5 - BARCODE[0]}in; top: {BLEED + trim_h - 0.5 - BARCODE[1]}in; width: {BARCODE[0]}in; height: {BARCODE[1]}in; background: #ffffff; border: 1.2pt solid #111; display: flex; align-items: center; justify-content: center; text-align: center; font: 600 8pt "Plus Jakarta Sans", sans-serif; color: #444; line-height: 1.4; }}
.lab {{ font: 700 9pt "Plus Jakarta Sans", sans-serif; color: #67e8f9; line-height: 1.4; text-shadow: 0 0 4px #000; }}
.lback {{ left: {BLEED + 0.15}in; top: {BLEED + 0.12}in; }}
.lfront {{ left: {front_x + 0.15}in; top: {BLEED + 0.12}in; }}
.lspine {{ top: {BLEED + trim_h / 2 - 0.1}in; text-align: center; color: #f0abfc; }}
.lspine span {{ display: inline-block; transform: rotate(90deg); white-space: nowrap; }}
.lbleed {{ left: 0.04in; bottom: 0.02in; color: #f87171; font-size: 7pt; }}
.lsafe {{ left: {BLEED + SAFE + 0.1}in; bottom: {BLEED + SAFE - 0.2}in; color: #86efac; font-size: 7.5pt; }}
</style></head><body>
{art}{guides}</body></html>"""


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--pages", type=int, required=True, help="page count of the finished interior PDF")
    ap.add_argument("--trim", default="8.5x11", help="trim size in inches, like 8.5x11 or 6x9")
    ap.add_argument("--paper", choices=("white", "cream"), default="white")
    ap.add_argument("--ink", choices=("bw", "standard-color", "premium-color"), default="premium-color")
    ap.add_argument("--out", default=str(HERE / "out"))
    args = ap.parse_args()

    trim_w, trim_h = (float(x) for x in args.trim.lower().split("x"))
    key = (args.paper, args.ink)
    if key not in SPINE_PER_PAGE:
        sys.exit(f"KDP offers {args.ink} only on white paper. Try --paper white.")
    spine = round(args.pages * SPINE_PER_PAGE[key], 4)
    total_w = 2 * trim_w + spine + 2 * BLEED
    total_h = trim_h + 2 * BLEED
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)

    from playwright.sync_api import sync_playwright
    import pymupdf

    scale = 300 / 96  # 300 dpi
    with sync_playwright() as p:
        browser = p.chromium.launch()

        def render(mode: str, stem: str, pdf: bool = True, png: bool = True) -> None:
            page = browser.new_page(
                viewport={"width": round(total_w * 96), "height": round(total_h * 96)}, device_scale_factor=scale
            )
            page.set_content(cover_html(args.pages, trim_w, trim_h, spine, mode))
            page.wait_for_timeout(400)
            if pdf:
                page.pdf(path=str(out / f"{stem}.pdf"), width=f"{total_w}in", height=f"{total_h}in",
                         print_background=True, prefer_css_page_size=True)
            if png:
                page.screenshot(path=str(out / f"{stem}.png"), full_page=False)
            page.close()

        render("art", "cover-wrap", pdf=True, png=True)
        render("guides", "cover-template-guides")
        render("blank", "cover-template-blank")

        # The front cover alone, for the book's Amazon page.
        page = browser.new_page(viewport={"width": round(total_w * 96), "height": round(total_h * 96)}, device_scale_factor=scale)
        page.set_content(cover_html(args.pages, trim_w, trim_h, spine, "art"))
        page.wait_for_timeout(400)
        front_left = BLEED + trim_w + spine
        page.screenshot(
            path=str(out / "front-cover.png"),
            clip={"x": front_left * 96, "y": BLEED * 96, "width": trim_w * 96, "height": trim_h * 96},
        )
        page.close()
        browser.close()

    # Flattened copy: one 300-dpi picture inside a PDF.
    doc = pymupdf.open()
    pg = doc.new_page(width=total_w * 72, height=total_h * 72)
    pg.insert_image(pg.rect, filename=str(out / "cover-wrap.png"))
    doc.save(str(out / "cover-wrap-flattened.pdf"))
    doc.close()
    # A JPG of the front cover.
    pix = pymupdf.Pixmap(str(out / "front-cover.png"))
    pix.save(str(out / "front-cover.jpg"), jpg_quality=92)

    # A copy of the listing sheet with the paperback author name filled in (this copy stays on your computer).
    info = (HERE / "book-info.md").read_text(encoding="utf-8").replace("{{AUTHOR}}", kdp_author())
    (out / "book-info.md").write_text(info, encoding="utf-8")

    print(f"Spine: {spine:.4f} in for {args.pages} pages ({args.paper} paper, {args.ink})")
    print(f"Full cover: {total_w:.4f} x {total_h:.4f} in  =  {round(total_w * 300)} x {round(total_h * 300)} px at 300 dpi")
    print(f"Wrote files to {out}")


if __name__ == "__main__":
    main()

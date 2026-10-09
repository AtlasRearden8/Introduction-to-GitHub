# Publishing on Amazon KDP

Everything you need to turn this guide into a paperback.

| File | What it is |
|------|------------|
| `build_cover.py` | Builds the full-wrap cover (back, spine, front) and the guide templates |
| `book-info.md` | Title, subtitle, description, keywords, categories, and a pre-publish checklist |
| `out/` | The finished files (made by the scripts, not saved in git) |

## The files in `out/`

| File | Use it for |
|------|------------|
| `interior.pdf` | **Upload to KDP as the manuscript.** 8.5 × 11 in, 252 pages, fonts embedded |
| `cover-wrap.pdf` | **Upload to KDP as the cover.** Back + spine + front, with 0.125 in bleed |
| `cover-wrap-flattened.pdf` | The same cover as one 300-dpi picture. Use it if KDP complains about transparency or fonts |
| `front-cover.jpg` and `.png` | Just the front cover, for your Amazon page, social posts, or a website |
| `cover-template-guides.pdf` / `.png` | Your cover with bleed, trim, safe zone, spine fold lines, and barcode area drawn on |
| `cover-template-blank.pdf` / `.png` | An empty template with the same guides, for designing a cover in another tool |

## How to rebuild

You'll need the tools in `requirements-pdf.txt` (Playwright and Chromium, plus PyMuPDF). In a terminal in this folder:

```
pip install -r requirements-pdf.txt
python -m playwright install chromium
python scripts/build_pdf.py --kdp --no-placeholders --out kdp/out/interior.pdf
python kdp/build_cover.py --pages 252
```

The cover script needs the **page count of the finished interior**, because the spine gets wider with every page. If you change the interior, check its page count and pass it to `--pages`.

### Options

| Option | Meaning |
|--------|---------|
| `build_pdf.py --kdp` | Print-on-demand interior: plain title page, copyright page, white backgrounds, no page number on the front pages, even page count |
| `build_pdf.py --no-placeholders` | Leave out the dashed "Screenshot:" boxes. Don't use this once you've added real screenshots to the chapters |
| `build_cover.py --ink bw` | Black-and-white interior (thinner spine). Also `standard-color` and `premium-color` (the default) |
| `build_cover.py --paper cream` | Cream paper (black-and-white only) |
| `build_cover.py --trim 6x9` | A different trim size. The cover changes, but the interior would need rebuilding at that size too |

## Cover specifications used

| Item | Value |
|------|-------|
| Trim size | 8.5 × 11 in |
| Bleed | 0.125 in on every outside edge |
| Spine | pages × 0.002347 in (premium color, white paper) = **0.591 in** at 252 pages |
| Full cover size | **17.841 × 11.250 in** (5,352 × 3,375 px at 300 dpi) |
| Safe zone | Text and faces stay 0.375 in inside the trim edge (KDP's minimum is 0.25 in) |
| Barcode | A clear 2 × 1.2 in area in the lower right of the back cover. KDP places the ISBN barcode there |
| Spine text | Included, because KDP allows it above 79 pages |

> KDP's spine-width numbers and rules can change. Before you upload, use KDP's **Cover Calculator** (on kdp.amazon.com) with your page count and print options, and confirm the width and height match `Full cover size` above. If they don't, pass the right numbers to `build_cover.py`.

## Uploading to KDP

1. Sign in at <https://kdp.amazon.com> and choose **Create → Paperback**.
2. Paste the title, subtitle, author, description, keywords, and categories from `book-info.md`.
3. Choose **ISBN**, then **Print options**: white paper, premium color, 8.5 × 11 in, bleed, and your preferred cover finish.
4. Upload `interior.pdf` as the manuscript.
5. Upload `cover-wrap.pdf` as the cover (choose "I have a print-ready PDF cover").
6. Open **Launch Previewer**. Check every page, and check that nothing important is near an edge or the spine.
7. Order a **proof copy** before you publish.

## Changing the design

The cover is plain HTML and CSS inside `build_cover.py` (look for `cover_html`). Edit it, rebuild, and look at `out/cover-wrap.pdf`. The book's title, subtitle, author, and tagline live in `scripts/guide.py`, so the cover, the title page, and the copyright page always agree.

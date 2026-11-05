"""Markdown -> .docx for the thesis pack. Usage: python md2docx.py OUT_DIR "src.md::Name.docx::P|L" ... (P portrait, L landscape). Needs python-docx."""
import re, sys
from pathlib import Path
from docx import Document
from docx.shared import Pt, Cm
from docx.enum.section import WD_ORIENT

INLINE = re.compile(r"(\*\*(?:[^*]|\*(?!\*))+\*\*|\*[^*\s][^*]*\*|`[^`]+`|\[[^\]]+\]\([^)]+\))")


def add_inline(par, text, size=None):
    text = text.replace("***", "**")
    for part in INLINE.split(text):
        if not part:
            continue
        if part.startswith("**") and part.endswith("**"):
            r = par.add_run(part[2:-2].replace("*", "")); r.bold = True
        elif part.startswith("`") and part.endswith("`"):
            r = par.add_run(part[1:-1]); r.font.name = "Consolas"
        elif part.startswith("[") and "](" in part:
            r = par.add_run(part[1:part.index("](")])
        elif part.startswith("*") and part.endswith("*") and len(part) > 2:
            r = par.add_run(part[1:-1]); r.italic = True
        else:
            r = par.add_run(part)
        if size:
            r.font.size = Pt(size)


def convert(src, dst, landscape=False):
    doc = Document()
    st = doc.styles["Normal"]; st.font.name = "Calibri"; st.font.size = Pt(11)
    sec = doc.sections[0]
    if landscape:
        sec.orientation = WD_ORIENT.LANDSCAPE
        sec.page_width, sec.page_height = sec.page_height, sec.page_width
    for side in ("left_margin", "right_margin", "top_margin", "bottom_margin"):
        setattr(sec, side, Cm(2))
    lines = Path(src).read_text(encoding="utf-8").splitlines()
    i = 0
    while i < len(lines):
        ln = lines[i]
        s = ln.strip()
        if s.startswith("```"):
            i += 1
            while i < len(lines) and not lines[i].strip().startswith("```"):
                p = doc.add_paragraph(); r = p.add_run(lines[i]); r.font.name = "Consolas"; r.font.size = Pt(8.5)
                p.paragraph_format.space_after = Pt(0)
                i += 1
            i += 1; continue
        if s.startswith("|"):
            rows = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
                if not all(re.fullmatch(r":?-{2,}:?", c) for c in cells if c):
                    rows.append(cells)
                i += 1
            ncol = max(len(r) for r in rows)
            t = doc.add_table(rows=len(rows), cols=ncol); t.style = "Table Grid"
            for ri, row in enumerate(rows):
                for ci in range(ncol):
                    cell = t.cell(ri, ci); cell.text = ""
                    add_inline(cell.paragraphs[0], row[ci] if ci < len(row) else "", size=9)
                    if ri == 0:
                        for r in cell.paragraphs[0].runs: r.bold = True
            doc.add_paragraph()
            continue
        m = re.match(r"^(#{1,6})\s+(.*)", s)
        if m:
            h = doc.add_heading(level=min(len(m.group(1)), 4)); add_inline(h, m.group(2))
        elif s in ("---", "***"):
            pass
        elif s.startswith(">"):
            p = doc.add_paragraph(); p.paragraph_format.left_indent = Cm(1)
            add_inline(p, s.lstrip(">").strip()); [setattr(r, "italic", True) for r in p.runs]
        elif re.match(r"^[-*]\s+", s):
            indent = (len(ln) - len(ln.lstrip())) // 2
            p = doc.add_paragraph(style="List Bullet" if indent == 0 else "List Bullet 2")
            add_inline(p, re.sub(r"^[-*]\s+(\[[ x]\]\s+)?", lambda mm: "☐ " if mm.group(1) and "x" not in mm.group(1) else ("☑ " if mm.group(1) else ""), s))
        elif re.match(r"^\d+\.\s+", s):
            indent = (len(ln) - len(ln.lstrip())) // 2
            p = doc.add_paragraph(style="List Number" if indent == 0 else "List Number 2")
            add_inline(p, re.sub(r"^\d+\.\s+", "", s))
        elif s:
            p = doc.add_paragraph(); add_inline(p, s)
        i += 1
    doc.save(dst)


if __name__ == "__main__":
    out = Path(sys.argv[1]); out.mkdir(parents=True, exist_ok=True)
    for spec in sys.argv[2:]:
        src, name, orient = spec.split("::")
        convert(src, out / name, landscape=(orient == "L"))
        print("wrote", out / name)

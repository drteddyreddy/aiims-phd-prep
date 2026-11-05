"""Render extract_rows.py JSON into verification-table markdown (summary rows + per-paper detail).

Usage: python render_rows.py EXTRACT_DIR START_NUM stem1[:TAG] stem2[:TAG] ... > out.md
"""
import json, sys
from pathlib import Path

d, n0, items = Path(sys.argv[1]), int(sys.argv[2]), sys.argv[3:]
SUMMARY = ["design", "n", "population_and_timing_after_detox", "parameters", "sham_or_control",
           "primary_result_with_effect_size_and_ci"]
DETAIL = [("Design", "design"), ("N", "n"), ("Population and timing after detox", "population_and_timing_after_detox"),
          ("Stimulation or intervention parameters", "parameters"), ("Sham/control method", "sham_or_control"),
          ("Primary outcome and instrument", "primary_outcome_and_instrument"),
          ("Primary result with effect size and CI", "primary_result_with_effect_size_and_ci"),
          ("Secondary results", "secondary_results"), ("Follow-up", "follow_up"),
          ("Adverse events", "adverse_events"), ("Risk-of-bias notes", "risk_of_bias_notes")]
cell = lambda s, k=160: s.replace("|", "/").replace("\n", " ")[:k] + (" …" if len(s) > k else "")
rows, details = [], []
for i, it in enumerate(items):
    stem, _, tag = it.partition(":")
    j = json.loads((d / f"{stem}.json").read_text(encoding="utf-8"))
    m = j["_meta"]; tag = tag or m["tag"]; num = n0 + i
    v = lambda k: (j.get(k) or {}).get("value", "NR") if isinstance(j.get(k), dict) else str(j.get(k, "NR"))
    rows.append(f"| {num} | {cell(v('citation'), 90)} | " + " | ".join(cell(v(k)) for k in SUMMARY) + f" | {tag} |")
    det = [f"### {num}. {v('citation')}", "",
           f"Source: `{m['source']}` | Tag: **{tag}** | Quotes verified: {m['quotes_ok']}/{m['quotes_ok'] + m['quotes_missed']}", "",
           "**What this changes in the pack:** _see REPORT-2_", "", "| Field | Extracted |", "|---|---|"]
    det += [f"| {lab} | {cell(v(k), 2000)} |" for lab, k in DETAIL]
    fp = v("full_parameters")
    if fp and fp != "NR":
        det += ["", "Full parameters", "", "| Item | Detail |", "|---|---|"]
        for part in fp.split(";"):
            a, _, b = part.partition(":")
            if a.strip(): det.append(f"| {cell(a.strip(), 80)} | {cell(b.strip(), 400)} |")
    details.append("\n".join(det))
print("\n".join(rows)); print(); print("\n\n".join(details))

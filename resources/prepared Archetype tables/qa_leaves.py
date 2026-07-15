#!/usr/bin/env python3
"""Independent verification of the archetype leaf inventory.

This script does NOT import the generator. It re-parses the source ADL files with
its own implementation and cross-checks every prepared/<id>.md against that parse
and against the file's own header counts.

Run:  python qa_leaves.py        Exit 0 = all hard checks pass, 1 = a discrepancy.
Writes qa_report.txt.
"""
import re
import sys
from collections import Counter
from pathlib import Path

BASE = Path(__file__).resolve().parent
SOURCE_DIR = BASE / "archetypesMapped"
PREPARED_DIR = BASE / "preparedArchetypes"

NODE_HEADER = re.compile(r'(?m)^\t*(?P<slot>allow_archetype\s+)?(?P<rm_type>[A-Z][A-Z_]+)\[(?P<code>(?:at|id)\d+(?:\.\d+)?)\]')
VALUE_DATATYPE = re.compile(r'\b(?:C_)?(DV_[A-Z_]+)\b')
ORDINAL_VALUE = re.compile(r'-?\d+\|\[local::')
SLOT_INCLUDE = re.compile(r'archetype_id/value\s+matches\s*\{\s*/(.*?)/\s*\}')
ARCHETYPE_ID = re.compile(r'(openEHR-EHR-[A-Z_]+\.[\w.-]+\.v\d+)')
INLINE_LABEL = re.compile(r'--\s*(.*?)\s*$')

EXTENSION_LABELS = {"extension", "extension slot"}
VALID_DATATYPE = re.compile(r'^DV_[A-Z_]+$')


# ---------------------------------------------------------------- source parse

def definition_block(text):
    lines = text.splitlines()
    start = None
    for i, line in enumerate(lines):
        keyword = line.rstrip()
        if keyword == "definition":
            start = i + 1
        elif start is not None and keyword in ("ontology", "rules", "terminology"):
            return "\n".join(lines[start:i])
    return "\n".join(lines[start:]) if start is not None else ""


def value_type(element_text):
    match = re.search(r'value\s+matches\s*\{', element_text)
    if not match:
        return "any"
    open_brace = match.end() - 1
    depth = 0
    close_brace = open_brace
    for pos in range(open_brace, len(element_text)):
        if element_text[pos] == '{':
            depth += 1
        elif element_text[pos] == '}':
            depth -= 1
            if depth == 0:
                close_brace = pos
                break
    inner = element_text[open_brace + 1:close_brace]
    if inner.strip() in ('*', ''):
        return "any"
    hits = [(m.start(), m.group(1)) for m in VALUE_DATATYPE.finditer(inner)]
    ordinal = ORDINAL_VALUE.search(inner)
    if ordinal:
        hits.append((ordinal.start(), "DV_ORDINAL"))
    ordered = []
    for _, datatype in sorted(hits):
        if datatype not in ordered:
            ordered.append(datatype)
    return " / ".join(ordered) if ordered else "any"


def archetype_id(path):
    head = path.read_text(encoding="utf-8", errors="replace")[:400]
    match = ARCHETYPE_ID.search(head)
    return match.group(1) if match else path.stem


def parse_source(path):
    """Independent parse -> (elements, slots, structural_counter, extension_count).

    elements: list of (code, label, value_type);  slots: list of (code, label, allowed).
    """
    block = definition_block(path.read_text(encoding="utf-8", errors="replace"))
    headers = list(NODE_HEADER.finditer(block))
    elements, slots, structural, extensions = [], [], Counter(), 0

    for i, node in enumerate(headers):
        rm_type, code = node.group("rm_type"), node.group("code")
        end_of_line = block.find("\n", node.end())
        header_line = block[node.end():end_of_line if end_of_line != -1 else len(block)]
        label_match = INLINE_LABEL.search(header_line)
        label = (label_match.group(1) if label_match else "").lstrip("*").strip()
        body = block[node.start():headers[i + 1].start() if i + 1 < len(headers) else len(block)]

        if node.group("slot"):
            if label.lower() in EXTENSION_LABELS:
                extensions += 1
                continue
            include = SLOT_INCLUDE.search(body)
            allowed = include.group(1).replace("\\", "") if include else ""
            slots.append((code, label, "any archetype" if allowed in ('.*', '') else allowed))
        elif rm_type == "ELEMENT":
            elements.append((code, label, value_type(body)))
        else:
            structural[rm_type] += 1

    return elements, slots, structural, extensions


# ---------------------------------------------------------------- md parse

def parse_markdown(path):
    """Parse a generated md -> (header_counts, element_rows, slot_rows, malformed_rows)."""
    text = path.read_text(encoding="utf-8")
    header = re.search(r'\*\*Element leaves:\*\* (\d+).*?\*\*Cluster slot leaves:\*\* (\d+)', text)
    counts = (int(header.group(1)), int(header.group(2))) if header else (None, None)

    elements, slots, malformed = [], [], []
    section = None
    for line in text.splitlines():
        if line.startswith("## Element leaves"):
            section = "element"
        elif line.startswith("## Cluster slot leaves"):
            section = "slot"
        elif line.startswith("|") and set(line.strip()) != {"|", "-"} and not line.startswith("| Code"):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            target = elements if section == "element" else slots
            (target if len(cells) == 3 else malformed).append(cells)
    return counts, elements, slots, malformed


# ---------------------------------------------------------------- comparison

def allowed_as_set(allowed):
    """Archetype ids a slot accepts, as a set (separator-agnostic: handles '|' and ' / ')."""
    allowed = allowed.strip()
    if allowed == "any archetype":
        return frozenset({"any archetype"})
    return frozenset(part.strip() for part in re.split(r'\s*/\s*|\|', allowed) if part.strip())


def check_archetype(arch_id, source_path, md_path):
    """Return (issues, warnings) for one archetype."""
    issues, warnings = [], []
    src_elements, src_slots, _, _ = parse_source(source_path)
    counts, md_elements, md_slots, malformed = parse_markdown(md_path)

    for row in malformed:
        issues.append(f"[table] {arch_id}: row does not have 3 columns: {row}")

    if counts != (len(src_elements), len(src_slots)):
        issues.append(f"[count] {arch_id}: md header {counts} != source "
                      f"(elements={len(src_elements)}, slots={len(src_slots)})")
    if len(md_elements) != len(src_elements):
        issues.append(f"[count] {arch_id}: md element rows {len(md_elements)} != source {len(src_elements)}")
    if len(md_slots) != len(src_slots):
        issues.append(f"[count] {arch_id}: md slot rows {len(md_slots)} != source {len(src_slots)}")

    source_elements = {tuple(e) for e in src_elements}
    markdown_elements = {(r[0], r[1], r[2]) for r in md_elements}
    for missing in sorted(source_elements - markdown_elements):
        issues.append(f"[element] {arch_id}: in source but not md: {missing}")
    for extra in sorted(markdown_elements - source_elements):
        issues.append(f"[element] {arch_id}: in md but not source: {extra}")

    source_slots = {(c, l, allowed_as_set(a)) for c, l, a in src_slots}
    markdown_slots = {(r[0], r[1], allowed_as_set(r[2])) for r in md_slots}
    if source_slots != markdown_slots:
        issues.append(f"[slot] {arch_id}: slot set differs between source and md")

    for row in md_slots:
        if row[1].strip().lower() in EXTENSION_LABELS:
            issues.append(f"[extension] {arch_id}: Extension slot leaked into md: {row}")

    for row in md_elements:
        for token in (t.strip() for t in row[2].split("/")):
            if token != "any" and not VALID_DATATYPE.match(token):
                issues.append(f"[valuetype] {arch_id}: invalid value token '{token}' in {row}")

    codes = [r[0] for r in md_elements] + [r[0] for r in md_slots]
    repeated = sorted(code for code, n in Counter(codes).items() if n > 1)
    if repeated:
        warnings.append(f"[repeated-code] {arch_id}: code(s) {repeated} appear on multiple leaves "
                        f"(a repeated sub-structure flattened; disambiguate via parent cluster)")

    return issues, warnings


# ---------------------------------------------------------------- report

def totals(source_files, ids):
    elements = slots = extensions = 0
    structural = Counter()
    value_types = Counter()
    raw_nodes = 0
    for arch_id in ids:
        src_elements, src_slots, src_structural, ext = parse_source(source_files[arch_id])
        elements += len(src_elements)
        slots += len(src_slots)
        extensions += ext
        structural += src_structural
        value_types.update(vt for _, _, vt in src_elements)
        raw_nodes += len(list(NODE_HEADER.finditer(
            definition_block(source_files[arch_id].read_text(encoding="utf-8", errors="replace")))))
    return elements, slots, extensions, structural, value_types, raw_nodes


def main():
    source_files = {archetype_id(p): p for p in SOURCE_DIR.rglob("*.adl")}
    md_files = {p.stem: p for p in PREPARED_DIR.glob("*.md") if p.name != "00_INDEX.md"}

    issues, warnings = [], []
    for missing in sorted(set(source_files) - set(md_files)):
        issues.append(f"[coverage] source has no md: {missing}")
    for orphan in sorted(set(md_files) - set(source_files)):
        issues.append(f"[coverage] md has no source: {orphan}")

    shared_ids = sorted(set(source_files) & set(md_files))
    for arch_id in shared_ids:
        file_issues, file_warnings = check_archetype(arch_id, source_files[arch_id], md_files[arch_id])
        issues += file_issues
        warnings += file_warnings

    elements, slots, extensions, structural, value_types, raw_nodes = totals(source_files, shared_ids)
    accounted = elements + slots + extensions + sum(structural.values())
    if raw_nodes != accounted:
        issues.append(f"[conservation] raw nodes {raw_nodes} != elements+slots+extension+structural {accounted}")

    report = [
        "# QA REPORT (independent re-parse vs prepared/*.md)",
        f"Archetypes checked: {len(shared_ids)}",
        f"Element leaves: {elements}",
        f"Cluster slot leaves (Extension excluded): {slots}",
        f"Total leaves: {elements + slots}",
        f"Extension slots excluded: {extensions}",
        f"Structural container nodes dropped: {sum(structural.values())}  {dict(structural.most_common())}",
        f"Raw source node headers: {raw_nodes}  (conservation {'OK' if raw_nodes == accounted else 'FAIL'})",
        "",
        "## Value-type distribution (element leaves)",
    ]
    report += [f"{count:5d}  {datatype}" for datatype, count in sorted(value_types.items(), key=lambda kv: -kv[1])]
    report.append(f"\nSUM value-type counts: {sum(value_types.values())} "
                  f"(== element leaves {elements}: {sum(value_types.values()) == elements})")
    report.append("")
    report.append(f"## WARNINGS (informational): {len(warnings)}")
    report += warnings or ["(none)"]
    report.append("")
    report.append(f"## ISSUES (hard failures): {len(issues)}")
    report += issues or ["(none)"]

    text = "\n".join(report)
    (BASE / "qa_report.txt").write_text(text, encoding="utf-8")
    print(text)
    print("\n---\nwrote qa_report.txt")
    return 1 if issues else 0


if __name__ == "__main__":
    sys.exit(main())

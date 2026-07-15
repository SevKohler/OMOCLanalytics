#!/usr/bin/env python3
"""Extract the data leaves of each openEHR archetype into a plain markdown table.

A "leaf" is either:
  - a data ELEMENT (an actual data point, with its value datatype), or
  - a CLUSTER slot (a plug-in point where other archetypes may be attached).

Structural container nodes (the root ENTRY/CLUSTER node, HISTORY, EVENT, ITEM_TREE,
ACTIVITY, ISM_TRANSITION, internal grouping CLUSTERs) carry no data and are dropped.
The generic openEHR "Extension" slot is skipped as boilerplate.

HOW A LEAF IS DISCOVERED
------------------------
1. Scan only the `definition` section (definition_lines); all metadata is ignored.
2. Match each node header (NODE_HEADER): an RM type in CAPS + a bracketed code, e.g.
   `ELEMENT[at0004]  -- Weight` or `allow_archetype CLUSTER[at0020]  -- Device`.
3. Classify by RM type (not by tree depth):
       ELEMENT                      -> element leaf
       allow_archetype (a slot)     -> slot leaf   (except label "Extension" = skip)
       anything else                -> structural container, dropped
4. Enrich: element -> datatype from its `value matches { }` block (CHOICE -> "A / B");
   slot -> archetypes it accepts, from its `include ... archetype_id` line.

Reads:  used/**/*.adl        Writes: prepared/<archetype-id>.md  +  prepared/00_INDEX.md
Deterministic: same input always yields byte-identical output.
Verify separately with qa_leaves.py (an independent re-parse + cross-check).
"""
import re
from collections import namedtuple
from pathlib import Path

BASE = Path(__file__).resolve().parent
SOURCE_DIR = BASE / "archetypesMapped"
OUTPUT_DIR = BASE / "preparedArchetypes"

# A node header line, e.g. "\t\tELEMENT[at0004] ... -- Weight" or "allow_archetype CLUSTER[at0020] ...".
NODE_HEADER = re.compile(r'^(?P<indent>\t*)(?P<slot>allow_archetype\s+)?(?P<rm_type>[A-Z][A-Z_]+)\[(?P<code>(?:at|id)\d+(?:\.\d+)?)\]')
INLINE_LABEL = re.compile(r'--\s*(.*?)\s*$')            # the human label after "--"
VALUE_DATATYPE = re.compile(r'\b(?:C_)?(DV_[A-Z_]+)\b')  # DV_TEXT, C_DV_QUANTITY -> DV_QUANTITY, ...
ORDINAL_VALUE = re.compile(r'-?\d+\|\[local::')          # ADL shorthand for a DV_ORDINAL value
SLOT_INCLUDE = re.compile(r'archetype_id/value\s+matches\s*\{\s*/(.*?)/\s*\}')
ARCHETYPE_ID = re.compile(r'(openEHR-EHR-[A-Z_]+\.[\w.-]+\.v\d+)')
CONCEPT_TEXT = re.compile(r'concept\s*\n\s*\[(?:at|id)\d+(?:\.\d+)?\]\s*--\s*(.*)')

EXTENSION_LABELS = {"extension", "extension slot"}

Element = namedtuple("Element", "code label value_type")
Slot = namedtuple("Slot", "code label allowed")
Archetype = namedtuple("Archetype", "id concept category elements slots")


def definition_lines(text):
    """The lines of the archetype's `definition` section (up to the next top-level keyword)."""
    lines = text.splitlines()
    start = None
    for i, line in enumerate(lines):
        keyword = line.rstrip()
        if keyword == "definition":
            start = i + 1
        elif start is not None and keyword in ("ontology", "rules", "terminology"):
            return lines[start:i]
    return lines[start:] if start is not None else []


def clean_label(raw):
    """Strip the openEHR translation marker ('*') and surrounding whitespace."""
    return raw.lstrip("*").strip()


def element_value_type(element_text):
    """The datatype(s) inside the element's `value matches { }` braces.

    Only the value block is inspected, so datatypes used in sibling constraints
    (name, null_flavour) are ignored. A CHOICE of datatypes is joined with ' / '.
    """
    match = re.search(r'value\s+matches\s*\{', element_text)
    if not match:
        return "any"
    open_brace = match.end() - 1
    depth = 0
    close_brace = open_brace
    for pos in range(open_brace, len(element_text)):
        char = element_text[pos]
        if char == '{':
            depth += 1
        elif char == '}':
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

    ordered_unique = []
    for _, datatype in sorted(hits):
        if datatype not in ordered_unique:
            ordered_unique.append(datatype)
    return " / ".join(ordered_unique) if ordered_unique else "any"


def slot_allowed_archetypes(block, header_index):
    """Human-readable list of archetypes a slot accepts (alternatives joined with ' / ')."""
    raw = ""
    for line in block[header_index + 1:header_index + 8]:
        include = SLOT_INCLUDE.search(line)
        if include:
            raw = include.group(1)
            break
        if NODE_HEADER.match(line):
            break
    unescaped = raw.replace("\\", "")
    if unescaped in (".*", ""):
        return "any archetype"
    # ADL joins alternative ids with '|'; ' / ' keeps the markdown table cell intact.
    return unescaped.replace("|", " / ")


def element_body(block, header_index):
    """The element's own lines, from its header down to (but not including) the next node."""
    body = []
    for line in block[header_index + 1:]:
        if NODE_HEADER.match(line):
            break
        body.append(line)
    return "\n".join(body)


def find_first(pattern, text, default=""):
    match = pattern.search(text)
    return match.group(1).strip() if match else default


def parse_archetype(path, category):
    text = path.read_text(encoding="utf-8", errors="replace")
    archetype_id = find_first(ARCHETYPE_ID, "\n".join(text.splitlines()[:5]), default=path.stem)
    concept = find_first(CONCEPT_TEXT, text)

    block = definition_lines(text)
    elements, slots = [], []
    for i, line in enumerate(block):
        node = NODE_HEADER.match(line)
        if not node:
            continue
        code = node.group("code")
        label_match = INLINE_LABEL.search(line)
        label = clean_label(label_match.group(1) if label_match else "")

        if node.group("slot"):
            if label.lower() in EXTENSION_LABELS:
                continue
            slots.append(Slot(code, label, slot_allowed_archetypes(block, i)))
        elif node.group("rm_type") == "ELEMENT":
            elements.append(Element(code, label, element_value_type(element_body(block, i))))
        # every other RM type is a structural container -> not a leaf

    return Archetype(archetype_id, concept, category, elements, slots)


def render_markdown(arch):
    lines = [f"# {arch.id}\n"]
    if arch.concept:
        lines.append(f"**Concept:** {arch.concept}\n")
    lines.append(f"**Category:** {arch.category}\n")
    total = len(arch.elements) + len(arch.slots)
    lines.append(f"**Element leaves:** {len(arch.elements)}  |  **Cluster slot leaves:** {len(arch.slots)}  "
                 f"|  **Total leaves:** {total}\n")

    lines.append("\n## Element leaves\n")
    if arch.elements:
        lines.append("| Code | Element | Value type |")
        lines.append("|------|---------|------------|")
        lines += [f"| {e.code} | {e.label} | {e.value_type} |" for e in arch.elements]
    else:
        lines.append("_None._")

    lines.append("\n## Cluster slot leaves\n")
    if arch.slots:
        lines.append("| Code | Slot | Allowed archetypes |")
        lines.append("|------|------|--------------------|")
        lines += [f"| {s.code} | {s.label} | {s.allowed} |" for s in arch.slots]
    else:
        lines.append("_None._")

    lines.append("")
    return "\n".join(lines)


def render_index(archetypes):
    total_elements = sum(len(a.elements) for a in archetypes)
    total_slots = sum(len(a.slots) for a in archetypes)
    lines = [
        "# Archetype leaf inventory (used)\n",
        f"**Archetypes:** {len(archetypes)}  |  **Element leaves:** {total_elements}  "
        f"|  **Cluster slot leaves:** {total_slots}  |  **Total leaves:** {total_elements + total_slots}\n",
        "\nOne md per archetype lists its data ELEMENT leaves and its CLUSTER slot leaves. "
        "Structural container nodes (history/event/item_tree/root/grouping clusters) are excluded.\n",
        "\n| Archetype | Category | Concept | Elements | Slots | Leaves |",
        "|-----------|----------|---------|----------|-------|--------|",
    ]
    for a in sorted(archetypes):
        leaves = len(a.elements) + len(a.slots)
        lines.append(f"| [{a.id}]({a.id}.md) | {a.category} | {a.concept} | {len(a.elements)} | {len(a.slots)} | {leaves} |")
    lines.append("")
    return "\n".join(lines)


def category_of(path):
    """Folder path of the archetype relative to used/, e.g. 'entry/observation'."""
    parts = path.relative_to(SOURCE_DIR).parts[:-1]
    return "/".join(parts) if parts else "root"


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    archetypes = [parse_archetype(path, category_of(path)) for path in sorted(SOURCE_DIR.rglob("*.adl"))]

    for arch in archetypes:
        (OUTPUT_DIR / f"{arch.id}.md").write_text(render_markdown(arch), encoding="utf-8")
    (OUTPUT_DIR / "00_INDEX.md").write_text(render_index(archetypes), encoding="utf-8")

    elements = sum(len(a.elements) for a in archetypes)
    slots = sum(len(a.slots) for a in archetypes)
    print(f"Wrote {len(archetypes)} md files + 00_INDEX.md to {OUTPUT_DIR}")
    print(f"Totals: element_leaves={elements}, slot_leaves={slots}, total_leaves={elements + slots}")


if __name__ == "__main__":
    main()

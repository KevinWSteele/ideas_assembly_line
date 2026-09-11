"""Transcript parsing, with line numbers preserved so a digest can link back
to its source -- the prototype review flagged missing source traceability as
a must-fix, not a nice-to-have."""
import re


def split_into_agenda_items(text):
    """Return a list of dicts: {title, body, start_line, end_line}."""
    lines = text.splitlines()
    marker = re.compile(r"^AGENDA ITEM \d+:")
    starts = [i for i, line in enumerate(lines) if marker.match(line)]
    items = []
    for idx, start in enumerate(starts):
        end = starts[idx + 1] if idx + 1 < len(starts) else len(lines)
        title = lines[start].split(":", 1)[1].strip()
        body = "\n".join(lines[start + 1:end]).strip()
        items.append({
            "title": title,
            "body": body,
            "start_line": start + 1,  # 1-indexed, for human-facing "see source" links
            "end_line": end,
        })
    return items

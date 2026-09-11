#!/usr/bin/env python3
"""
Meeting Digest -- quick prototype.

Reads a plain-text meeting transcript, splits it into agenda-item topics, and
prints a short plain-language digest of each: what was discussed, what was
decided (if anything), and what happens next.

Two summarization modes:
  - OPENAI_API_KEY set  -> calls the OpenAI API for a nicer natural-language summary.
  - no key set          -> falls back to a simple rule-based summary (keyword
                            matching for votes/decisions), so this runs out of
                            the box with zero cost and zero setup for the demo.

This is a Stage 2 prototype: quick and rough on purpose. See example_prototype.md
for what's faked/simplified.
"""
import os
import re
import sys

TRANSCRIPT_PATH = sys.argv[1] if len(sys.argv) > 1 else os.path.join(
    os.path.dirname(__file__), "sample_transcript.txt"
)


def split_into_agenda_items(text):
    """Split the transcript into (title, body) chunks on "AGENDA ITEM N:" markers."""
    parts = re.split(r"\n(?=AGENDA ITEM \d+:)", text)
    items = []
    for part in parts:
        part = part.strip()
        if not part.startswith("AGENDA ITEM"):
            continue
        title_line, _, body = part.partition("\n")
        title = title_line.split(":", 1)[1].strip() if ":" in title_line else title_line
        items.append((title, body.strip()))
    return items


def summarize_rule_based(title, body):
    """Free, local, zero-dependency summary: pull out the decision/outcome by
    keyword rather than truly understanding the text. Crude, but honest about it."""
    outcome = None
    motion_match = re.search(r"Motion carries ([\d\-]+)", body)
    if motion_match:
        outcome = f"Passed ({motion_match.group(1)} vote)."
    elif "no vote" in body.lower() or "discussion only" in body.lower():
        outcome = "Discussion only, no vote taken tonight."

    next_step = None
    next_match = re.search(r"(report back|due back|bring a .* recommendation).{0,80}", body, re.IGNORECASE)
    if next_match:
        next_step = next_match.group(0).strip().rstrip(".") + "."

    return {
        "topic": title,
        "outcome": outcome or "No formal outcome recorded.",
        "next_step": next_step,
    }


def summarize_openai(title, body):
    """Higher-quality summary via the OpenAI API. Requires OPENAI_API_KEY and
    the `openai` package. Not exercised unless a key is present."""
    import openai  # local import: only required if this path is actually used

    client = openai.OpenAI(api_key=os.environ["OPENAI_API_KEY"])
    prompt = (
        "Summarize this city council agenda item in 1-2 plain-language sentences "
        "for a busy resident. State clearly whether it passed, failed, or was "
        "discussion-only, and what happens next if anything.\n\n"
        f"AGENDA ITEM: {title}\n\n{body}"
    )
    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
    )
    return {"topic": title, "outcome": resp.choices[0].message.content.strip(), "next_step": None}


def main():
    with open(TRANSCRIPT_PATH, "r", encoding="utf-8") as f:
        text = f.read()

    use_openai = bool(os.environ.get("OPENAI_API_KEY"))
    mode = "OpenAI API" if use_openai else "rule-based (free, local)"
    print(f"# Meeting Digest\n(summarization mode: {mode})\n")

    for title, body in split_into_agenda_items(text):
        if "call to order" in title.lower() or "adjournment" in title.lower():
            continue  # skip pure procedural items, nothing a resident needs from these
        summary = summarize_openai(title, body) if use_openai else summarize_rule_based(title, body)
        print(f"## {summary['topic']}")
        print(f"**Outcome:** {summary['outcome']}")
        if summary.get("next_step"):
            print(f"**Next step:** {summary['next_step']}")
        print()


if __name__ == "__main__":
    main()

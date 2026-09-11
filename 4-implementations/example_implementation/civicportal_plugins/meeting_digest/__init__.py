"""
Meeting Digest -- CivicPortal plugin (hypothetical integration).

Public interface a host application would call:

    from civicportal_plugins.meeting_digest import generate_digest

    digest = generate_digest(transcript_text, source_name="2026-03-03-council.txt",
                              backend="local_llm")

Imagined integration point: registered as a scheduled job in a larger
"CivicPortal" resident-notification platform that watches a
transcripts/incoming/ directory, runs each new transcript through this
plugin, and publishes the resulting digest to a public resident feed. None
of that host application needs to actually exist for this exercise --
this module is written as if it were being dropped into one.
"""
from .transcript import split_into_agenda_items
from .summarizers import BACKENDS

SKIP_TITLES = ("call to order", "adjournment")


def generate_digest(transcript_text, source_name="transcript", backend="local_llm", **backend_kwargs):
    """Returns a list of dicts, one per substantive agenda item:
    {topic, outcome, next_step, source_link}."""
    if backend not in BACKENDS:
        raise ValueError(f"Unknown backend '{backend}'. Choose from: {list(BACKENDS)}")
    summarizer = BACKENDS[backend](**backend_kwargs)

    digest = []
    for item in split_into_agenda_items(transcript_text):
        if any(skip in item["title"].lower() for skip in SKIP_TITLES):
            continue
        result = summarizer.summarize(item["title"], item["body"])
        digest.append({
            "topic": item["title"],
            "outcome": result["outcome"],
            "next_step": result.get("next_step"),
            "source_link": f"{source_name}#L{item['start_line']}-L{item['end_line']}",
        })
    return digest

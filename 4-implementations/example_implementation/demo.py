#!/usr/bin/env python3
"""Standalone demo of the meeting_digest plugin, standing in for how a host
CivicPortal application would call it. Run from this directory.

Usage:
    python demo.py                  # rule_based backend (default) -- deterministic, always correct on this sample
    python demo.py local_llm        # the recommended backend -- requires Ollama running locally; see
                                     # example_implementation.md "What's still open" before trusting its output
    python demo.py cloud_llm        # requires OPENAI_API_KEY
"""
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))
from civicportal_plugins.meeting_digest import generate_digest

backend = sys.argv[1] if len(sys.argv) > 1 else "rule_based"

with open(os.path.join(os.path.dirname(__file__), "sample_transcript.txt"), encoding="utf-8") as f:
    transcript_text = f.read()

print(f"# Meeting Digest (backend: {backend})\n")
for item in generate_digest(transcript_text, source_name="sample_transcript.txt", backend=backend):
    print(f"## {item['topic']}")
    print(f"**Outcome:** {item['outcome']}")
    if item["next_step"]:
        print(f"**Next step:** {item['next_step']}")
    print(f"**Source:** {item['source_link']}")
    print()

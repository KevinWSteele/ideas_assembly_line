> **📖 This is the worked example.** Illustrative only — read it for format, then build a prototype from a real idea instead. Previous stage: [`example_idea.md`](../1-ideas/example_idea.md). Next stage: [`example_review.md`](../3-reviews/example_review.md).

# Prototype: Meeting Digest

**Builds on:** [`1-ideas/example_idea.md`](../1-ideas/example_idea.md) — "Meeting Digest: plain-language summaries of local government meetings"

## What this demonstrates

That a plain meeting transcript can be automatically split into topics and turned into a short "what happened, what's next" digest, without needing any manual tagging of the source document.

## The fictionalized use case

A fully made-up transcript for a fictional "City of Anytown" council meeting ([`sample_transcript.txt`](example_prototype/sample_transcript.txt)), covering a routine vote, a substantive vote (a bike lane proposal), and a discussion-only item. No real municipality, real meeting, or real data is involved.

## What's in this prototype

A single Python script, [`digest.py`](example_prototype/digest.py), with two summarization paths:

- **Rule-based (default, free, runs with zero setup):** splits the transcript on `AGENDA ITEM` markers and uses keyword/regex matching (e.g. "Motion carries", "discussion only", "report back") to pull out the outcome and next step for each item.
- **OpenAI API (opt-in via `OPENAI_API_KEY`):** sends each agenda item to `gpt-4o-mini` for a proper natural-language summary instead of keyword matching.

The rule-based path is the one actually demoed here — it's what makes this runnable by anyone with no API key and no cost.

## How to run it

```
cd 2-prototypes/example_prototype
python digest.py
```

No dependencies required for the default path (standard library only). Output is printed straight to the terminal.

To try the OpenAI path instead: `pip install -r requirements.txt`, set `OPENAI_API_KEY`, then run the same command.

## Known limitations

- The rule-based mode only recognizes outcome phrasing that looks like this specific transcript's style ("Motion carries N-N", "discussion only"). A real transcript from an actual municipality would very likely use different phrasing and break the regex matching — this is the biggest open question for a reviewer to dig into.
- No handling yet for transcripts that aren't already clean text (real ones often start as PDFs or auto-captioned video).
- Procedural items (roll call, adjournment) are just skipped by keyword rather than genuinely understood as non-substantive.
- No links back to timestamps/source yet, which the original idea flagged as important for trust.

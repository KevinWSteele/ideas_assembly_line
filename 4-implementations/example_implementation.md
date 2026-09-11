> **📖 This is the worked example.** Illustrative only. Previous stage: [`example_review.md`](../3-reviews/example_review.md). This is the last stage — there's no further example after this one.

# Implementation: Meeting Digest

**Applies recommendations from:** [`3-reviews/example_review.md`](../3-reviews/example_review.md)

## What changed from the prototype

The review's central recommendation was to add a free, local-LLM summarization backend as a middle ground between the prototype's two options (fragile-but-free regex, and robust-but-paid cloud API). This implementation does that, and goes one step further: instead of picking one backend, it turns summarization into a **pluggable interface** with three interchangeable implementations (`rule_based`, `local_llm` via [Ollama](https://ollama.com), `cloud_llm` via OpenAI), selected by config rather than hardcoded. It also adds the source-traceability the original idea asked for: every digest item now links back to the exact line range in the source transcript it was summarized from.

## Hypothetical integration target

Imagined as a plugin inside a larger **CivicPortal** resident-notification platform (hypothetical — doesn't need to exist for this exercise): CivicPortal would run a scheduled job that watches a `transcripts/incoming/` directory, calls this plugin's `generate_digest()` on each new file, and publishes the result to a public resident-facing feed. The plugin's only contract with the host app is the `generate_digest(transcript_text, source_name, backend) -> list[dict]` function in [`civicportal_plugins/meeting_digest/__init__.py`](example_implementation/civicportal_plugins/meeting_digest/__init__.py) — CivicPortal wouldn't need to know anything about how summarization actually happens internally.

## What's in this implementation

```
civicportal_plugins/meeting_digest/
  __init__.py       <- public plugin interface: generate_digest()
  transcript.py      <- splits transcript into agenda items, tracks line numbers
  summarizers.py      <- RuleBasedSummarizer / LocalLLMSummarizer / CloudLLMSummarizer
demo.py              <- standalone runner standing in for how CivicPortal would call the plugin
sample_transcript.txt
```

## How to run it

```
cd 4-implementations/example_implementation
python demo.py                # rule_based backend, deterministic, no setup
python demo.py local_llm       # requires Ollama running locally with a model pulled
python demo.py cloud_llm       # requires: pip install -r requirements.txt, OPENAI_API_KEY set
```

## What's still open

**The most important finding from actually building this:** the `local_llm` backend was tested across several runs against the sample transcript. Most runs were accurate — genuinely better and more natural than the regex backend, exactly as the review predicted. But on one run, it summarized the discussion-only school-budget item as **"Passed (unanimous, no vote count given)"** — which is simply wrong; that item explicitly had no vote. This is real, observed evidence of exactly the risk the *original Stage 1 idea* flagged under "Open questions/risks": *"Summarization can misrepresent a close or contentious vote."* It's not solved by this implementation — it's a genuine open problem for whoever picks this up next. Concretely: `local_llm` is not yet trustworthy enough to publish unreviewed, and the demo defaults to `rule_based` specifically so it never shows a misleading result out of the box.

Other gaps:
- No automated check that an LLM-generated outcome is actually consistent with what the transcript said (e.g. cross-checking against the presence/absence of "Motion carries" as a sanity check, regardless of backend used).
- Only tested against one fictional transcript — real municipal transcripts (and their formatting quirks) haven't been tried.
- No caching — re-running the same transcript re-summarizes it from scratch every time, which matters more once `cloud_llm` is in the mix (a per-call cost) than it does for `rule_based` or `local_llm`.

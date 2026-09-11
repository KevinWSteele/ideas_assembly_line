> **📖 This is the worked example.** Illustrative only. Previous stage: [`example_prototype.md`](../2-prototypes/example_prototype.md). Next stage: [`example_implementation.md`](../4-implementations/example_implementation.md).

# Review: Meeting Digest prototype

**Reviewing:** [`2-prototypes/example_prototype.md`](../2-prototypes/example_prototype.md)

## Reproduction

- [x] I was able to reproduce the claimed result
- [ ] I was **not** able to reproduce it

Ran exactly the documented steps:

```
cd 2-prototypes/example_prototype
python digest.py
```

Got a three-item digest correctly identifying the routine vote, the bike lane vote (with its 4-0 outcome and the six-month follow-up), and the discussion-only budget item — matching what the write-up claims. No dependencies needed, no errors. I didn't test the `OPENAI_API_KEY` path since I didn't want to spend money on this review; noting that as a gap below.

## Stack and dependencies

- Default path: pure Python 3 standard library (`re`, `os`, `sys`). No install step, no account, no cost. This part is already about as lean as it gets.
- Optional path: `openai` Python package + an OpenAI API key. This is a paid, metered, internet-dependent external service — every digest generated this way costs money and requires an account.

## Could this be leaner?

The free path is already free — the real question is whether it's good *enough*, and I don't think it is yet. It only recognizes outcomes phrased almost exactly like this sample transcript ("Motion carries N-N", "discussion only"). Real municipal transcripts vary a lot in phrasing, so this will silently produce "No formal outcome recorded" on plenty of real meetings rather than actually failing loudly — that's a quiet-failure risk worth flagging directly.

The OpenAI path would handle phrasing variation far better, but at a real per-use cost and an external dependency — a meaningful downside for something meant to run regularly and for free on public meeting archives.

**Recommendation:** a small **local** LLM (e.g. via [Ollama](https://ollama.com) running something like `llama3.2:3b` or `phi3`) would likely be the sweet spot — no per-use cost, no API key, no data leaving the machine, and meaningfully more robust to phrasing variation than regex matching. It's a heavier install than the current zero-dependency script (needs Ollama installed and a model pulled once), but no ongoing cost or account. Worth prototyping as an alternate summarization backend before assuming the OpenAI path is the only way to get past the regex approach's fragility.

## Other notes

- The "known limitations" section in the prototype write-up already correctly identifies the phrasing-fragility issue and the missing source-timestamp links — an implementation should treat both as must-fix, not nice-to-have, given the original idea's emphasis on residents being able to verify anything that matters to them.
- Worth testing against a real (not fictional) public transcript from an actual city before going further, to see how much phrasing really does vary in practice.

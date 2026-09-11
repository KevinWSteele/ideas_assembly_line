> **📖 This is the worked example.** It's illustrative only, not a real proposal — read it to see the expected format, then write your own idea rather than building on this one. Next stage: [`example_prototype.md`](../2-prototypes/example_prototype.md).

# Meeting Digest: plain-language summaries of local government meetings

**Target user:** A resident of a small city who cares about local decisions (zoning, school budgets, a new bike lane) but doesn't have two hours to watch or read the full transcript of a city council meeting.

## The problem

City council, school board, and planning commission meetings are open to the public and often recorded or transcribed — but the raw video or transcript is long, jargon-heavy, and organized around a meeting's procedural agenda rather than around "what actually got decided." Most residents never find out a decision affecting them happened until well after the fact, not because the information was hidden, but because nobody had time to read it.

## The proposed idea

A tool that takes a public meeting transcript (or video-to-text transcript) as input and produces a short, plain-language digest: what was discussed, what was decided, who voted which way, and what happens next — organized by topic, not by agenda item number. A resident could skim a 3-minute digest instead of a 2-hour transcript and still know what actually changed.

Roughly: ingest a transcript → identify discussion topics and decision points → summarize each in plain language → output a short digest, ideally with timestamps/links back to the source so a reader can verify anything that matters to them.

## Why this seems promising

- The raw input (meeting transcripts/minutes) is usually already public record — no new data collection needed.
- This doesn't require real-time attendance or any special access — it can run entirely on existing public recordings after the fact.
- "Summarize a long document" is a well-trodden technical problem; the genuinely useful part is choosing the right structure (topic + decision + next step) for *this* kind of document.

## Open questions / risks

- Summarization can misrepresent a close or contentious vote if it's not careful — accuracy and traceability back to the source matter more here than in a generic summarizer.
- Transcript quality varies a lot by municipality; some don't have one at all yet, only meeting minutes PDFs.
- Worth thinking about early: does this need a paid AI API, or can it work with something free/local? (Good question for whoever reviews the prototype.)

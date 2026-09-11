# Stage 3: Reviews

Evaluate a prototype from [`2-prototypes/`](../2-prototypes/) with a critical eye.

**What goes here:** a written review answering three questions about a specific prototype:

1. **Does it actually work?** Did you follow the prototype's own "How to run it" steps and get the claimed result? Say exactly what you did and what happened, including if it didn't work.
2. **What's it built on?** What languages, frameworks, libraries, and external services (especially paid ones) does it depend on?
3. **Could it be leaner?** Is there a simpler, cheaper, faster, or free way to get the same result? This is the most valuable part of a review — be specific and practical, not just "yes, probably."

This is a written evaluation, not new code — though a few lines showing an alternative approach are welcome if they help make your point.

**Who can contribute:** anyone. You don't need deep expertise — a careful, honest attempt to reproduce the result and think about the tradeoffs is exactly what this stage needs. Fresh eyes are valuable here specifically because you *don't* have context on why the prototype was built the way it was.

**How to contribute:**
1. Pick a prototype from `2-prototypes/`.
2. Actually try to run it. This is the whole point of this stage — don't review from reading the code alone.
3. Copy [`TEMPLATE.md`](TEMPLATE.md) into a new file in this folder, named `review-<slug>.md`.
4. **Link to the specific prototype you reviewed, right at the top.**
5. Open a Pull Request (see the [root README](../README.md)).

**Worked example:** [`example_review.md`](example_review.md), reviewing [`../2-prototypes/example_prototype.md`](../2-prototypes/example_prototype.md).

Once your review is here, anyone can pick it up and build a refined implementation from it in [`4-implementations/`](../4-implementations/).

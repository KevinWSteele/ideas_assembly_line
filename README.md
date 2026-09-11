# Ideas Assembly Line

A self-service pipeline for turning "I have an idea" into a validated, buildable proposal — without needing permission, a meeting, or prior context on any existing project.

Built for the **DC Civic Tech × Unstuck Labs** event on **Friday, September 11, 2026**, and open for anyone to keep using afterward.

---

## The problem this solves

Volunteers show up wanting to help. But without deep context on a project, two things usually happen:

- They don't know **what** to work on.
- They're hesitant to touch a real, already-underway codebase they don't fully understand yet — reasonably, since a wrong move there has real cost.

The result: people leave without contributing, or a good idea they had never gets captured anywhere.

This repo fixes that by giving every level of contribution — *just an idea*, *a rough proof of concept*, *a critical review*, *a refined implementation* — its own dedicated, low-stakes space. You can jump in at whichever stage matches your skills and available time, work entirely on your own schedule, and never put an existing production codebase at risk, because nothing in here touches one.

---

## How it works: four stages, four folders

Work flows in one direction, stage to stage. Anyone can contribute at **any** stage, on **any** existing entry from the stage before it, at **any** time — there's no assignment process and no gatekeeper.

```
1-ideas/            →   2-prototypes/     →   3-reviews/        →   4-implementations/
"here's a concept"      "here's proof         "here's how to        "here's a refined
                          it can work"          make it better"        build of it"
```

| Stage | Folder | What you make | Who can make it |
|---|---|---|---|
| 1. Idea | [`1-ideas/`](1-ideas/) | A write-up proposing a tool/system for a **specific target user** | Anyone — no code required |
| 2. Prototype | [`2-prototypes/`](2-prototypes/) | A small proof-of-concept demonstrating the idea works, against a **fictional** use case | Anyone who picks up an idea |
| 3. Review | [`3-reviews/`](3-reviews/) | An honest evaluation of a prototype: does it reproduce, what's its stack, could it be leaner? | Anyone who picks up a prototype |
| 4. Implementation | [`4-implementations/`](4-implementations/) | A refined build that applies the review's recommendations | Anyone who picks up a review |

**Every entry after Stage 1 must contain a clear, visible hyperlink at the top of the file to the specific entry from the previous stage it's building on.** That's what keeps the whole chain traceable — anyone should be able to click backward from a Stage 4 implementation all the way to the original Stage 1 idea.

### Why this naturally filters for quality

Nothing advances a stage unless someone *chooses*, on their own initiative, to spend their time building on it. There is no approval step and no judge. That means:

- A weak idea just sits in `1-ideas/` with no prototype ever built against it — and that's fine, it cost nothing to write.
- An idea that reaches `4-implementations/` got there because **multiple different people, independently, each found it compelling enough to build on.**

The pipeline itself *is* the validation process. By the time something is a "Stage 4" entry, it's been organically vetted by real, voluntary effort at every step — not by committee.

### Why nothing here is risky

Every prototype and implementation in this repo targets a **fictionalized use case**. A Stage 4 implementation is written *as if* it were being refactored into a larger existing codebase — but that codebase doesn't have to actually exist anywhere for this exercise. Nobody's contribution can break real infrastructure, because nothing in this repo is connected to any.

---

## How to contribute

1. **Pick a stage.** Browse the folder for the stage below the one you want to contribute to (e.g., read `1-ideas/` before writing a prototype). Pick any entry that interests you — including ones that already have a prototype/review/implementation; parallel, competing attempts at the same stage are welcome and encouraged.
2. **Copy the template.** Each stage folder has a `TEMPLATE.md` — copy it into a new file in that same folder.
3. **Name your file clearly**, matching the pattern already used in that folder (see naming convention below) so people can tell at a glance what it's about and what it builds on.
4. **Link back.** At the very top of your file, link to the specific entry you're building on (skip this for new Stage 1 ideas — they're the start of a chain).
5. **Submit it:**
   - If you have write access to this repo, create a branch and open a Pull Request.
   - If you don't, fork the repo, add your file, and open a Pull Request from your fork.
   - At the in-person event, a maintainer may just merge these live as they come in — ask the room.
6. **That's it.** You don't need anyone's permission to start, and you don't need to finish something someone else started — pick it up, do what you can, and leave it for the next person.

### File naming convention

Use short, lowercase, hyphenated slugs that describe the idea, and keep the same slug as you move through stages so the family of related files is easy to spot:

```
1-ideas/idea-meeting-digest.md
2-prototypes/prototype-meeting-digest.md
2-prototypes/prototype-meeting-digest-alt-approach.md   <- a second, competing prototype is fine
3-reviews/review-meeting-digest.md
4-implementations/implementation-meeting-digest.md
```

If a stage already has multiple entries for the same idea, add a short suffix describing your specific angle (e.g., `-alt-approach`, `-no-api-version`) instead of overwriting someone else's file.

---

## See it in action: the worked example

Every folder contains an `example_*` file. Together they form one complete, start-to-finish walkthrough of the whole pipeline, using a single made-up idea, so you can see exactly what a good submission looks like at each stage before writing your own:

1. [`1-ideas/example_idea.md`](1-ideas/example_idea.md) — the original proposal
2. [`2-prototypes/example_prototype.md`](2-prototypes/example_prototype.md) — a proof of concept built from it
3. [`3-reviews/example_review.md`](3-reviews/example_review.md) — a review of that prototype
4. [`4-implementations/example_implementation.md`](4-implementations/example_implementation.md) — a refined implementation applying the review

These `example_*` files are illustrative only — not a real proposal — so they'll always stay in place as a reference. Don't build on them; pick a real entry instead.

---

## Questions at the event?

Ask in the room, or open an Issue on this repo — issues themselves are a fine, lightweight way to ask "is anyone already working on X?" before you start.

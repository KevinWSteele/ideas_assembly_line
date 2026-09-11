"""Pluggable summarization backends.

The Stage 3 review's core recommendation: don't force a choice between
"free but fragile regex" and "robust but paid API" -- add a free, local LLM
backend as a first-class third option. All three implement the same
interface so callers (and CivicPortal, hypothetically) can swap backends
via config with no other code changes.
"""
import os
import re
import urllib.request
import json


class Summarizer:
    def summarize(self, title, body):
        """Return {"outcome": str, "next_step": str | None}."""
        raise NotImplementedError


class RuleBasedSummarizer(Summarizer):
    """Free, zero-dependency, but only recognizes this transcript style's
    exact phrasing -- kept as the always-available fallback backend."""

    def summarize(self, title, body):
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

        return {"outcome": outcome or "No formal outcome recorded.", "next_step": next_step}


class LocalLLMSummarizer(Summarizer):
    """Free, runs entirely on-machine via Ollama (https://ollama.com). No
    per-use cost, no API key, no data leaves the machine -- the middle
    ground the review recommended between the regex and cloud-API backends."""

    def __init__(self, model="llama3.1:latest", host="http://127.0.0.1:11434"):
        self.model = model
        self.host = host

    def summarize(self, title, body):
        prompt = (
            "Summarize this city council agenda item for a busy resident. "
            "Respond with EXACTLY two lines, no extra commentary:\n"
            "OUTCOME: <one sentence -- passed/failed/discussion-only, with vote count if given>\n"
            "NEXT_STEP: <one short sentence on what happens next, or 'None'>\n\n"
            f"AGENDA ITEM: {title}\n\n{body}"
        )
        payload = json.dumps({
            "model": self.model,
            "prompt": prompt,
            "stream": False,
        }).encode("utf-8")
        req = urllib.request.Request(
            f"{self.host}/api/generate", data=payload,
            headers={"Content-Type": "application/json"},
        )
        with urllib.request.urlopen(req, timeout=60) as resp:
            result = json.loads(resp.read())
        text = result.get("response", "").strip()
        return self._parse(text)

    @staticmethod
    def _parse(text):
        """Local models don't reliably follow an exact output format run to
        run (seen in practice: "OUTCOME:" vs "Outcome:" vs "Next Step:" vs
        "NEXT_STEP:") -- match the label loosely (case/spacing/punctuation
        insensitive, optional markdown bold) instead of requiring one exact
        string, and degrade gracefully instead of failing outright."""
        outcome_match = re.search(
            r"\**outcome\**\s*:\s*(.+)", text, re.IGNORECASE)
        next_step_match = re.search(
            r"\**next[\s_]*step\**\s*:\s*(.+)", text, re.IGNORECASE)

        outcome = outcome_match.group(1).strip() if outcome_match else text.splitlines()[0].strip()
        next_step = next_step_match.group(1).strip() if next_step_match else None
        if next_step and next_step.lower().rstrip(".") == "none":
            next_step = None
        return {"outcome": outcome, "next_step": next_step}


class CloudLLMSummarizer(Summarizer):
    """Highest quality, but paid, metered, and requires an external account
    and an internet connection -- kept available but not the default,
    per the review."""

    def __init__(self, model="gpt-4o-mini"):
        self.model = model

    def summarize(self, title, body):
        import openai  # only imported if this backend is actually selected

        client = openai.OpenAI(api_key=os.environ["OPENAI_API_KEY"])
        prompt = (
            "Summarize this city council agenda item in 1-2 plain-language "
            "sentences for a busy resident, stating clearly whether it passed, "
            "failed, or was discussion-only, and what happens next if anything.\n\n"
            f"AGENDA ITEM: {title}\n\n{body}"
        )
        resp = client.chat.completions.create(model=self.model, messages=[{"role": "user", "content": prompt}])
        return {"outcome": resp.choices[0].message.content.strip(), "next_step": None}


BACKENDS = {
    "rule_based": RuleBasedSummarizer,
    "local_llm": LocalLLMSummarizer,
    "cloud_llm": CloudLLMSummarizer,
}

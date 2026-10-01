# AI Attribution and Cross-Model Review Policy

**Status: REQUIRED — owner directive**

This policy applies to every AI/LLM, coding agent, copilot, autonomous agent, and model-assisted tool that creates or materially changes GitHub content in this repository.

## 1. Exact model attribution is mandatory

Whenever AI materially creates or changes a GitHub artifact that supports attribution—including commits, pull requests, issues, releases, review comments, generated documentation, or similar records—the AI must identify the **exact model name and model number/version exposed to it**.

Do not use only a generic label such as "AI", "ChatGPT", "Claude", "Gemini", or "Copilot" when a more specific model identifier is available. Never invent a model version. If the exact version is not exposed, use the most specific available identifier and state that the exact version is unavailable.

### Commit trailers

Every commit materially authored by AI must include these trailers:

```text
AI-Model: <exact model name/version>
AI-Provider: <provider>
AI-Tool: <product/agent surface>
AI-Role: Author
```

If additional AI models materially contributed to the same commit, add one or more:

```text
AI-Contributor: <exact model name/version> | <provider> | <role>
```

Do not fabricate a human email address or misuse GitHub's `Co-authored-by` trailer to impersonate a model identity. Use the AI-specific trailers above.

## 2. AI-drafted pull requests require independent cross-model review

Every PR body must contain an **AI Participation** section declaring whether AI drafted or materially prepared the PR.

If `AI-Drafted: yes`:

1. The final PR diff must be reviewed by a **different model** from the drafting model before merge.
2. A different reasoning-effort setting or a second instance of the same underlying model does **not** count as another model.
3. Both the drafting and reviewing model names/versions must be recorded in the PR.
4. The reviewing model must review the current PR head commit. Record that exact SHA in `Review-Commit-SHA`.
5. Any material push after the review invalidates the prior cross-model review. The updated head must be reviewed again and the SHA updated.
6. The reviewing model should leave a GitHub review/comment when its tool access permits, identifying itself with `AI-Review-Model: <exact model>` and `Reviewed-Commit-SHA: <sha>`.
7. An AI-drafted PR must not be represented as ready for merge until the cross-model review is complete.

Required PR fields:

```text
AI-Drafted: yes|no
Drafting-Model: <exact model name/version or N/A>
Reviewing-Model: <different exact model name/version or N/A>
Cross-Model-Review: completed|not-required
Review-Commit-SHA: <reviewed head SHA or N/A>
```

## 3. Other GitHub artifacts

When AI materially drafts an issue, release note, review, architecture decision, generated report, or other GitHub artifact with a natural attribution location, include:

```text
AI-Model: <exact model name/version>
AI-Provider: <provider>
AI-Role: <Drafted|Reviewed|Co-authored|Analyzed>
```

Where multiple models participate, list each model and its role.

## 4. Honesty and traceability

- Never claim review or participation by a model that did not actually perform that work.
- Never backfill a guessed model/version.
- Preserve existing human authorship and attribution.
- Model attribution supplements human accountability; it does not transfer legal or organizational responsibility to the model.
- Repo-specific rules may add stricter requirements but may not weaken this policy unless the repository owner explicitly directs otherwise.

## 5. Agent instruction

Before creating a commit, PR, or other attributable GitHub artifact, read this file and comply with it. This policy is intended to be consumed by all current and future AI tools operating in the repository.

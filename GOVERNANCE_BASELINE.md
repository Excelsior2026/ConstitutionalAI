# Repository Governance Baseline

**Status: REQUIRED for active development.** Effective 2026-10-28. This baseline supplements, and never silently overrides, repository-specific policies, architecture decisions, license terms, regulations, or AGENTS.md instructions.

## Authority, responsibility, and approvals
- Human owners retain authority over consequential decisions. An AI system may perform only tasks explicitly delegated within a documented scope. No model may approve its own work, expand its own authority, impersonate a human, or treat model consensus as human authorization.
- Document the authorized decision, accountable human, scope, evidence, and outcome for security changes, releases, production deployments, regulated data actions, license changes, and other high-impact operations. When applicable, approvals are time-bounded, revocable, and bound to the exact action.
- Keep AI attribution separate from legal responsibility. Do not claim approval or deployment merely because a model recommended it.

## AI provenance and independent review
- Read and obey [AI_ATTRIBUTION.md](AI_ATTRIBUTION.md). Record the actual model name/version, provider, tool, and role on every materially AI-authored GitHub artifact. Never guess missing historical authorship.
- AI-drafted PRs require an independent review by a **different actual model**, against the final PR head SHA. Review evidence must exist as a linked, attributable review artifact with the exact reviewed SHA and findings or explicit no-findings conclusion. PR-body claims and a green metadata validator **alone are not proof of independent review**.
- A material push invalidates earlier review; rerun appropriate checks and secure a new independent review. Record both models in the PR. Human acceptance is separate from cross-model review.
- Protect existing author credit and session privacy; do not inspect or alter another agent's private state without authority.

## Changes, testing, and release
- Work on scoped branches or isolated worktrees; avoid overwriting simultaneous work. No unreviewed direct-to-default-branch implementation changes, force pushes, or bypass of required checks.
- For material work, identify the issue/requirement and expected outcome; link changed artifacts, tests, review, and acceptance evidence. Make interfaces versioned and backwards-compatible when practical; declare breaking changes and migration/rollback plans.
- Run relevant tests, lint, build, security checks, and end-to-end examples as appropriate to the repository. Describe what did **not** run; failures must not be represented as successes. A passing PR metadata workflow is not proof that branch protection is configured.
- Maintain release notes and document known limitations. Do not label a prototype production-ready or promise outcomes without verification.

## Security and evidence
- Use least privilege; protect secrets, tokens, private conversations, personal data, and regulated records. Never commit secrets or real sensitive test fixtures. Review dependency and supply-chain risks; report and remediate vulnerabilities through the repository's disclosure mechanism.
- Preserve audit-relevant decisions, evidence manifests, checksums/digests where supported, tests, and review identifiers. Do not rewrite certified or otherwise immutable historical records; corrections use documented, append-only or versioned remediation where required.
- Separate untrusted input from privileged instructions, tools, and authorization; test denial, retry, restart, and failure paths for high-impact workflows.

## Product boundaries and ownership
- Respect each product's service and data ownership boundaries, licensing, third-party rights, confidentiality, and existing architecture decisions. Do not silently transfer IP, relicense code, introduce competing product rights, or move features into a neighboring product. Shared components must use explicit versioned interfaces; consuming products opt in to interfaces they need.
- For government or regulated projects, trace applicable source guidance through requirements, implementation, tests, evidence, and human acceptance. Distinguish law from advisory guidance. Vendor-neutral contracts and outcome demonstrations are preferred over vendor-specific checklists.
- Repo-specific requirements may add stricter controls; material conflicts require a documented human decision, never unilateral relaxation by an agent.

## Enforcement reality
This document is a required working policy, not a claim that automated enforcement exists. Verify required GitHub checks, review evidence, CODEOWNERS, branch rulesets, security scanning, and approval permissions individually before claiming an enforced merge gate.

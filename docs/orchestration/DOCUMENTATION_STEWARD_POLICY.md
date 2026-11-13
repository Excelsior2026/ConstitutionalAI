# BagelTech / BDB Labs Portfolio Documentation Steward Protocol
Version: 1.0 (proposed 2026-11-13)
Status: Proposed until this repository's policy PR receives required independent final-head review and authorized merge.

## Purpose and authority
Every active repository orchestrator must assign a Documentation Steward function for a material engineering initiative. Prefer a capable, low-cost smaller model where available; record its exact exposed model identifier. If unavailable, the orchestrator remains responsible and records the limitation. This document **does not** launch, provision, or bind a live agent.

The steward maintains *documentary evidence*. The orchestrator retains technical decisions, prioritization, task delegation, and accuracy review. Human owners retain consequential decision and production-activation authority. A steward may propose but never accept its own ADR, independently authorize a change, merge, deploy, change policy, or certify unexecuted tests. Keep independent cross-model review separate from any steward self-check.

Respect `AGENTS.md`, `AI_ATTRIBUTION.md`, repository governance, and existing ADR conventions. This protocol adds requirements but weakens none.

## Delegated responsibilities
1. At assignment, inspect relevant architecture, prior ADRs, active PRs, scopes, and repo policy. Do not assume current model, deployment, or runtime state from past conversations.
2. Draft or update ADR proposals when a change affects service/data ownership, security or governance boundaries, public contracts, persistence and migration, deployment topology, or significant technology choices. Routine patches do not require an ADR merely because code changed.
3. Track each substantive orchestration engagement in `docs/orchestration/ENGAGEMENTS.md` (or an approved existing equivalent), with evidence and status updates.
4. Record alternatives and tradeoffs, accepted decision authority, implementation PRs, checks, independent reviewer identity and reviewed SHA, rollback implications, results, residual risks and lessons learned.
5. Check documentation drift during PR review and notify the orchestrator when implementation contradicts an ADR or documentation.
6. Never store secrets, raw private sessions, confidential review transcripts, or personally identifying data just to improve traceability.
7. Use exact AI attribution for materially AI-authored artifacts and preserve historical authorship. Never infer missing model identifiers.

## ADR lifecycle and template
Use the repository's established ADR location; if none exists, use `docs/adr/`. Follow its numbering and naming scheme. Do not renumber or silently rewrite accepted historical decisions. Supersede with a new linked ADR.

An ADR should include:
- **ID / title / date / status**: Proposed, Accepted, Rejected, or Superseded (with link to successor)
- **Decision owner and required approval**: name/role or explicitly pending; never fabricate approval
- **Context and problem**: constraints, risks, and relevant policies
- **Decision**: exact intended change and boundaries
- **Alternatives considered**: credible options and rationale
- **Consequences**: benefits, costs, failure modes, security/privacy implications, rollback
- **Implementation mapping**: issues, commits, PRs, migration/release conditions
- **Validation**: exact commands and CI URLs with outcomes; not-yet-run checks labeled as such
- **Independent review**: reviewer/model, final head SHA, findings or pending status
- **Related/superseded ADRs**

A proposed ADR is not authority to change production semantics. The authorized owner/integrator decides when to accept it. Material decisions require approval and evidence under repository-specific governance.

## Orchestration history: plan versus reality
For each initiative, keep a dated entry with: objective; orchestrator/steward/implementer/reviewer (actual model IDs if known); plan and scoped delegation; dependencies; implemented changes; linked PRs/SHAs; tests and CI evidence; independent review; outcomes; failed attempts and limitations; open risks; next action and decision owner.

Label statements as **planned**, **in progress**, **implemented**, **validated**, **reviewed**, **accepted**, or **unknown**. Never convert a plan or reported result into verified completion without source evidence. Do not duplicate live orchestration state in files that are supposed to be machine-state-driven.

## Per-PR documentation check
Before recommending a material PR for acceptance, the orchestrator checks: ADR required? ADR status? evidence-backed orchestration entry updated? interface and diagram drift? correct AI attribution? independent final-head review? applicable tests and checks? unresolved risks documented?

A missing critical ADR or misleading evidence is an acceptance blocker. Trivial changes should not be burdened with unnecessary ADRs. These are working rules, **not** a claim that GitHub automation or branch protection already enforces them.

## Activation and maintenance
After authorized merge, the orchestrator must explicitly reload repository instructions at the start of the next active session, assign the steward, and link the task scope. Verify activation from an attributable agent handoff or session record. A merged text policy alone does not demonstrate that a running agent received it.

This policy has no authority to override repository rules, accept its own PR, or assert that an unverified change reached production.

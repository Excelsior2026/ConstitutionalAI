# Mandatory AI Contribution Policy

Before making commits, pull requests, reviews, issues, releases, or other attributable GitHub changes, read and obey [AI_ATTRIBUTION.md](AI_ATTRIBUTION.md).

Non-negotiable owner rules:
- AI-authored commits must name the exact model/version in commit trailers.
- AI-drafted PRs must name the drafting model and be reviewed at the final head SHA by a **different model** before merge.
- Both participating models must be identified in the PR.
- Never claim model participation that did not occur.



<!-- PORTFOLIO ADR GOVERNANCE: BEGIN -->
## Consequential decisions, ADRs, and model review roles

Record each consequential decision in a version-controlled ADR in the repository's established ADR directory and numbering scheme. Consequential decisions include architecture and system boundaries; security and privacy; authentication, authorization, and tenancy; APIs and data models or migrations; dependency and technology-stack choices; deployment, build, and release behavior; reliability and operations; accessibility; and material testing or code-quality tradeoffs. Create or update the ADR before or alongside the implementation and link it from relevant issues, PRs, and evidence.

Use the [ADR index and governance guide](docs/adr/README.md) and its linked template. Preserve existing repository-specific approval, attribution, review, and status rules.

### Required model subagents for substantial engineering work

The orchestrator must assign three distinct model subagents for each substantial engineering task or orchestration. Each is separate from the implementer and from the other review roles; do not combine roles to simulate independent review.

1. **Documentation Steward** — audits existing ADR coverage before work; drafts detailed ADRs and retrospective records from repository evidence; maintains the ADR index, decision log, issue links, and implementation/verification evidence as work proceeds; reconciles documentation to the final code and exact commit. The steward does not invent historical intent or approve its own ADRs.
2. **Owner Review and Approval Delegate** — acts as the delegated owner-side reviewer for requirements fit, decision rationale, evidence, risks, acceptance criteria, and ADR completeness. It may approve or request changes only within authority explicitly delegated for the task, and must state that scope in its review. It must not claim to be the human owner or authorize a merge, deployment, production change, or reserved security/legal/privacy decision unless the human owner explicitly delegated that specific authority.
3. **Principal Systems Architect** — independently reviews the actual technology stack, dependencies, architecture and integration boundaries, security and reliability implications, maintainability, test strategy, and code quality. It records evidence-based findings, alternatives, and required ADRs against the exact commit under review.

The owner delegate, architect, and documentation steward must be distinct model subagents and distinct from the implementation author. Review the exact final commit SHA; any material change requires a fresh review. If the environment cannot provide the required distinct subagents, record the limitation and do not claim the corresponding review or approval occurred.

### ADR evidence and status

An ADR must distinguish verified facts from inference. For retrospective ADRs, label the record **Retrospective**, use the current recording date, cite code/docs/history evidence, and state when original decision date, author, rationale, or approval is unknown. Do not fabricate those details. Keep decisions proposed or pending until the repository's authorized approval rule is satisfied. The Documentation Steward maintains the index and links but does not change status to accepted on its own.
<!-- PORTFOLIO ADR GOVERNANCE: END -->

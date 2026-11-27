# Architecture Decision Records

This is the index and working guide for architecture and other consequential decision records in this repository.

## Repository convention

- Canonical ADR directory: `docs/adr/`
- Template: [ADR-TEMPLATE.md](ADR-TEMPLATE.md)
- Preserve any existing numbering, naming, status, and approval conventions in this repository.
- Add each new ADR to the record list below and link it from the related issue, pull request, and evidence.

## Documentation and review roles

For substantial engineering work, the orchestrator assigns three distinct model subagents, each separate from the implementer and from one another:

1. **Documentation Steward:** audits ADR coverage, drafts evidence-backed ADRs, maintains this index and implementation evidence, and reconciles documents with the final commit.
2. **Owner Review and Approval Delegate:** reviews requirements fit, evidence, risks, acceptance criteria, and ADR completeness; approves or requests changes only within the task's explicitly delegated scope. It cannot claim human-owner identity or authorize merge, deployment, production changes, or reserved decisions without explicit authority.
3. **Principal Systems Architect:** independently reviews the actual tech stack, dependencies, architecture, integrations, security/reliability, maintainability, test strategy, and code quality against the exact commit.

These roles cannot be combined. If distinct subagents are unavailable, record the limitation and do not claim the review occurred. The repository's existing human approval and independent review rules remain in force.

## When to write an ADR

Create or update a detailed ADR for consequential architecture, security, privacy, identity/access, tenancy, API, data/migration, dependency, technology-stack, build/release/deployment, operations, accessibility, reliability, or material testing/code-quality decisions. Record the decision before or alongside implementation. Do not create ADRs for trivial implementation details.

Each record must capture context, constraints, evidence, options (including doing nothing), decision and rationale, consequences/tradeoffs, security/privacy/accessibility/operations implications, risks and mitigation or rollback, validation, follow-up ownership, and links. Use `[ADR-TEMPLATE.md](ADR-TEMPLATE.md)`.

For retrospective records, label them **Retrospective**, use the date the record is written, cite repository evidence, separate facts from inference, and identify unknown original dates, authors, intent, or approval. Never invent history. Keep status Proposed or Pending until approval under this repository's rules. The Documentation Steward maintains records but does not approve its own ADRs.

## Existing ADR records

_No ADR records were found in the configured ADR locations during initial setup. This is an audit item, not proof that the repository has no consequential decisions._

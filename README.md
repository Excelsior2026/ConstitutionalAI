# The Constitutional AI Project — Founding Repository

This repository hosts the living library for **Constitutional AI** and its companion line **AI and Our Social Contract**.

## Note on Authorship
Co-authored and authenticated by **William Parris & GPT ‑5**.

The placement of `AUTHORS.txt` and corresponding references across this repo affirm that this work was conceived and developed as a human–AI partnership.

## Repository Structure

- `90_Administrative/` – Administrative files such as checksums and curator notes for internal tracking.
- `Constitutional-AI-Framework-main/` – Source code implementing the Constitutional AI framework.
- `ConstitutionalAI_PublicationPack_v1_DOIReady/` – Publication materials ready for DOI assignment.
- `scripts/` – Utility scripts for processing or analysis.
- `site/` – Documentation site or static website assets.
- `AUTHORS.txt` – List of authors and contributors.
- `CITATION.cff` – Citation information for referencing this repository.
- `CODE_OF_CONDUCT.md` – Code of conduct guidelines.
- `CONTRIBUTING.md` – Contribution guidelines.
- `.DS_Store` – Mac OS metadata (can be removed).

## Proposed Reorganization

To improve navigation and clarity, consider the following adjustments:

- Move administrative files (`90_Administrative`, `AUTHORS.txt`, `CITATION.cff`, `CODE_OF_CONDUCT.md`, `CONTRIBUTING.md`) into a `docs/` directory.
- Move `Constitutional-AI-Framework-main` into a `src/` directory to clearly distinguish code.
- Remove `.DS_Store`.
- Keep publication packages in a dedicated `publication_packages/` directory if desired.
- Ensure the documentation site in `site/` remains separate or integrate it into `docs/` if appropriate.

Please review these suggestions and let me know if you'd like me to implement them.

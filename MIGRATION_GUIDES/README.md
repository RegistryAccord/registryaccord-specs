# Migration Guides

Purpose
- Document safe upgrade paths between schema versions and highlight breaking vs additive changes.

Structure
- One guide per version pair (e.g., post 1.0.0 → 1.1.0).
- Include rationale, field-level mapping, example transforms, and client fallback advice.

Authoring checklist
- Identify semver impact and governance status change.
- Provide before/after examples and negative-case implications.
- Update SPEC_INDEX.json and SPEC_VERSION_MATRIX.md if compatibility shifts.

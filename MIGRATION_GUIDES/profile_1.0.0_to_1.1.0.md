# Migration: profile 1.0.0 → 1.1.0 (example)

Summary
- Adds optional `pronouns` (string) and `location` (string); no removals; backward-compatible.

Semver
- Minor (additive fields only); status remains stable.

Impacts
- Writers: unchanged; older clients ignore new fields.
- Readers: update type definitions to recognize optional fields.

Transforms
- No required transforms; default to omitting absent fields.

Examples
- Before: { "displayName": "A", "bio": "..." }
- After:  { "displayName": "A", "bio": "...", "pronouns": "they/them" }

Testing
- Add valid fixtures including new fields; ensure invalid fixtures catch type/length bounds.

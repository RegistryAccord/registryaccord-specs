# AI Guide

Context
- This is the canonical, language-neutral specs repo for RegistryAccord with Lexicon v1, NSIDs, ADRs, and governance.

Goals
- Keep schemas interoperable and easy to validate/migrate; minimize churn; ensure every change is reviewable and CI-safe.

Authoring rules
- Lexicon v1 only; NSIDs under com.registryaccord.*; additively evolve; breaking changes require new NSIDs.
- Provide examples and update schemas/INDEX.md with status (DRAFT/STABLE).

Workflow
- Validate locally: npm ci && npm run validate.
- In PRs: update examples, INDEX, and docs as needed; link proposal issue and any ADRs.

Review outputs
- Use unified diffs; small, targeted changes; call out breaking changes explicitly with migration notes.

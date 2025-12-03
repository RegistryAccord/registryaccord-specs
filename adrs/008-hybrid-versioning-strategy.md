# ADR-008: Date-Based API Versioning with SemVer SDKs

- **Status:** Accepted
- **Author:** RegistryAccord Team
- **Created:** 2025-11-18
- **Updated:** 2025-11-18

## Summary
RegistryAccord uses a hybrid versioning approach combining date-based API versions (e.g., `2025-11-01`) for protocol stability with Semantic Versioning (e.g., `1.2.3`) for SDK packages. This strategy balances strong governance for the open protocol with developer-friendly package management. The approach mirrors Stripe's proven model, which has maintained multi-year backward compatibility without forced breaking changes.

## Context
The protocol must satisfy two competing requirements:

- **Protocol (API) needs:** strong governance, explicit opt-in upgrades, long-term stability, and clear staleness signals for integrations pinned to specific versions.
- **Developer (SDK) needs:** SemVer compatibility for package managers, recognizable upgrade semantics, and the ability to backport fixes without forcing new API adoption.

Pure SemVer for APIs weakens governance and allows surprise dependency upgrades, while date-only versioning for SDKs breaks package manager semantics. A single scheme cannot satisfy both needs simultaneously.

## Decision
Adopt a two-layer versioning strategy:

1. **API Specifications:** Date-based versioning (`YYYY-MM-DD`). Every request must include `RA-API-Version` and accounts are pinned to the first version they call until opted-in to a new date. Breaking changes require a new date release.
2. **SDK Packages:** Semantic Versioning (`MAJOR.MINOR.PATCH`). MAJOR tracks breaking API releases, MINOR covers additive features, and PATCH contains bug fixes.
3. **Mapping:** Maintain `versions.md` to map each API date to compatible SDK major versions. All OpenAPI specs embed `x-api-version`, `x-release-date`, `x-support-until`, and `x-api-stability` metadata.

## Rationale
- **Date-based APIs** provide governance (new date == protocol change), clear staleness signals, and prevent surprise upgrades because the version string is explicit in code.
- **SemVer SDKs** integrate cleanly with npm/pip/go modules, give instant safety signals (1.2.3→1.2.4 safe, 1.2.3→2.0.0 breaking), and allow backporting patches.
- **Mapping table** bridges the two systems and informs tooling/SDK generators.

## Consequences
**Positive:**
- Proven governance model (Stripe precedent).
- Developer-friendly SDK upgrades.
- No surprise breakage thanks to account pinning.
- Flexible support windows (18 months) managed per API date.

**Negative:**
- Two versioning schemes to document and automate.
- Educating developers on the hybrid approach.
- Mapping file (`versions.md`) must stay accurate.

## Alternatives Considered
1. **Pure SemVer everywhere:** Too easy to accidentally break APIs, no staleness signals, dependency upgrades can break integrations.
2. **Pure date-based everywhere:** Package managers cannot express constraints, and developers lose performant SemVer semantics.
3. **Path-based versioning only (`/v1/`):** Useful but orthogonal—still requires governance over request headers and SDK packages.

## Implementation
- `VERSIONING.md` documents the policy; `versions.md` enumerates mappings.
- Each OpenAPI file includes x-headers with release metadata.
- SDK repositories (TypeScript, Python, Go, etc.) follow SemVer and reference the API date they target.
- Deprecation process: 90-day notice via headers (`Deprecation`, `Sunset`) and comms before removing support.
- Tooling enforces that new API dates trigger SDK major bumps and mapping updates.

## References
- `VERSIONING.md`
- `versions.md`
- `SPECS_REQUIREMENTS.md` §6.1 & §12.7
- Stripe API versioning model

## Related ADRs
- ADR-002 (Cursor Pagination) – depends on stable versioning.
- ADR-003 (RFC 7807 Errors) – echoes `RA-API-Version` in responses.
- ADR-006 (Specification Completeness).

_Last updated: 2025-11-18_

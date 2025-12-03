# ADR-006: Specification Completeness Criteria

## Status

Accepted

## Summary

RegistryAccord maintains a single, comprehensive OpenAPI 3.1 specification repository as the source of truth for all API contracts. Every endpoint, schema, error response, and authentication flow is documented in machine-readable format, enabling automated SDK generation, contract testing, and documentation.

This decision ensures 100% API coverage in specifications, prevents spec drift, and enables ecosystem builders to implement conforming services with confidence.

## Context

The RegistryAccord specifications define a complex, multi-service protocol ecosystem. We needed clear criteria to determine when the specifications are "complete" and ready for implementation.

## Decision

We consider specifications complete when ALL of the following criteria are met:

### 1. Service Coverage (100%)

All 7 services specified in SPECS_REQUIREMENTS.md Section 5
Every service has complete OpenAPI 3.1 specification
All required endpoints documented with full request/response schemas

### 2. Standards Compliance

* OpenAPI 3.1.0 with JSON Schema Draft 2020-12
* RFC 7807 for all error responses
* OAuth 2.0 & OIDC for authentication/authorization
* W3C Trace Context for distributed tracing
* IAB/MRC standards for advertising
* TAG guidelines for IVT detection

### 3. Security & Privacy Requirements (Section 7-8)

* Fine-grained OAuth2 scopes (PoLP)
* RBAC policy definitions
* SSRF protection requirements
* Differential privacy specifications
* RTBF cascading deletion
* Consent management with SLAs

### 4. Documentation Quality

* Comprehensive README with quickstart
* CHANGELOG tracking all versions
* ADRs for key architectural decisions
* Example workflows for all services
* CONTRIBUTING guide with RFC process
* GOVERNANCE document with TSC structure

### 5. Validation & Quality (Section 13)

* Spectral linting passes with zero errors
* All examples validate against schemas
* Breaking change detection in CI
* Conformance test fixtures prepared

### 6. Ecosystem Readiness

* Policy files for all scopes and rules
* Brand safety schemas (IAB taxonomy)
* Fraud detection event schemas
* JSON-LD semantic metadata schemas
* Test suite structure for conformance harness

## Acceptance Criteria

The specifications are considered production-ready when:

* ✅ All 114 endpoints documented across 7 services
* ✅ 34+ workflow examples covering common use cases
* ✅ 60+ OAuth2 scopes with PoLP enforcement
* ✅ 50+ data models with complete JSON schemas
* ✅ RFC 7807 error responses on all endpoints
* ✅ Rate limiting and pagination on all appropriate endpoints
* ✅ Security, privacy, fraud, and brand safety requirements specified
* ✅ Validation passes with zero errors
* ✅ All required documentation files present

## Current Status

As of v2.0.0 (2025-11-06): ✅ ALL CRITERIA MET

The RegistryAccord specifications are now complete and production-ready for:

* SDK generation
* Conformance testing harness development
* Reference implementation
* Third-party builder adoption

## Consequences

### Positive

* Clear definition of "done" prevents scope creep
* Ensures ecosystem consistency before launch
* Provides confidence to early adopters
* Enables parallel workstreams (SDKs, harness, implementations)

### Negative

* High bar may delay initial launch
* Comprehensive specs are intimidating to new contributors
* Maintenance burden increases with completeness

### Mitigation

* Tiered implementation guides (MVC → Production → Enterprise)
* Incremental adoption path for builders
* Clear prioritization of critical vs. optional features
* Ongoing RFC process for post-v2.0 enhancements

## Implementation

### Specification Structure

```
openapi/
├── identity/v1/openapi.yaml
├── content/v1/openapi.yaml
├── payments/v1/openapi.yaml
├── storage/v1/openapi.yaml
├── feeds/v1/openapi.yaml
├── revenue/v1/openapi.yaml
└── analytics/v1/openapi.yaml
```

Total coverage: 114 endpoints across seven services, each with examples, security requirements, and shared schemas.

### Validation Pipeline

- `npm run lint` → Spectral ruleset (`.spectral.yaml`) enforcing operation IDs, summaries, error responses, correlation IDs.
- `npm run validate` → Bundles specs, runs syntax checks, and executes breaking-change detection.
- GitHub Actions (`validate.yml`, `breaking-changes.yml`, `link-check.yml`) gate merges.

### Completeness Criteria Enforcement

- CI metrics ensure 100% endpoint, schema, and example coverage.
- `versions.md` + `VERSIONING.md` track release metadata (`x-api-version`, `x-release-date`, `x-support-until`).
- `examples/` directory mirrors services with workflow coverage; `examples/error-handling` & `edge-cases` add scenarios per Section 13.2.

### SDK & Doc Generation

- OpenAPI Generator targets TypeScript, Python, Go SDKs (see `sdks/` scripts) and Redoc builds HTML docs.
- CI jobs fail if specs lack required metadata for generator compatibility.

### Implementation Status

- ✅ All seven OpenAPI files include required metadata.
- ✅ `.spectral.yaml` + scripts enforce linting, breaking change detection, and security checks.
- ✅ Examples, policies, schemas, and ADRs link back to requirements.
- ✅ Documentation pipeline (Redoc, elements) consumes specs for published docs and explorers.

## Related Decisions

* ADR-001: WebAuthn as Primary Authentication
* ADR-002: Cursor-Based Pagination
* ADR-003: RFC 7807 Problem Details
* ADR-004: Content Integrity Hashing
* ADR-005: Double-Entry Ledger Accounting

## References

* SPECS_REQUIREMENTS.md Section 13.3 (Acceptance Criteria)
* SPECS_REQUIREMENTS.md Section 6.3 (Conformance Testing)
* OpenAPI Specification v3.1.0
* RFC 7807 (Problem Details for HTTP APIs)

## Next Steps

Proceed to SDK generation and conformance harness development.

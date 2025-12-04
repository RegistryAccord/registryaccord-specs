# Global API Standards

## 1. API Design Requirements

All API specifications must follow these design principles:

### 1.1. REST API Standards

  * REST v1 endpoints with explicit version prefixes (e.g., `/v1/...`).
  * Signed `ETag` headers for content integrity.
  * Correlation IDs for request tracing.

### 1.2. Versioning

  * See *Section 2.1* for detailed versioning specifications.

### 1.3. Authentication & Authorization

  * JWT-based authentication for API requests.
  * **Principle of Least Privilege (PoLP):** Scopes must be fine-grained (e.g., `content:read`, `content:write`) and enforced at the operation level.
  * OIDC/OAuth2 flows for 3rd-party application authorization.
  * Scoped tokens with clear permission boundaries.

### 1.4. Error Handling Standards

  * **RFC 7807 Problem Details:** All error responses must conform to the RFC 7807 standard, providing `type`, `title`, `status`, `detail`, and `instance` fields.
  * **Correlation ID:** All error responses must include the request's correlation ID (e.g., `trace-id`).
  * **Error Catalog:** A machine-readable catalog of error types must be provided in JSON Schema format, versioned, and located in `/schemas/errors/`.
  * **Retry Hints:** Rate limit and transient error responses should include `Retry-After` headers.

### 1.5. Pagination Standards

  * **Method:** All list endpoints must use **cursor-based pagination** for performance and dataset consistency.
  * **Parameters:** Use `limit`, `after` (cursor), and `before` (cursor).
  * **Response:** The response body must include a `pagination` object with `next_cursor` and `has_next_page` fields.

### 1.6. Rate Limiting Standards

  * **Headers:** All responses must include standardized rate limit headers (`X-RateLimit-Limit`, `X-RateLimit-Remaining`, `X-RateLimit-Reset`).
  * **Visibility:** Specs must document default quotas and **per-endpoint** limits.
  * **Flexibility:** Specs must define standards for **burst allowances** (e.g., using a **token bucket** algorithm, allowing bursts up to 2x the sustained rate for 60 seconds) and a process for **negotiating higher quotas** (e.g., via a `/v1/limits/request` API or support ticket with a defined SLA).
  * **Error:** A `429 Too Many Requests` response (per RFC 7807) must be returned when limits are exceeded.

### 1.7. Webhook Standards

  * **Signatures:** All outgoing webhooks must be signed using a strong, verifiable signature (e.g., HMAC-SHA256) included in a request header.
  * **Retries:** Specs must define the webhook retry policy (e.g., **exponential backoff with jitter**, for a maximum of **5 retries over 72 hours**).
  * **Dead Letter Queue (DLQ):** Events that fail all retries must be sent to a designated Dead Letter Queue, and the event publisher must be notified.
  * **Guarantees:** Event delivery guarantees (e.g., "at-least-once") must be documented.
  * **Event Schemas:** All webhook payloads must conform to a registered schema.

### 1.8. API Design Consistency

  * **Timestamps:** All timestamps must be in **ISO 8601** format with the UTC `Z` timezone designator (e.g., `2025-11-05T18:30:00Z`).
  * **Currency:** All monetary values must be represented as integers in the smallest currency unit (e.g., cents) with an **ISO 4217** currency code (e.g., `amount: 1000`, `currency: "USD"` for $10.00).
  * **Booleans:** Field names for booleans should be positive assertions (e.g., `is_active` instead of `is_not_deleted`).
  * **Enums:** All enum values should be `SCREAMING_SNAKE_CASE` for clarity.

### 1.9. Observability & Traceability

  * **Headers:** Every request MUST include `traceparent`, optional `tracestate`, and `X-Correlation-ID` headers as defined in [`docs/OBSERVABILITY.md`](../OBSERVABILITY.md).
  * **Schemas:** Logging, metrics, and health responses MUST conform to the JSON Schemas under `schemas/observability/` (`trace-context.json`, `logging-standards.json`, `metrics-standards.json`, `health-checks.json`).
  * **Error Surfaces:** RFC 7807 envelopes MUST surface the correlation ID and trace identifiers so incidents can be traced end-to-end.
  * **Propagation:** Services MUST propagate inbound Trace Context headers to all downstream calls and record them in structured logs per the observability standards.

## 2. Versioning & Governance

### 2.1. Versioning Policy

#### Two-Layer Versioning Strategy
RegistryAccord uses a hybrid approach inspired by Stripe:
1. **API Specifications**: Date-based versioning (YYYY-MM-DD)
2. **SDK Packages**: Semantic Versioning (MAJOR.MINOR.PATCH)

#### API Version Format (Date-Based)
- Format: `YYYY-MM-DD` (e.g., `2025-11-01`)
- Header: `RA-API-Version: 2025-11-01` (required in all requests/responses)
- Pinning: Accounts are pinned to the API version at first request
- Explicit Upgrade: Developers must explicitly upgrade to new API versions

#### Why Date-Based for APIs?
- Clear staleness signals (2023-06-15 is obviously 2+ years old)
- Explicit breaking changes (new date = deliberate API change)
- No accidental upgrades via dependency resolution
- Strong governance for open protocol

### 2.2. RFC Process

  * **RFC Repo:** A public RFC (Request for Comments) repo must be used for all major changes.
  * **RFC Lifecycle:** RFCs must follow a defined lifecycle: `Draft` -> `Review` (14-day min) -> `Accepted` (TSC vote) -> `Implemented` (2+ implementations) -> `Final`.
  * **Decision Making:** Final decisions are made by a Technical Steering Committee (TSC) vote.
  * **Governance Transition:** The transition from company stewardship to a neutral foundation will be triggered by objective ecosystem metrics (e.g., **3+ independent, certified implementations in production**).

### 2.3. Conformance Testing

  * **Harness:** An automated conformance harness (`registryaccord-conformance`) must be provided. The harness must be runnable as a **CLI tool or Docker container**, and its **tests must be public** to allow for pre-certification validation. Test results must be available in a machine-readable format (e.g., **JUnit XML or JSON**).
  * **Test Coverage:** The suite must cover all API endpoints, auth flows, error cases, and **security & fairness policies**.
  * **Ongoing Monitoring:** Conformance is not one-time. The platform must include **Security Scorecard APIs** and automated checks to continuously audit implementations *after* certification. Scorecards will be calculated as a **weighted average** across dimensions (e.g., **Security, Privacy, Performance, Reliability, Fairness**), be **updated daily**, and be publicly visible.
  * **Badge Generation:** A system for automatically generating and renewing "RA-Certified" badges.
  * **Dashboard:** A public dashboard must show the conformance and security scorecard status of known implementations.

### 2.4. Fairness Audit Framework

  * **Audit Requirements:**
      * **Frequency:** Semi-annual audits for all widely deployed rankers.
      * **Independence:** Auditors selected by RA governance board with no financial ties to ranker owners.
      * **Rotation:** To maintain independence, auditors may serve a maximum of **3 consecutive years** for the same ranker, with a **1-year cooling-off period** before re-engagement.
      * **Access:** Full access to ranker logic (signals, weights) under NDA is **non-negotiable for certification**.
  * **Audit Fund:**
      * **Funding:** A central audit fund, sourced from **1-3% of platform revenue**, will be managed by RA.
      * **Transparency:** Allocation will be transparent and reviewed annually.
      * **Triggers:** Includes provisions for **emergency audits** for critical fairness issues.
  * **Audit Scope:**
      * Signal definitions and weighting mechanisms.
      * Historical performance across demographic groups.
      * Compliance with published documentation.
      * Dispute handling processes.
      * A/B test methodology.
  * **Dispute Resolution (Three-Tier):**
      * **Tier 1 (Standard):** 2-day acknowledgment, 10-day resolution.
      * **Tier 2 (Escalated):** Independent appeals board, 20-day resolution.
      * **Tier 3 (Ombudsperson):** Binding decision, 30-day resolution.
  * **Public Transparency:**
      * **Audit Report Format:** Published audit reports must follow a standard format, including an executive summary, methodology, findings by category, remediation recommendations, and an auditor conflict-of-interest statement.
      * Quarterly transparency reports on disputes will be published.
      * A public dashboard with dispute statistics will be maintained.

## 3. Security & Privacy

### 3.1. Security Baselines

  * **Zero Trust Architecture:**
      * **Transport Security:** mTLS with certificate pinning required for service-to-service calls; TLS 1.3 minimum for external.
      * **Context-Aware Access:** Specs must define hooks for context-aware controls (e.g., time-based, location-based, anomaly-based denials).
  * **API Key Management (Builder Security):**
      * **PoLP Scoping:** API keys must be scoped to the minimum required operations (e.g., `content:read`).
      * **Key Scanning:** Define revocation APIs to support automated scanning for leaked keys in public repositories.
      * **Separation:** Mandate separation of developer/testing keys from production keys.
  * **Runtime Threat Detection:**
      * **OWASP API Top 10:** Implementations must be able to detect and block common OWASP API threats (injection, broken auth, mass assignment).
      * **Shadow API Detection:** Define standards for API discovery and inventory to detect "zombie" (deprecated) or "shadow" (undeclared) endpoints.
  * **SSRF Protection:** All services must validate and sanitize all user-supplied URLs, especially for webhook callbacks and storage provider configurations, to prevent **Server-Side Request Forgery (SSRF)** attacks. Use allow-lists for known hosts where possible.
  * **Supply Chain Security:**
      * **SBOMs:** A Software Bill of Materials (SBOM) is required for all core services.
      * **Dependency Scanning:** Conforming implementations must meet minimum dependency vulnerability scanning standards.
      * **Signed Artifacts:** All official SDK releases must be signed with published checksums.
      * **Provenance:** Build integrity must be verifiable (e.S., SLSA framework).

### 3.2. Privacy by Design

  * **Behavioral Tracking Limits:**
      * **No Shadow Profiles:** Specs must prohibit the collection of behavioral data before explicit, granular consent.
      * **Cross-App Correlation:** Define strict limits on correlating user data across different 3rd-party applications.
  * **Right to Erasure (RTBF) SLAs:**
      * **Timeframe:** A maximum of **30 days** for deletion propagation.
      * **Policy:** Define hard vs. soft delete policies for different data types.
      * **Cascading Deletion:** Deletion requests must cascade from the Identity Service to all other services (Content Registry, Storage, Analytics).
  * **Data Residency & Sovereignty:**
      * **APIs:** Must include APIs for users/builders to specify data sovereignty routing (e.S., "EU-only").
      * **Attestation:** Must include endpoints for builders to query compliance status (e.S., GDPR, CCPA).
  * **Breach Notification:** Specs must mandate adherence to breach notification timelines (e.S., 72 hours per GDPR).

## 4. Brand Safety & Fraud Detection

### 4.1. Brand Safety

  * **Schema:** Define a **Brand Safety Schema** aligned with **IAB Content Taxonomy v3.0**.
  * **Classification API:** The Revenue Service must use this schema for pre-bid content classification.
  * **Confidence Scores:** Classification responses must include confidence scores.
  * **Review:** Define standards for human review escalation for contested classifications.

### 4.2. Invalid Traffic (IVT) & Fraud

  * **Bot Detection:** The Analytics service must include bot detection requirements.
  * **Fraud Scoring:** Define fraud scoring APIs that advertisers and the Payments service can query.
  * **Fake Engagement:** The Payments service must use fraud scores to detect fake engagement (bot views/clicks) before payouts.
  * **IVT Refunds:** The Revenue service must have a defined policy and API for refunding spend on impressions later classified as IVT.

### 4.3. Content Moderation

  * **Deepfake Detection:** The Content Registry must include metadata hooks for deepfake detection flags.
  * **Appeal APIs:** All takedown actions must be associated with an appeal API.

## 5. Transparency & Explainability

### 5.1. User (Audience) Transparency

  * **Data Access API:** Must include a "'What do you know about me?'" endpoint for user data export.
  * **Ad Targeting Explanation API:** Must include a "'Why am I seeing this ad?'" endpoint that explains the targeting signals used (in an obfuscated, user-safe way).

### 5.2. Creator Transparency

  * **Content Access Audit API:** Must include a "'Who accessed my content?'" audit trail API for creators.
  * **Monetization Change Notifications:**
      * **SLAs:** Changes to platform split rules must be announced with a minimum notice period.
      * **Minimums:** Define policies for minimum creator split thresholds.
  * **Monetization Dispute APIs:** The Payments service must include APIs for creators to formally contest revenue calculations.

### 5.3. Algorithmic Transparency

  * **Tiered Explainability:** The Feed Generator must provide tiered explanations (high-level for users, detailed for auditors).
  * **Signal Obfuscation:** Ranking signal explanations must be obfuscated to prevent SEO spam and gaming.
  * **IP/Transparency Balance:** While proprietary methods are protected from public disclosure, **independent auditors** (per *Section 6.4*) must be granted full access to all logic, signals, and weights to verify fairness.

### 5.4. Dispute Resolution & Reporting

  * **Who Can File:**
      * Content creators affected by ranking bias.
      * Users experiencing discriminatory content delivery.
      * Independent auditors identifying systemic issues.
      * Regulatory bodies or consumer advocates.
  * **Filing Costs:** Filing is free for first-time complainants. To prevent system abuse, repeat filers (e.g., 3+ disputes in 90 days) may be subject to a small, refundable fee (returned if the dispute is upheld).
  * **Evidence Requirements:**
      * Detailed description of perceived unfairness.
      * Examples with timestamps and user IDs (anonymized).
      * Comparison with documented ranker behavior.
      * Supporting data (if available).
  * **Resolution Process (Tier 1):**
      * Platform reviews evidence within **2 business days**.
      * Engages ranker owner for response (within **7 days**).
      * Decision made based on fairness metrics and audit history.
      * Appeals escalate to the **independent board** (Tier 2).
  * **Consequences for Repeated Violations:**
      * **1st Violation:** Public warning + mandatory re-audit.
      * **2nd Violation:** Temporary suspension from marketplace (30 days).
      * **3rd Violation:** Certification revoked and ranker delisted.
  * **Public Reporting:**
      * RA will publish **quarterly transparency reports** on dispute/appeal statistics (volume, types, outcomes, timelines).
      * Dispute outcomes (anonymized) will be published to a public dashboard (via the `/v1/feeds/disputes/stats` API).

## 6. Documentation Requirements

### 6.1. API Reference

  * Comprehensive endpoint descriptions, parameters, auth requirements, error codes, and rate limits.

### 6.2. Implementation Guides

  * To reduce complexity, documentation must include **tiered implementation guides**:
    1.  **"Minimum Viable Conformance"** (Core APIs)
    2.  **"Production Ready"** (Security + Privacy baselines)
    3.  **"Enterprise Grade"** (Full fraud, brand safety, compliance)
  * Quickstart tutorials, auth flows, and common use cases.
  * Data Models: Complete entity definitions and field types.

### 6.3. Tooling & Automation

  * **Reference Docs:** Specs must be consumable by tools like **Redoc** or **Stoplight** for automatic generation of reference documentation.
  * **Interactive Explorers:** Docs must include an interactive API explorer (e.S., "Try it out") with sandbox environments.
  * **Code Snippets:** Tooling must generate code snippets in all supported SDK languages, with each language maintained in its respective SDK repository.
  * **Changelogs:** Changelogs must be automatically generated from spec diffs.

## 7. Observability Standards

Specs must define standards for observability to ensure interoperability and debugging.

  * **7.1. Distributed Tracing:** All API requests must accept and propagate **W3C Trace Context** headers (`traceparent`, `tracestate`).
  * **7.2. Structured Logging:** All services must emit structured (JSON) logs with standard fields (e.g., `service`, `trace_id`, `user_id`).
  * **7.3. Health Checks:** All services must expose standard health check endpoints:
      * `/livez`: Liveness probe (service is running).
      * `/readyz`: Readiness probe (service is ready to accept traffic).
  * **7.4. Metrics:** Specs must define a standard set of core metrics to be exposed (e.g., via OpenTelemetry format). Implementations must follow **OpenTelemetry semantic conventions** for metric and dimension naming to ensure comparability.

## 8. SDK Generation Requirements

  * **Generator Tooling:** Specs must be compatible with standard generators like **OpenAPI Generator**.
  * **Custom Templates:** The project will maintain custom templates to ensure idiomatic code, auth helpers, and retry logic for each supported language.
  * **Repository Structure:** Each programming language will have its own dedicated SDK repository (e.g., `registryaccord-sdk-ts`, `registryaccord-sdk-py`, `registryaccord-sdk-go`).
  * **Package Naming:** Define standard package names per language (e.g., `@registryaccord/sdk` for TypeScript, `registryaccord` for Python).
  * **Generated Features:** SDKs must include auth helpers, automated retries, pagination, and typed models/errors.
  * **Language Support:** Initially supporting TypeScript, Python, Go, Java, and .NET with plans to expand based on community demand.

#### 8.1 SDK Versioning Strategy
- SDKs follow Semantic Versioning (MAJOR.MINOR.PATCH).
- SDK major version bumps when API date version changes with breaking changes.
- SDK minor version bumps for new API features (backward-compatible).
- SDK patch version bumps for bug fixes.
- Each SDK release specifies compatible API version(s) in README.

Example:
- SDK v1.x.x → API `2025-11-01`. 
- SDK v2.x.x → API `2026-05-15` (breaking changes).
- SDK v2.5.0 → API `2026-05-15` + new optional features.

## 9. Testing & Quality

### 9.1. Validation & Linting

  * **Linting:** A standard **Spectral ruleset** must be enforced in CI to ensure all specs are consistent.
  * **Breaking Change Detection:** CI must run a tool (e.g., `openapi-diff`) to fail any PR that introduces an unintentional breaking change.
  * **Validation:** All examples must be validated against their schemas in CI.
  * **Security Scanning:** Specs must be scanned for common security anti-patterns.

### 9.2. Example Requirements

  * **Coverage:** Every API endpoint must have at least one full request/response example.
  * **Scenarios:** Examples must cover:
      * The "happy path" (2xx response).
      * Key error scenarios (4xx responses).
      * Edge cases (e.g., empty lists, boundary values).
  * **Workflows:** Multi-step workflow examples (e.g., "Create a Subscription") must be provided.

### 9.3. Acceptance Criteria

  * **Spec Completeness:** 100% of API endpoints and data models are documented in the OpenAPI specs.
  * **Conformance:** All core RA services pass 100% of the conformance test suite, including security, privacy, and **fairness** checks.
  * **Documentation:** All API reference docs are auto-generated and published.
  * **Developer Experience:** Time-to-First-Value (TTFV) is under 20 minutes with the quickstart.
  * **Performance:** All services meet their defined SLOs under load.

## 10. Open Questions & Policy Decisions

This section tracks key policy decisions that must be resolved via the RFC process before v1 GA.

  * **BYO IdP Mapping:** Define the specific patterns (SAML2, OIDC) and attribute mapping specs for "Bring Your Own" Identity Provider.
  * **Multi-Tenancy Model:** Standardize how tenancy is represented (e.g., tenant ID in JWT claim vs. in API path).
  * **Regional Compliance:** Define how regional rules (e.g., GDPR, CCPA) will be surfaced in the API (e.g., region-specific endpoints vs. request headers).
  * **Privacy-Preserving Computation:** Defer federated learning and homomorphic encryption to v2. Focus v1 on differential privacy for analytics and ad auction logs.
  * **Audit Fund Percentage:** Finalize the exact revenue percentage (current range: 1-3%) for the central audit fund and its review cadence via RFC.

## Version History

| Version | Date       | Change Type | Description        | Related ADR |
|---------|------------|-------------|--------------------|-------------|
| 1.0.0   | 2025-12-04 | Initial     | Base Specification | N/A         |

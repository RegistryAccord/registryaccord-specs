# RegistryAccord Conformance Test Suite

This directory contains test fixtures and specifications for validating implementations against the RegistryAccord protocol.

## Purpose

The conformance test suite ensures that:

* All API endpoints behave according to specifications
* Security requirements are enforced
* Privacy guarantees are met
* Error handling is consistent
* Performance SLOs are achievable

## Test Organization

Tests are organized by service:

* `identity/` - Identity Service tests (WebAuthn and OAuth2)
* `content/` - Content Registry tests (versioning, provenance)
* `payments/` - Payments & Payouts tests (splits, fraud, disputes)
* `storage/` - Storage Gateway tests (uploads, pre-signed URLs)
* `feeds/` - Feed Generator tests (ranking, A/B testing)
* `revenue/` - Revenue Services tests (RTB, brand safety)
* `analytics/` - Analytics Service tests (ingestion, privacy)
* `integration/` - End-to-end integration tests

## Running Tests

**Note:** This directory contains test fixtures and specifications.

The actual conformance test harness is in a separate repository:

`registryaccord-conformance` (to be implemented in Phase 5)

The test harness will:

* Read these YAML test specifications
* Execute tests against a target implementation
* Generate conformance reports
* Calculate security scorecard scores

## Test Specification Format

Each test file follows this YAML structure:

```yaml
test_suite: "Identity Service - OAuth2 Flows"
version: "1.0.0"
tests:
  - name: "OAuth2 Authorization Code Flow"
    description: "Complete OAuth2 authorization code flow"
    steps:
      - request:
          method: GET
          path: /authorize
          parameters:
            client_id: "test_client"
            redirect_uri: "https://example.com/callback"
            scope: "identity:read"
        expected_response:
          status: 302
          headers:
            Location: "^https://example\.com/callback\?code=.+"
      # ... more steps
```

## Test Categories

### Functional Tests

* Verify endpoint behavior
* Test data validation
* Check response formats

### Security Tests

* Authentication enforcement
* Authorization (PoLP) verification
* Rate limiting compliance
* Idempotency key handling

### Privacy Tests

* Consent enforcement
* RTBF cascading deletion
* Privacy budget limits
* Purpose limitation tags

### Performance Tests

* Latency SLOs (p95, p99)
* Throughput targets
* Pagination efficiency

## Conformance Levels

Implementations can achieve different conformance levels:

* **Minimum Viable Conformance (MVC)**
  * Core CRUD operations working
  * Basic auth/authz
  * Required error responses
* **Production Ready**
  * All functional tests passing
  * Security baseline met
  * Privacy guarantees enforced
* **Enterprise Grade**
  * Full test suite passing
  * Fraud detection operational
  * Brand safety implemented
  * Performance SLOs met

## Contributing Tests

When adding new tests:

* Follow the YAML structure above
* Include both success and error scenarios
* Test edge cases and boundary values
* Document expected SLOs where applicable
* Reference specific sections of SPECS_REQUIREMENTS.md

## Related Repositories

* Specs: `registryaccord-specs` (this repo)
* Test Harness: `registryaccord-conformance` (separate repo, planned)
* Reference Implementation: `registryaccord-reference` (separate repo, planned)

For more information, see:

* `docs/requirements/global-standards.md` (Conformance Testing)
* `docs/requirements/global-standards.md` (Testing & Quality)

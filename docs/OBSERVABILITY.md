# Observability Standards

RegistryAccord specifications require consistent tracing, logging, and metrics so implementers can correlate requests across services. This document summarizes the contract enforced in the OpenAPI specs and referenced schemas under `schemas/observability/`.

## Trace Context & Correlation IDs

* **Required headers on every request:**
  * `traceparent` (W3C Trace Context) – see [`schemas/observability/trace-context.json`](../schemas/observability/trace-context.json)
  * `tracestate` (optional vendor-specific context) – also defined in the Trace Context schema
  * `X-Correlation-ID` (UUID v4) – echoed in all responses and RFC 7807 errors
* Services MUST propagate the inbound `traceparent` and `tracestate` headers to all downstream calls and emit new span IDs per hop.
* `X-Correlation-ID` MUST appear in structured logs, metrics, and every error envelope so users can trace failures end-to-end.

## Structured Logging

* Logs are JSON and must follow [`schemas/observability/logging-standards.json`](../schemas/observability/logging-standards.json).
* Required fields: `timestamp`, `level`, `service`, `trace_id`, `message`.
* Recommended contextual fields: `request_id` (`X-Correlation-ID`), `user_id`, `org_id`, `http_method`, `http_status`, `duration_ms`.
* Log levels follow the shared taxonomy (`DEBUG`, `INFO`, `WARN`, `ERROR`, `FATAL`).

## Metrics & Health Checks

* Service metrics must conform to [`schemas/observability/metrics-standards.json`](../schemas/observability/metrics-standards.json), exposing OpenTelemetry semantic attributes (`service.name`, `http.method`, `http.status_code`, etc.).
* Health probes (liveness & readiness) must follow [`schemas/observability/health-checks.json`](../schemas/observability/health-checks.json), including component-level status, dependency checks, and `trace_id` propagation for failing checks.
* Metrics and health responses should include `traceparent` / `X-Correlation-ID` headers when invoked over HTTP to preserve the causal chain.

## OpenAPI Integration

All OpenAPI specs under `openapi/*/v1/openapi.yaml` import the following reusable header parameters:

* `#/components/parameters/TraceParent`
* `#/components/parameters/TraceState`
* `#/components/parameters/CorrelationId`

By referencing these parameters on every operation, the specs guarantee that SDKs and services document the required tracing and observability contract.

For implementation guidance, see the upstream requirements in [Rate Limiting Standards](requirements/global-standards.md#46-rate-limiting-standards) and the security/correlation guidance in `adrs/003-rfc7807-errors.md`.

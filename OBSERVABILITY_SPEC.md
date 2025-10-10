# Observability Specification

Correlation
- Accept X-Correlation-Id; generate if absent and echo in responses and events.

Logging
- Structured JSON with levels, correlationId, did (when authorized), and event types.

Metrics
- Prometheus-friendly counters and histograms for request latency and error classes.

Tracing
- OpenTelemetry spans for inbound requests, downstream calls, and event publish/consume.

Redaction
- Never log secrets, tokens, or raw PII; log stable identifiers and hashes where needed.

Sampling
- Default head-based sampling; adjust per environment based on SLOs.

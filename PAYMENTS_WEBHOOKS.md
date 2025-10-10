# Payments Webhooks (Design-Only)

Versioning
- Versioned header (e.g., X-Pay-Version) and payload schema; explicit deprecation windows.

Security
- HMAC signatures with shared secret; include timestamp in signature base string.
- Reject if timestamp skew exceeds 5 minutes; single-use nonce to prevent replay.

Delivery
- At-least-once; provider retries with exponential backoff.
- Receiver returns 2xx only after durable persistence of event.

Validation
- Verify signature, version, and event type; reject unknown or deprecated versions.

Idempotency
- Deduplicate by event ID and signature tuple; store minimal state for replay windows.

Observability
- Correlate deliveries via X-Correlation-Id; return deterministic error bodies on failures.

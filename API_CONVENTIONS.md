# API Conventions

Transport
- HTTPS only; TLS 1.3 recommended.

Auth
- Bearer JWT with sub=did, aud, exp claims; scopes optional and versioned.
- Correlate auth model with DID operations and session issuance.

Request envelopes
- Prefer raw JSON objects unless batching; include `idempotencyKey` for mutating calls.

Response envelopes
- 2xx: `{ data: <object>, meta?: { ... } }`
- Errors: `{ error: { code: string, message: string, details?: object, correlationId: string } }`

Idempotency
- Header: Idempotency-Key; server enforces deduplication window with safe replay.

Correlation
- Header: X-Correlation-Id accepted; generated if absent and returned in responses.

Pagination
- Cursor-based via `cursor` and `limit` with stable sort keys; see PAGINATION_AND_FILTERING.md.

Rate limits
- Headers: `X-RateLimit-Limit`, `X-RateLimit-Remaining`, `X-RateLimit-Reset`.

Content types
- `application/json` default; media uploads negotiated separately per MEDIA_SPEC.md.

Versioning
- URI or header-based API versioning per service; schemas are semver-governed independently.

Time
- RFC 3339 UTC timestamps in payloads; see TIME_AND_LOCALE.md.

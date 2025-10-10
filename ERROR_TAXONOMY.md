# Error Taxonomy

Naming
- Codes are SCREAMING_SNAKE_CASE grouped by domain (IDENTITY_, CDV_, FED_, PAY_).

Classes
- VALIDATION: Unprocessable inputs; non-retriable.
- AUTHZ: Missing/invalid credentials or insufficient scopes; non-retriable until state changes.
- CONFLICT: Resource state conflicts; retriable after reconciliation.
- RATE_LIMIT: Backoff and retry after reset.
- TRANSIENT: Infrastructure or dependency failures; retriable with exponential backoff.

HTTP mapping examples
- 400: *_VALIDATION, *_BAD_REQUEST
- 401/403: *_AUTHZ, *_FORBIDDEN
- 404: *_NOT_FOUND
- 409: *_CONFLICT
- 429: *_RATE_LIMIT
- 500: *_INTERNAL
- 503: *_UNAVAILABLE

Common fields
- `code`, `message`, `correlationId`, optional `details` object.

Examples
- IDENTITY_VALIDATION
- IDENTITY_AUTHZ
- CDV_SCHEMA_REJECT
- CDV_MEDIA_CHECKSUM_MISMATCH
- FED_INGEST_RATE_LIMIT
- PAY_WEBHOOK_SIGNATURE_INVALID

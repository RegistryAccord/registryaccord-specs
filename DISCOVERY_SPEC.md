# Discovery Specification (Minimal)

Scope
- Read-focused scope defining request parameters and response shapes; ranking algorithms remain pluggable.

Endpoints (draft v0)
- GET /v1/feed/following?cursor&limit
- GET /v1/search?q&cursor&limit

Inputs
- Stable cursors and `limit`; search `q` is vendor-neutral.

Outputs
- Arrays of content references adhering to schema versions (e.g., post 1.0.0) plus `nextCursor`.

Transparency
- Document ranking inputs and non-goals; clients may select ranking strategies.

Safety
- Apply rate limits and abuse controls consistently; return standard error envelopes.

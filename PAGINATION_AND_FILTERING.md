# Pagination and Filtering

Pagination
- Cursor-based pagination with `limit` (default 25, max 100) and opaque `cursor`.
- Stable sort keys must be documented per endpoint; default reverse chronological by indexedAt or createdAt.
- Responses include `nextCursor` when more results remain.

Filters
- Common filters: `did`, `collection`, `since`, `until`.
- Filtering must not alter sort stability; combine with indexable predicates only.

Consistency
- Endpoints MUST return deterministic ordering for identical inputs.
- Cursor invalidation is allowed after major reindexing; return a specific error code for invalid cursor.

Examples
- listRecords(did, collection, limit, cursor, since, until) with reverse chronological index.

# ADR 002: Cursor-Based Pagination for RegistryAccord APIs

## Status

Accepted

## Summary

All list endpoints in RegistryAccord use cursor-based pagination instead of offset-based pagination. Cursors are opaque tokens pointing to specific records, enabling consistent pagination even as data changes and supporting efficient database queries with indexed cursors.

This decision ensures stable pagination results across all seven services (Identity, Content, Storage, Payments, Feeds, Revenue, Analytics) and prevents issues like duplicate or skipped items when data is inserted/deleted during pagination.

## Context

RegistryAccord APIs need to provide efficient pagination mechanisms for large result sets. Traditional offset/limit pagination has several drawbacks:

1. **Performance degradation**: As offset increases, database queries become slower because the database must count and skip more records
2. **Inconsistent results**: When new records are inserted during pagination, they can cause existing pages to shift, leading to duplicate or missing results
3. **Limited scalability**: Offset/limit pagination doesn't scale well with large datasets

We evaluated several pagination approaches:

- **Offset/Limit**: Traditional approach with the drawbacks mentioned above
- **Cursor-based**: Uses opaque cursors to navigate through result sets
- **Keyset pagination**: Similar to cursor-based but uses explicit field values

## Decision

We will implement **cursor-based pagination** for all RegistryAccord APIs that return collections of resources.

### Implementation Details

1. **Cursor Parameters**:
   - `limit`: Maximum number of items to return (default: 20, maximum: 100)
   - `after`: Cursor for forward pagination
   - `before`: Cursor for backward pagination

2. **Response Structure**:
   - `data`: Array of resources
   - `pagination`: Pagination metadata
     - `has_next_page`: Boolean indicating if there are more results
     - `has_prev_page`: Boolean indicating if there are previous results
     - `next_cursor`: Cursor for the next page (null if no more results)
     - `prev_cursor`: Cursor for the previous page (null if no previous results)

3. **Cursor Implementation**:
   - Opaque base64-encoded strings
   - Encapsulate sorting criteria and position information
   - Stable under concurrent modifications

4. **Sorting**:
   - Deterministic ordering by `created_at` descending
   - Secondary sort by resource key for stability

## Consequences

### Positive

- **Improved performance**: Constant-time pagination regardless of result set size
- **Consistent results**: Stable pagination even with concurrent modifications
- **Better user experience**: Eliminates duplicate/missing items during pagination
- **Scalability**: Efficiently handles large datasets

### Negative

- **Complexity**: More complex implementation than offset/limit
- **No direct page access**: Cannot jump to arbitrary pages
- **Learning curve**: Developers need to understand cursor-based patterns

### Neutral

- **API consistency**: All RegistryAccord APIs will use the same pagination pattern
- **Client implementation**: Clients need to handle cursor-based navigation

## Examples

### Request with forward pagination

```http
GET /v1/identities?limit=20&after=eyJjcmVhdGVkX2F0IjoiMjAyMy0wMS0wMVQwMDowMDowMFoiLCJpZCI6IjEyMyJ9
```

### Response

```json
{
  "data": [
    // ... array of identity resources
  ],
  "pagination": {
    "has_next_page": true,
    "has_prev_page": true,
    "next_cursor": "eyJjcmVhdGVkX2F0IjoiMjAyMy0wMS0wMVQwMDowMDowMFoiLCJpZCI6IjQ1NiJ9",
    "prev_cursor": "eyJjcmVhdGVkX2F0IjoiMjAyMy0wMS0wMVQwMDowMDowMFoiLCJpZCI6IjEyMyJ9"
  }
}
```

## Implementation

### Pagination Parameters (Standard Across All Services)

**Request parameters:**
- `limit` (integer, optional): Maximum items per page (default 50, max 100).
- `after` (string, optional): Cursor to resume after a specific item.
- `before` (string, optional): Cursor to page backwards before a specific item.

**Response format:**

```json
{
  "items": [...],
  "pagination": {
    "next_cursor": "cursor_xyz789",
    "prev_cursor": "cursor_abc123",
    "has_next_page": true,
    "has_prev_page": true,
    "total_count": 1000
  }
}
```

### Cursor Format

Opaque Base64-encoded JSON:

```json
{
  "v": 1,
  "id": "item_xyz789",
  "created_at": "2025-11-18T06:00:00Z"
}
```

- `v` version allows future evolution.
- Includes sort key (`created_at`) and tie-breaker (`id`).
- Clients treat cursor as opaque token.

### Specification Example (Content Service `/v1/content`)

```yaml
parameters:
  - name: limit
    in: query
    schema:
      type: integer
      default: 50
      maximum: 100
  - name: after
    in: query
    schema:
      type: string
    description: Cursor for forward pagination
  - name: before
    in: query
    schema:
      type: string
    description: Cursor for backward pagination

responses:
  '200':
    content:
      application/json:
        schema:
          type: object
          properties:
            items:
              type: array
            pagination:
              $ref: '#/components/schemas/Pagination'
```

Shared `Pagination` schema appears in every OpenAPI spec with `next_cursor`, `prev_cursor`, `has_next_page`, `has_prev_page`, and optional `total_count`.

### Database Query Pattern

Forward pagination (descending `created_at`):

```sql
SELECT *
FROM content
WHERE created_at < :cursor_created_at
   OR (created_at = :cursor_created_at AND id < :cursor_id)
ORDER BY created_at DESC, id DESC
LIMIT :limit + 1;
```

Backward pagination mirrors the comparison (`>` / ASC). Composite index `(created_at DESC, id DESC)` is required for efficiency.

### Implementation Status

- ✅ All seven OpenAPI specs define cursor parameters and shared pagination schemas.
- ✅ Examples in specs and `examples/edge-cases/` show cursor responses.
- ✅ `docs/requirements/global-standards.md` documents cursor-based pagination.
- ✅ SDKs expose helper methods for iterating via cursors.

## References

- [RFC 5988](https://tools.ietf.org/html/rfc5988) - Web Linking
- [GraphQL Pagination](https://graphql.org/learn/pagination/)
- [Use the Index, Luke](https://use-the-index-luke.com/no-offset)

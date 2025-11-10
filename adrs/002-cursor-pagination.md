# ADR 002: Cursor-Based Pagination for RegistryAccord APIs

## Status

Accepted

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

## References

- [RFC 5988](https://tools.ietf.org/html/rfc5988) - Web Linking
- [GraphQL Pagination](https://graphql.org/learn/pagination/)
- [Use the Index, Luke](https://use-the-index-luke.com/no-offset)

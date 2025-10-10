# Media Specification

Storage
- S3-compatible storage with versioning and lifecycle policies; block public access by default.

Object layout
- s3://ra-media/{env}/{did}/{assetId}/{originalName}

Metadata
- `mimeType`, `size`, `checksum` (SHA-256 hex), `uri`, `createdAt`.

Upload flow
- uploadInit: returns `assetId` and pre-signed URL with expiry.
- finalize: verifies checksum, persists metadata, emits `cdv.media.finalized`.

Access
- Signed URLs for private buckets; short-lived and least privilege.

Limits
- Server-configured max file size and dimensions documented; reject on exceeding limits.

# ADR 004: Content Integrity Hashing

## Status

Accepted

## Summary

RegistryAccord uses SHA-256 cryptographic hashing for all content objects. Each binary payload is hashed before registration, creating immutable identifiers that allow anyone to verify integrity, detect tampering, and deduplicate identical files across the ecosystem. Content hashes live alongside version metadata so lineage stays trustworthy.

This ADR covers integrity hashing enforced by the Content Registry; ADR-012 documents how the Storage Gateway uses the same hashes for content-addressed storage.

## Context

The RegistryAccord Content Registry requires a robust mechanism to ensure content integrity throughout its lifecycle. Content creators, consumers, and intermediaries need to be able to verify that content has not been tampered with or corrupted during storage, transmission, or processing.

Key requirements include:

1. **Immutable Verification**: Content hashes must be cryptographically secure and immutable
2. **Tamper Detection**: Any modification to content must be detectable
3. **Version Tracking**: Each content version must have a unique, verifiable hash
4. **Third-Party Verification**: External parties must be able to independently verify content integrity
5. **Performance**: Hash computation should not significantly impact system performance

We evaluated several hashing algorithms:

- **MD5**: Fast but cryptographically broken, vulnerable to collision attacks
- **SHA-1**: Also cryptographically broken, deprecated for security use
- **SHA-256**: Part of the SHA-2 family, cryptographically secure, widely adopted
- **SHA-3**: Newer standard with different design, but SHA-256 is sufficient
- **BLAKE2**: Fast alternative but less universally supported

## Decision

We will use **SHA-256** for content integrity hashing in the RegistryAccord Content Registry.

### Implementation Details

1. **Hash Generation**:
   - Compute SHA-256 hash of the complete content bytes
   - Represent hash as a 64-character lowercase hexadecimal string
   - Store hash in the ContentVersion object

2. **Hash Verification**:
   - Recompute hash from content bytes when needed
   - Compare with stored hash for verification
   - Reject content if hashes don't match

3. **Version Integrity**:
   - Each ContentVersion includes its SHA-256 hash
   - Parent version references enable lineage verification
   - Immutable hashes prevent version tampering

4. **Third-Party Verification**:
   - Publicly expose content hashes via API
   - Enable independent verification by external tools
   - Support standard SHA-256 hash computation tools

## Consequences

### Positive

- **Security**: SHA-256 is cryptographically secure with no known practical collision attacks
- **Standardization**: Widely supported across platforms, languages, and tools
- **Interoperability**: External systems can easily verify content integrity
- **Tamper Evidence**: Any content modification is immediately detectable
- **Version Safety**: Immutable hashes prevent version history tampering

### Negative

- **Performance**: SHA-256 computation is slower than broken alternatives like MD5
- **Storage**: 256-bit (32-byte) hashes require more storage than smaller hashes
- **Bandwidth**: Hash transmission adds overhead to API responses

### Neutral

- **Industry Standard**: SHA-256 is widely used in blockchain, security, and web applications
- **Tool Support**: Abundant libraries and command-line tools available
- **Future-Proof**: Unlikely to be deprecated soon due to its security properties

## Examples

### Hash Generation

```bash
# Generate SHA-256 hash of a file
sha256sum content.txt
# Output: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  content.txt
```

### API Response with Hash

```json
{
  "data": {
    "id": "z1y2x3w4-5678-90ef-ghij-klmnopqrstuv",
    "content_id": "a1b2c3d4-5678-90ef-ghij-klmnopqrstuv",
    "version_number": 2,
    "parent_version_id": "v1w2x3y4-5678-90ef-ghij-klmnopqrstuv",
    "hash": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
    "size_bytes": 2048000,
    "storage_url": "https://storage.example.com/bucket/image-v2.jpg",
    "metadata": {},
    "created_at": "2025-11-06T12:05:00Z",
    "created_by": "123e4567-e89b-12d3-a456-426614174000"
  }
}
```

## Implementation

### Content Registry Schema

`openapi/content/v1/openapi.yaml` defines `content_hash` on every content record and version:

```yaml
Content:
  type: object
  required: [id, content_hash, storage_url, metadata, created_at]
  properties:
    content_hash:
      type: string
      pattern: ^[a-f0-9]{64}$
      description: SHA-256 hash of content bytes
```

### Client & Gateway Workflow

1. **Client hash:** Creator computes SHA-256 locally before upload (Web Crypto example in spec/examples).
2. **Upload:** Client performs `PUT /v1/storage/objects/hash:{sha256}` with the hash in path/header.
3. **Verification:** Storage Gateway streams upload, recomputes SHA-256, and rejects if mismatch.
4. **Registration:** Client calls `POST /v1/content` referencing the verified hash + storage URL.

### Versioning & Verification

- `ContentVersion` objects store hashes for every revision.
- `GET /v1/content/{id}/verify` downloads from storage and recomputes SHA-256 to confirm integrity.
- Hashes are exposed publicly so third parties can independently validate.

### Deduplication

- Clients may `HEAD /v1/storage/objects/hash:{sha256}` to skip uploads when the hash already exists.
- Multiple content records may reference the same hash/storage URL, conserving bandwidth.

### Implementation Status

- ✅ Content & version schemas require SHA-256 hashes.
- ✅ Storage Gateway endpoints enforce hash-based addressing (see ADR-012).
- ✅ Verification and error responses (`hash-mismatch`) documented in OpenAPI + error catalog.
- ✅ Examples in `examples/content/*` show hashing workflow end-to-end.

## References

- [NIST FIPS 180-4](https://csrc.nist.gov/publications/detail/fips/180/4/final) - Secure Hash Standard (SHA-2)
- [RFC 6234](https://tools.ietf.org/html/rfc6234) - US Secure Hash Algorithms (SHA and SHA-based HMAC and HKDF)
- [OWASP Cryptographic Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html)

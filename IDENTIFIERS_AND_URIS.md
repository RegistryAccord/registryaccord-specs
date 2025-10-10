# Identifiers and URIs

DIDs
- DID method: PLC-derived or equivalent per identity service.
- JWT sessions: `sub=did`, `aud` per service, `exp` reasonable duration.

Record URIs
- Content-addressed `uri` per record returned by CDV on create, with stable dereference semantics.
- `cid` metadata returned alongside `uri` for integrity and caching hints.

Media identifiers
- `assetId` unique within CDV; metadata includes `mimeType`, `size`, `checksum`, `uri`.

Normalization
- Case sensitivity rules documented per field; DID is case-sensitive per method specification.
- URIs must be percent-encoded where applicable and compared by canonical form.

Ownership semantics
- Records and media link to an author DID; authorization checks enforce author or delegated rights.

# Security Policy

Supported artifacts
- Stable schemas and federation docs in this repository are supported for security reports.
- Service implementations have their own security policies and SLAs.

Private disclosure
- Report vulnerabilities via the private channel listed in the organization profile or designated email alias.
- Include reproduction steps, affected artifacts, and impact assessment when possible.
- Expect acknowledgment within 3 business days and status updates as triage proceeds.

Scope
- Identity: DID document integrity, key lifecycle, JWT issuance and verification guidance.
- CDV: schema-enforced write paths and media finalize checksums.
- Events: NATS JetStream subjects, access control, and credentials handling.
- Webhooks: signature verification, replay protection, and deterministic error handling.
- Payments: design-only in Phase 1; report findings confined to specifications and webhook security guidance.

Out-of-scope examples
- Social engineering, physical attacks, and secrets stored outside project control.
- Vulnerabilities in third-party platforms or provider infrastructure.

Best-practice expectations
- TLS 1.3 for transport, strong ciphers.
- Signed artifacts and SBOM in implementations.
- No long-lived secrets in CI; OIDC to cloud favored.

Coordinated disclosure
- Coordinate publication timelines to protect ecosystem users and implementers.

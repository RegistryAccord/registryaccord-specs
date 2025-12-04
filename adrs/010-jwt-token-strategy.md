# ADR-010: JWT Token Strategy with WebAuthn Primary Authentication

- **Status:** Accepted
- **Author:** RegistryAccord Team
- **Created:** 2025-11-18
- **Updated:** 2025-11-18

## Summary
RegistryAccord authenticates end users with WebAuthn/Passkey, authorizes third-party apps through OAuth2/OIDC, and issues short-lived JWT access tokens with refresh token rotation. This layered strategy provides phishing-resistant login, ecosystem-friendly authorization, and high-performance token verification across all services.

## Context
Stakeholders include creators, third-party developers, enterprises, and service-to-service interactions. Password- or email-based flows cannot meet the security bar for high-value creator accounts, while OAuth2 alone does not provide primary authentication. We also require JWTs for high-throughput verification in distributed microservices.

## Decision
1. **Primary Authentication:** WebAuthn (FIDO2) passkeys for direct user login via the Identity service.
2. **Third-Party Authorization:** OAuth2/OIDC Authorization Code (with PKCE) for external apps requesting scoped access.
3. **Token Format:** ES256-signed JWT access tokens (1-hour TTL) plus refresh tokens (30 days) with rotation and revocation APIs.
4. **Claims:** Standard JWT claims (iss, sub, aud, exp, nbf, iat, jti) plus custom fields (scopes, org_id, session_id, auth_method).

## Rationale
- WebAuthn ensures phishing resistance, passwordless UX, and multi-device support.
- OAuth2/OIDC is the industry standard for delegated access and enables SSO federation.
- JWTs enable stateless verification (<200ms p95) across all services and languages.
- Refresh rotation limits token theft blast radius and enables session revocation.

## Consequences
**Positive:** Strong security posture, familiar OAuth2 developer flows, high verification throughput, revocable sessions, enterprise SSO readiness.

**Negative:** Browser/device compatibility considerations, need for account recovery options, increased implementation complexity, and refresh-token storage requirements.

## Alternatives Considered
1. **Password-only:** Rejected due to phishing risk and poor UX.
2. **Magic links / SMS OTP:** Vulnerable to phishing/SIM swap and limited for power users.
3. **Pure OAuth2:** Would defer all auth to third parties, violating decentralization goals.

## Implementation
- Identity endpoints implement WebAuthn registration/login and OAuth2 authorization/token/revoke flows.
- Token management APIs handle refresh, revoke, and verification operations.
- JWTs use ES256 signing; public keys exposed via JWKS for verification.
- SDKs and services cache JWKS and verify tokens locally whenever possible.
- Account recovery mechanisms (social recovery, backup codes) are tracked via future RFC.
- Observability targets: token verification p95 < 200ms, issuance p95 < 500ms.

## References
- `docs/requirements/identity.md`
- WebAuthn, OAuth2 RFC 6749, OIDC Core, JWT RFC 7519
- Identity OpenAPI specification

## Related ADRs
- ADR-001 (WebAuthn primary auth)
- ADR-008 (Versioning for token claims)
- ADR-009 (Service separation relying on shared JWT semantics)

_Last updated: 2025-11-18_

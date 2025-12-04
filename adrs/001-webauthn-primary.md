# ADR-001: WebAuthn as Primary Authentication Method

## Status

Accepted

## Summary

RegistryAccord uses WebAuthn (FIDO2) / Passkey as the primary authentication method for end users logging directly into RegistryAccord services. This provides phishing-resistant, passwordless authentication using device biometrics (TouchID, FaceID, Windows Hello) or security keys.

WebAuthn serves as the foundation for user authentication in the Identity Service, with OAuth2/OIDC as the authorization layer for third-party applications. This two-layer approach balances security (phishing resistance) with ecosystem openness (third-party app access).

## Context

The RegistryAccord Identity Service requires a secure, user-friendly authentication mechanism that protects against phishing, credential theft, and account takeover attacks while providing excellent UX across devices.

## Decision

We have chosen WebAuthn (FIDO2) / Passkey as the primary authentication method for users to authenticate directly with the Identity Service, with OAuth2/OIDC serving as the standard for application authorization.

## Rationale

### Why WebAuthn Primary?

- **Phishing-Resistant**: Cryptographic authentication prevents credential theft
- **Passwordless**: Eliminates password management burden for users
- **Hardware-Backed**: Leverages secure enclaves (TPM, Secure Enclave)
- **Industry Momentum**: Adopted by Google, Apple, Microsoft, GitHub
- **Better UX**: Biometric unlock is faster than passwords

### Why OAuth2/OIDC Secondary?

- **App Authorization**: Standard for 3rd-party app access delegation
- **Enterprise SSO**: SAML/OIDC federation for B2B use cases
- **Universal Compatibility**: Fallback for devices without Passkey support
- **Ecosystem Integration**: Enables "Sign in with Google/Apple" flows

### Authentication vs. Authorization Separation

- **WebAuthn**: "Who are you?" (user proves identity to RA)
- **OAuth2**: "What can you do?" (app requests scoped access on user's behalf)

This separation follows security best practices and enables flexible access control.

## Consequences

### Positive

- Industry-leading security posture
- Reduced support burden (no password resets)
- Future-proof authentication architecture
- Cross-device sync via platform authenticators
- Compliance with NIST AAL2/AAL3 standards

### Negative

- Requires education for users unfamiliar with Passkeys
- Browser/OS compatibility matrix to maintain
- Fallback flows add implementation complexity
- Not all devices support platform authenticators yet

### Mitigation

- Provide clear onboarding flows with Passkey explainers
- OAuth2/OIDC fallback for older devices
- Recovery mechanisms for lost authenticators (social recovery, MPC)
- Comprehensive documentation and example flows

## Alternatives Considered

- **Password + 2FA**: Rejected due to phishing risk and poor UX
- **OAuth2 Primary**: Rejected due to vendor lock-in and lack of true auth
- **DIDs/Decentralized Auth**: Deferred to v2 due to complexity and limited tooling

## Implementation

### Identity Service Endpoints

**WebAuthn Registration:**
- `POST /v1/sessions/webauthn/register/begin` – Start passkey registration. Returns WebAuthn challenge + credential creation options. Input: user ID, display name.
- `POST /v1/sessions/webauthn/register/complete` – Complete passkey registration. Input: signed attestation response from authenticator. Returns credential ID stored for future authentication.

**WebAuthn Authentication:**
- `POST /v1/sessions/webauthn/login/begin` – Start passkey login. Input: user identifier (email or username). Returns WebAuthn challenge + credential request options.
- `POST /v1/sessions/webauthn/login/complete` – Complete passkey login. Input: signed assertion response from authenticator. Returns JWT access token + refresh token.

### Current Implementation Status

- ✅ OpenAPI spec defines all four WebAuthn endpoints in `openapi/identity/v1/openapi.yaml`.
- ✅ Request/response schemas validated against WebAuthn Level 2 spec.
- ✅ Security schemes document JWT token format.

**Example workflow (from spec):**

```typescript
// 1. Start registration
const registerBegin = await fetch('/v1/sessions/webauthn/register/begin', {
  method: 'POST',
  body: JSON.stringify({
    user_id: 'usr_abc123',
    display_name: 'Jane Doe'
  })
})
const { challenge, credential_options } = await registerBegin.json()

// 2. Browser/device creates credential
const credential = await navigator.credentials.create({
  publicKey: credential_options
})

// 3. Complete registration
await fetch('/v1/sessions/webauthn/register/complete', {
  method: 'POST',
  body: JSON.stringify({
    credential,
    challenge
  })
})
```

### Related Implementations

- See ADR-010 for full JWT token strategy (WebAuthn + OAuth2).
- See `openapi/identity/v1/openapi.yaml` for complete API specification.

## References

- W3C WebAuthn Specification: https://www.w3.org/TR/webauthn-2/
- FIDO Alliance: https://fidoalliance.org/
- `docs/requirements/identity.md`: Authentication Strategy
- Passkey Support Matrix: https://passkeys.dev/device-support/

## Related Decisions

- ADR-002: OAuth2 Token Delegation Patterns (planned)
- ADR-003: Account Recovery Mechanisms (planned)

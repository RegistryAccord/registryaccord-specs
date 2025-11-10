# ADR-001: WebAuthn as Primary Authentication Method

## Status

Accepted

## Context

The RegistryAccord Identity Service requires a secure, user-friendly authentication
mechanism that protects against phishing, credential theft, and account takeover
attacks while providing excellent UX across devices.

## Decision

We have chosen WebAuthn (FIDO2) / Passkey as the primary authentication method
for users to authenticate directly with the Identity Service, with OAuth2/OIDC
serving as the standard for application authorization.

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

## References

- W3C WebAuthn Specification: https://www.w3.org/TR/webauthn-2/
- FIDO Alliance: https://fidoalliance.org/
- SPECS_REQUIREMENTS.md Section 5.1: Authentication Strategy
- Passkey Support Matrix: https://passkeys.dev/device-support/

## Related Decisions

- ADR-002: OAuth2 Token Delegation Patterns (planned)
- ADR-003: Account Recovery Mechanisms (planned)

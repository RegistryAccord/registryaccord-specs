# Identity Service Requirements

## 1. Identity Service API

  * **Endpoints:**
      * `/v1/identities`: Create and manage identity records.
      * `/v1/sessions`: Session management.
      * `/v1/tokens`: Token minting and verification.
      * `/v1/orgs`: Organization and team management.
      * `/v1/consents`: Granular consent grant/revoke.
      * `/v1/keys`: Key lifecycle management.
      * `/v1/audit`: Audit event access.
  * **Key Features (Authentication Strategy):**
      * **User Authentication:** **WebAuthn (FIDO2) / Passkey** is the primary, phishing-resistant method for users to authenticate *directly* with the Identity Service.
      * **Application Authorization:** **OAuth2/OIDC flows** are the standard for 3rd-party applications to request scoped access (via JWTs) to act on a user's behalf.
      * **Enterprise Support:** OIDC/OAuth2 flows must support enterprise SSO (e.g., SAML, OIDC) for B2B use cases.
      * **Core Functions:** Keypair lifecycle management, RBAC/ABAC, org/teams hierarchy.
  * **Creator Security Features:**
      * **Account Recovery:** Specs must define robust recovery mechanisms for lost passkeys (e.g., social recovery, MPC-based options).
      * **Stolen Credential Detection:** Service must include hooks for detecting anomalous token usage (e.g., unusual geographic location) and alerting the user.
      * **Secure Delegation:** Define **OAuth2 token delegation patterns** (e.g., token exchange, `grant_type`) for team members to securely manage a central creator account.
  * **Audience Privacy Features:**
      * **Granular Consent:** Must support a taxonomy for consent (e.g., `functional`, `analytics`, `advertising`, `cross-app_sharing`).
      * **Consent Receipts:** Must provide machine-readable proofs of consent for export.
      * **Withdrawal SLA:** Consent withdrawal (e.g., for analytics) must be propagated across all services within **24 hours**.
  * **Non-Functional Requirements (NFRs):**
      * High availability (99.9%+ uptime target).
      * Privacy-by-design architecture.
      * **SLOs:** `<200ms p95` token verification (cached); `<500ms p95` for new token issuance.

## Version History

| Version | Date       | Change Type | Description        | Related ADR |
|---------|------------|-------------|--------------------|-------------|
| 1.0.0   | 2025-12-04 | Initial     | Base Specification | N/A         |

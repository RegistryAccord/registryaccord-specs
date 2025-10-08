# ADR 001: Initial DID Method

* **Status:** Accepted
* **Date:** 2025-10-08

---

### Context

The RegistryAccord protocol requires a decentralized, user-sovereign identity method to ensure a user's identity is a portable asset they control. The solution must balance two key objectives:
1.  Provide a simple, "no-setup" onboarding experience for our primary audience of non-technical creators.
2.  Offer a fully decentralized, self-sovereign option for technically advanced users who wish to have maximum control.

The two primary candidates considered were `did:web` (relying on user-owned domains) and `did:plc` (relying on a managed directory server). A decision is needed on which method to prioritize and offer as the default.

---

### Decision

We will adopt **`did:plc`** as the **default, platform-managed** DID method for the RegistryAccord protocol.

We will also support **`did:web`** as an **optional, self-sovereign** method for users who already own and manage a domain and wish to use it for their identity.

This decision to prioritize `did:plc` is based on the following reasons:

* **Simplified User Onboarding:** It provides a "no-setup" flow that does not require users to purchase or configure a domain name, which is a significant barrier for non-technical creators.
* **Robust Key Management:** A managed `did:plc` server allows the platform to offer user-friendly key rotation and account recovery flows, which is a critical feature for mainstream adoption and aligns with the protocol's goals.
* **Strong Auditability:** The `did:plc` method provides a secure, auditable history of key rotations and document updates, which enhances the security and trustworthiness of the identity layer.

---

### Consequences

* **Positive:**
    * This approach significantly lowers the barrier to entry for our core target audience of creators.
    * It directly supports the guiding principle of "Pragmatic Decentralization" by providing a simple, managed on-ramp while still supporting a fully decentralized alternative.
    * It gives users a clear choice, reinforcing the commitment to "Creator-Centric Ownership".
* **Impact on Roadmap:**
    * The development of a managed `did:plc` server in the `registryaccord-identity-go` repository is now a critical-path deliverable for Phase 1.
    * The `registryaccord-cli-ts` and the future flagship `registryaccord-app` must be designed to handle both `did:plc` and `did:web` identifiers.

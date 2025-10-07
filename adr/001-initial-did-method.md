 ADR 001: Initial DID Method for Phase 1

* **Status:** Accepted
* **Date:** 2025-10-07

---

### ## Context

The RegistryAccord protocol requires a decentralized, user-sovereign identity method to ensure that a user's identity is a portable asset they control, independent of any single service. The primary goals for this identity system are cryptographic verifiability, data portability, and human-readability.

Two primary candidates were considered for the initial implementation:
1.  **`did:plc`**: Provides strong auditability and is managed by a dedicated server, which can simplify key recovery.
2.  **`did:web`**: Uses a standard domain name to host a DID document, relying on existing DNS and HTTPS infrastructure.

A decision is needed on which method to use as the default for the Phase 1 Proof of Concept (PoC) and initial implementation.

---

### ## Decision

We will adopt **`did:web`** as the default DID method for Phase 1 of the RegistryAccord protocol.

This decision is based on the following reasons:
* **Simplicity and Speed:** `did:web` does not require any on-chain transactions or specialized server infrastructure beyond a standard web server. This allows for faster implementation and easier testing during the PoC phase.
* **Alignment with CDV Model:** The method aligns perfectly with the protocol's goal of allowing users to self-host their Creator Data Vault (CDV) on their own domain. A user's identity can be directly tied to the domain where their data resides.
* **Low Barrier to Entry:** It is built on familiar, open standards (DNS, HTTPS, JSON) that are well-understood by the developer community, making it easy for early adopters to create and manage their identities.

---

### ## Consequences

* **Positive:**
    * This choice significantly accelerates the development timeline for the Phase 1 PoC.
    * It reinforces the narrative of user sovereignty by directly linking identity to a user-controlled domain name.
    * The developer experience for the PoC will be simpler, as creating a `did:web` can be easily demonstrated.

* **Trade-offs:**
    * The auditability of identity history is less robust compared to `did:plc`.
    * Identity security is tied to the security of the user's domain name registration and DNS configuration.

* **Future Work:**
    * `did:plc` remains a strong candidate for a future managed identity option provided by RegistryAccord or third-party providers. It can be offered as a high-assurance alternative for users who do not wish to manage their own domain.
    * The key lifecycle runbook must provide clear guidance on securing a domain for use with `did:web`.

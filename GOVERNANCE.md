# RegistryAccord Protocol Governance

### Philosophy & Overview

This document defines the official process for governing changes to the RegistryAccord protocol specifications. Our goal is to ensure the protocol evolves in a stable, transparent, and community-informed manner.

The process outlined here is the initial governance model for the project's early phases ("Architect" and "Community Builder"). It is designed to be lightweight and based on standard open-source practices. We expect this process to evolve into a more formal, community-driven model as the project matures.

### Scope

This governance process applies to all changes to the **Lexicon Schemas** and other core specification documents contained within the `registryaccord-specs` repository.

---

### The Change Process

All substantive changes to the protocol specifications, from fixing a typo to adding a new schema, must follow this process.

Process: Issue (proposal template) → PR (schemas+examples+docs) → Review (N maintainers) → Merge & tag. Stability: DRAFT→STABLE when two independent implementations pass examples under CI. Breaking: publish under a new schema id/version per policy (compatibility first). 

#### **Step 1: Discussion (GitHub Issue)**

* **Start Here:** Before making any changes, you must first open a **GitHub Issue** to describe your proposed change.
* **Purpose:** This allows the community and core maintainers to discuss the proposal, ask questions, and provide early feedback before any code is written.
* **Content:** The issue should clearly describe the problem you are trying to solve and your proposed solution.

#### **Step 2: Proposal (Pull Request)**

* **Implementation:** Once the discussion in the GitHub Issue has reached a consensus, a **Pull Request (PR)** can be opened with the specific changes to the schema files or documents.
* **Link the Issue:** The PR description **must** link back to the original GitHub Issue to provide context for the change.
* **Clear Description:** The PR description should summarize the changes and the rationale behind them.

#### **Step 3: Review**

* **Core Maintainer Review:** The PR will be reviewed by the core protocol maintainers (initially, the founding team).
* **Community Feedback:** We encourage the community to review open PRs and provide feedback.
* **CI Checks:** All PRs must pass the automated CI checks, which include schema validation and conformance tests.

#### **Step 4: Decision & Merge**

* **Consensus:** Once the PR has been approved by at least one core maintainer and any outstanding feedback has been addressed, it will be merged into the `main` branch.
* **Rejection:** A PR may be rejected if it does not align with the protocol's vision, introduces an unnecessary breaking change, or fails to gain consensus. The reasons for rejection will be clearly communicated in the PR.

---

### Schema Versioning

All Lexicon schemas follow **Semantic Versioning 2.0.0 (SemVer)**. The version number is defined in the `$id` field of each schema file (e.g., `com.registryaccord.profile.v1.0.0`).

* **MAJOR** version change (e.g., `1.x.x` -> `2.0.0`): For a breaking change that is not backward-compatible. This requires a formal ADR and significant community discussion.
* **MINOR** version change (e.g., `1.0.x` -> `1.1.0`): For adding new, optional fields or functionality in a backward-compatible manner.
* **PATCH** version change (e.g., `1.0.0` -> `1.0.1`): For backward-compatible bug fixes or clarifications in descriptions.

### ## Architectural Decision Records (ADRs)

Significant, high-impact architectural decisions (such as the choice of a DID method) are documented as **Architectural Decision Records (ADRs)** in the `/adr` directory. The process for proposing a new ADR follows the same Issue -> PR -> Review -> Merge flow.

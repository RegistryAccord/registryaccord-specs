# RegistryAccord Lexicon

### Overview

The Lexicon is the shared language of the RegistryAccord network. It is a collection of schemas that formally define all of the data structures and actions (like posts, profiles, and likes) that can be performed within the protocol.

By providing a clear, versioned, and open set of schemas, the Lexicon ensures that all participants in the ecosystem—from the flagship application to third-party clients and services—can communicate and interoperate reliably. This document provides a high-level overview of the Lexicon's core concepts.

**The formal, machine-readable Lexicon definitions are located in the `schemas/lexicons/` directory as Lexicon v1 JSON files.**

-----

### Core Concepts & Schemas

The protocol is built around a few core data types, or "nouns." Each of these is defined by a specific schema.

  * **Profile:** An entity's self-sovereign identity on the network, controlled by a cryptographic keypair. It contains metadata like a display name, bio, and avatar.
  * **Creator Data Vault (CDV):** A logical, portable container for a Profile's content and data. It is the unit of sovereignty and portability.
  * **Post:** The basic unit of content published by a Profile. It can contain text, attachments, and other metadata.
  * **Like:** An action indicating a Profile's appreciation for a Post.
  * **Follow:** An action representing a directional relationship from one Profile to another.
  * **Comment/Reply:** A Post that is in direct response to another Post, forming a conversation thread.
  * **Repost:** An action where a Profile shares another Profile's Post with their own followers.
  * **ModerationFlag:** An action used to report content for potential policy violations, which can be consumed by Gateway and client applications.

-----

### Naming and Evolution

To ensure clarity and prevent collisions, all schemas use a reverse-domain name identifier (NSID), e.g., `com.registryaccord.profile`.

We evolve schemas additively under the same NSID when changes are backward-compatible. Breaking changes MUST be published under a new NSID, with migration notes tracked in `schemas/INDEX.md` and rationale captured in an ADR. See `GOVERNANCE.md` for the full evolution policy.

### How to Find Schemas

The canonical JSON Schema definitions for all Lexicon types can be found in the [`/schemas`](/schemas) directory of this repository.

### \#\# Contributing

We welcome feedback and proposals for new schemas or changes to existing ones. Please read our main `CONTRIBUTING.md` file for details on how to get involved.

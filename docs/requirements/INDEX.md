# RegistryAccord Specs Repository - Requirements Index

## 1. Repository Overview & Purpose

  * **Repository Name:** `registryaccord-specs`
  * **Visibility:** Public
  * **License:** Apache-2.0
  * **Technology Stack:** TypeScript/JSON, YAML

This repository serves as the **single source of truth** for all API contracts, data schemas, and event definitions for the RegistryAccord (RA) protocol.

## 2. Core Content Requirements

This repository must contain the following artifacts:

### 2.1. OpenAPI 3.1 Specifications
Machine-readable OpenAPI 3.1 definitions for all core RegistryAccord services.

### 2.2. Schema Definitions
JSON Schema Dialect: All data models must use **JSON Schema Draft 2020-12**.

### 2.3. Policy Files
Machine-readable policy files defining scopes and claims.

### 2.4. Examples and Documentation
Example request/response payloads, typed error models, and ADRs.

## 3. Repository Structure

```text
registryaccord-specs/
├── openapi/              # Root for all OpenAPI definitions
├── schemas/              # Common, reusable schemas
├── policies/             # Machine-readable policy files
├── examples/             # Standalone, complex examples
├── tests/
└── adrs/                 # Architecture Decision Records
```

## Detailed Requirements

Please refer to the following documents for detailed requirements:

- **[Global API Standards](global-standards.md)**: Design principles, versioning, security, and observability.
- **[Identity Service](identity.md)**: Authentication, authorization, and user management.
- **[Content Registry](content.md)**: Content CRUD, versioning, and licensing.
- **[Storage Service](storage.md)**: Object storage and upload management.
- **[Payments Service](payments.md)**: Payments, payouts, and ledgers.
- **[Feeds Service](feeds.md)**: Feed generation, ranking, and fairness.
- **[Revenue Service](revenue.md)**: Advertising, bidding, and reporting.
- **[Analytics Service](analytics.md)**: Event ingestion and metrics.

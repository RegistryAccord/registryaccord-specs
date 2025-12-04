# Changelog

All notable changes to the RegistryAccord specifications will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.0.0] - 2025-11-07

### Added
- **Fairness & Transparency Framework**
  - Major Update: Comprehensive fairness, accountability, and transparency requirements for ranking algorithms and feed systems.
  - **New Feed Generator Endpoints**
    - `GET /v1/feeds/scorecards/{ranker_id}` - Public fairness scorecard retrieval
    - `GET /v1/feeds/audits/{ranker_id}` - Audit history and results
    - `POST /v1/feeds/disputes` - Fairness dispute submission
    - `GET /v1/feeds/disputes/stats` - Aggregated dispute statistics (public)
  - **New Schemas**
    - `schemas/audits/fairness-scorecard.json` - Public scorecard data model
    - `schemas/audits/audit-report.json` - Independent audit report structure
    - `schemas/audits/dispute-submission.json` - Dispute submission schema
    - `schemas/audits/dispute-outcome.json` - Dispute resolution outcome
  - **Fairness Audit Framework (Section 6.4)**
    - Independent Auditing: Semi-annual third-party audits mandatory
    - Platform-Pooled Funding: 1-3% of platform revenue allocated to audit fund
    - Auditor Rotation: 3-year maximum tenure with 1-year cooling-off
    - Audit Transparency: Standardized report format with public publication
    - Three-Tier Dispute Resolution: 2/10/20-day SLAs for standard/escalated/ombudsperson
  - **Algorithmic Fairness Requirements (Section 5.5)**
    - Quarterly automated + manual fairness testing
    - Public fairness metrics (demographic parity, content equity, engagement fairness)
    - Progressive violation consequences (warning → suspension → delisting)
    - IP protection balanced with auditor access requirements
  - **Transparency Features (Section 9.4)**
    - Public scorecards with certification status
    - Quarterly transparency reports on disputes
    - Audit findings publication (anonymized)
    - Free dispute filing (refundable fee for repeat filers)
  - **Examples**
    - 4 new fairness workflow examples demonstrating scorecard access, dispute submission, and audit history retrieval
- **Changed**
  - Updated requirements from v1.0 to v2.0 with comprehensive fairness requirements
- **Security & Privacy**
  - No changes to existing security or privacy baselines
  - Fairness framework enhances transparency without compromising builder IP protection

## [1.6.0] - 2025-11-06

### Added
- **Analytics Service (Section 5.7)**
  - Complete OpenAPI 3.1 specification with 12 endpoints
  - Event ingestion with context enrichment
  - Metrics querying with dimensions and filters
  - Schema registry for event validation
  - Data export jobs with multiple formats
  - Privacy budget management with differential privacy
  - 11 data models (Event, MetricQuery, MetricResult, SchemaDefinition, ExportRequest, ExportJob, PrivacyBudget, PrivacyBudgetAdjustment, Error, Pagination)
  - 4 workflow examples demonstrating all functionality
  - 10 OAuth 2.0 scopes following Principle of Least Privilege

## [1.5.0] - 2025-11-06

### Added
- **Revenue Services (Section 5.6)**
  - Complete OpenAPI 3.1 specification with 22 endpoints
  - Campaign and line item management
  - Audience segmentation
  - Creative management with checksum verification
  - Real-time bidding (RTB) with auction mechanics
  - Impression and click event tracking
  - Performance reporting and attribution
  - Budget management with daily caps
  - IVT (Invalid Traffic) refund processing
  - 12 data models (Campaign, LineItem, Segment, Creative, AuctionRequest, AuctionResult, ImpressionEvent, ClickEvent, CampaignReport, AttributionReport, BudgetStatus, IvtRefund)
  - 3 workflow examples demonstrating all functionality
  - 12 OAuth 2.0 scopes following Principle of Least Privilege

## [1.4.0] - 2025-11-06

### Added
- **Feed Generator Service (Section 5.5)**
  - Complete OpenAPI 3.1 specification with 10 endpoints
  - Personalized feed generation with multiple ranking algorithms
  - Custom signal registration and management
  - A/B testing for ranking algorithms
  - Cached feed retrieval
  - 6 data models (FeedQuery, FeedItem, RankingSignal, Experiment, Error, Pagination)
  - 3 workflow examples demonstrating all functionality
  - 10 OAuth 2.0 scopes following Principle of Least Privilege

## [1.3.0] - 2025-11-06

### Added
- **Storage Gateway Service (Section 5.4)**
  - Complete OpenAPI 3.1 specification with 14 endpoints
  - Bucket management with encryption and versioning
  - Object lifecycle management
  - Multipart upload with checksum verification
  - Presigned URL generation
  - RTBF (Right to be Forgotten) cascade delete
  - 9 data models (Bucket, Object, Upload, Checksum, Encryption, Error, Pagination)
  - 4 workflow examples demonstrating all functionality
  - 10 OAuth 2.0 scopes following Principle of Least Privilege

## [1.2.0] - 2025-11-06

### Added
- **Payments & Payouts Service (Section 5.3)**
  - Complete OpenAPI 3.1 specification with 26 endpoints
  - Payment intents with idempotency and fraud detection
  - Charges with capture and refund workflows
  - Subscription billing with recurring payments
  - Double-entry ledger accounting for audit trails
  - Payout processing with fraud hold capabilities
  - Dispute resolution with escalation paths
  - Revenue split rules for creator monetization
  - 8 data models (PaymentIntent, SplitRule, Charge, Subscription, LedgerEntry, Payout, Dispute, ErrorDetail)
  - 6 workflow examples demonstrating all functionality
  - 11 OAuth 2.0 scopes following Principle of Least Privilege
  - 3 fraud event schemas (fraud-detected, payout-held, dispute-created)
  - ADR-005 documenting Double-Entry Ledger Accounting approach

### Changed
- Enhanced validation scripts with Payments & Payouts support
- Updated README.md and CHANGELOG.md with Payments & Payouts information
- Updated package.json with Payments & Payouts linting scripts
- Updated policies/scopes.json with Payments & Payouts scopes

## [1.1.0] - 2025-10-27

### Added

#### Content Registry v1: Complete OpenAPI 3.1 specification with 20 endpoints
- Content management (CRUD operations with soft delete)
- Version management (lineage tracking, immutable hashes)
- Collection management (grouping and organization)
- License management (Creative Commons support)
- Lifecycle webhooks (real-time event subscriptions)

#### Examples: 6 complete workflow examples for Content Registry
- Content creation and management
- Version lineage tracking
- Collection workflows
- License attachment
- Content provenance verification
- Webhook subscriptions

#### JSON-LD Schemas: Schema.org definitions for Article, Video, Image

#### Event Schemas: Webhook payload definitions for lifecycle events
- content-created.json
- version-created.json
- license-attached.json
- content-deleted.json

#### Content Registry Scopes: 9 fine-grained OAuth2 scopes
- content:read, content:write, content:delete
- content:version, collection:read, collection:write
- license:read, license:write, event:subscribe

#### Standards Compliance
- Schema.org for semantic metadata
- Creative Commons license framework
- SHA-256 cryptographic hashing
- HMAC-SHA256 webhook signature verification

## [1.0.0] - 2025-11-06

### Added

#### Core Identity Service Specification
- **OpenAPI 3.1 Specification**: Complete API contract for all 22 Identity Service endpoints
  - Identity Management (create, resolve, update, delete)
  - Session Management (WebAuthn/Passkey authentication)
  - Consent Framework (4 consent types with granular controls)
  - Token Operations (OAuth 2.0 access tokens)
  - Audit Trail (immutable event logging)
  - Organization Management (multi-tenant support)
  - Key Lifecycle (cryptographic key management)

#### Data Models and Schemas
- **JSON Schema Definitions**: Formal schemas for all data models
  - Identity, Session, Token, Consent, AuditEvent, Organization, Member, Key
  - Error catalog with RFC 7807 compliant problem details
  - Pagination and metadata structures

#### Security Framework
- **OAuth 2.0 Scopes**: 21 fine-grained scopes following Principle of Least Privilege
- **RBAC Rules**: Role definitions for User, Admin, Service, and Auditor roles
- **Error Handling**: Standardized error responses with trace IDs
- **Rate Limiting**: Headers for client-side rate limit management

#### Documentation and Examples
- **Workflow Examples**: 8 comprehensive YAML examples demonstrating:
  - Create Identity flow
  - OAuth 2.0 Authorization Code flow
  - WebAuthn/Passkey authentication
  - Consent management (grant, list, revoke)
  - Token operations (mint, verify, refresh, revoke)
  - Audit event querying with filtering and pagination
  - Organization management (create, add member, update role, remove)
  - Key lifecycle (generate, rotate, list, revoke)

#### Validation and Tooling
- **Spectral Linting Rules**: Custom rules for API specification quality
- **Validation Scripts**: Automated validation for specification compliance
- **GitHub Actions Workflow**: Continuous validation of specifications

#### Architecture Decision Records
- **ADR-001**: WebAuthn as Primary Authentication Method

#### Repository Structure
- **Standardized Layout**: Organized directories for OpenAPI specs, schemas, examples, policies, and ADRs
- **Comprehensive README**: Detailed documentation with repository overview and quick start guide

### Changed

- **Repository Documentation**: Enhanced README with complete feature list and usage instructions
- **Security Policies**: Updated security guidelines with comprehensive vulnerability reporting guidelines

### Deprecated

- None

### Removed

- None

### Fixed

- **OpenAPI Validation**: Resolved all OpenAPI 3.1 validation errors
- **Spectral Rules**: Removed invalid Spectral linting rules

### Security

- **Authentication**: JWT tokens with required jti and kid claims
- **Authorization**: OAuth 2.0 with fine-grained scope controls
- **Cryptography**: Ed25519 key support with proper key lifecycle management
- **Rate Limiting**: Client-aware rate limiting with header exposure

## [Unreleased]

### Planned

- **Content Registry Service**: Specifications for content management and verification
- **Payments Service**: API contracts for payment processing and settlement
- **Additional ADRs**: Documentation of key architectural decisions
- **Enhanced Examples**: Additional workflow examples for advanced scenarios
- **Performance Guidelines**: Recommendations for service implementation optimization

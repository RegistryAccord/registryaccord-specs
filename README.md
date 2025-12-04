# RegistryAccord Specifications

[![Validate Specifications](https://github.com/RegistryAccord/registryaccord-specs/actions/workflows/validate.yml/badge.svg)](https://github.com/RegistryAccord/registryaccord-specs/actions/workflows/validate.yml)
[![Detect Breaking Changes](https://github.com/RegistryAccord/registryaccord-specs/actions/workflows/breaking-changes.yml/badge.svg)](https://github.com/RegistryAccord/registryaccord-specs/actions/workflows/breaking-changes.yml)
[![Check Links](https://github.com/RegistryAccord/registryaccord-specs/actions/workflows/link-check.yml/badge.svg)](https://github.com/RegistryAccord/registryaccord-specs/actions/workflows/link-check.yml)
[![Dependabot Updates](https://img.shields.io/badge/Dependabot-active-brightgreen)](https://github.com/RegistryAccord/registryaccord-specs/pulls/app%2Fdependabot)

This repository serves as the **single source of truth** for all API contracts, data schemas, and event definitions for the RegistryAccord (RA) protocol.

Its primary purpose is to define the ecosystem's interface in a machine-readable way, enabling:

* **SDK Generation**: Automatically generating idiomatic client SDKs for multiple languages.
* **Contract Testing**: Validating that services are compliant with the protocol.
* **Mocks & Tooling**: Allowing developers to build and test integrations using mock servers.
* **Documentation**: Serving as the foundation for all API reference documentation.

## 📁 Repository Structure

```
registryaccord-specs/
├── openapi/              # OpenAPI 3.1 specifications
│   ├── identity/v1/      # ✅ Identity Service (Phase 1 - Complete)
│   ├── content/v1/       # ✅ Content Registry (Phase 2 - Complete)
│   ├── payments/v1/      # 📋 Payments (Phase 3 - Planned)
│   └── ...               # Other services
├── schemas/              # Common, reusable schemas
│   ├── jsonld/           # Semantic content type definitions
│   ├── events/           # Asynchronous event schemas
│   ├── errors/           # Error catalog definitions
│   ├── brand-safety/     # IAB Content Taxonomy definitions
│   └── fraud/            # IVT and fraud event definitions
├── policies/             # Machine-readable policy files (scopes, etc.)
├── examples/             # Standalone, complex examples
│   └── content/          # Content Registry examples
├── tests/
│   └── conformance/      # Conformance test fixtures
└── adrs/                 # Architecture Decision Records
```

## 🚀 Quick Start

1. **Install dependencies**:
   ```bash
   npm install
   ```

2. **Validate specifications**:
   ```bash
   npm run validate
   ```

3. **Lint specifications**:
   ```bash
   npm run lint
   ```

## 📚 Documentation

* [SPECS_REQUIREMENTS.md](SPECS_REQUIREMENTS.md) - Detailed specification requirements
* [SECURITY.md](SECURITY.md) - Security policies and vulnerability reporting
* [Architecture Decision Records](adrs/) - Key architectural decisions

## SDKs

Official SDKs maintained in separate repositories:

* TypeScript - `npm install @registryaccord/sdk`
* Python - `pip install registryaccord`
* Go - `go get github.com/registryaccord/sdk-go`

See [docs/SDK-GENERATION.md](docs/SDK-GENERATION.md) for details.

## 🔭 Observability

All services must propagate Trace Context and correlation IDs and follow shared logging/metrics schemas:

* Trace Context & correlation IDs – [`docs/OBSERVABILITY.md`](docs/OBSERVABILITY.md)
* Schemas – `schemas/observability/trace-context.json`, `logging-standards.json`, `metrics-standards.json`, `health-checks.json`

Each OpenAPI spec imports reusable `traceparent`, `tracestate`, and `X-Correlation-ID` headers so SDKs and implementations expose a consistent contract.

## 🔧 Validation

* **Spectral linting rules** for API specification quality
* **Automated validation scripts** for specification compliance
* **GitHub Actions workflow** for continuous validation
* **Conformance test harness** for service compliance

## 🛡️ Security & Privacy

* **Zero Trust Architecture** with mTLS and TLS 1.3
* **Privacy by Design** with purpose limitation and differential privacy
* **Right to Erasure** with 30-day deletion SLA
* **Data Residency** APIs for sovereignty compliance

## 🤝 Contribution

We welcome contributions to the RegistryAccord specifications. Please see our contribution guidelines for how to get involved.

## 📄 License

This project is licensed under the Apache 2.0 License - see the [LICENSE](LICENSE) file for details.

## 🌐 Community

* **GitHub Issues**: Report bugs or request features
* **Discussion Forums**: Community discussions and support
* **Working Groups**: Participate in protocol development
* **RFC Process**: Contribute to major design decisions

## 📊 Current Status

| Service    | Status      | Version | Completion Date |
|------------|-------------|---------|-----------------|
| Identity   | ✅ Complete  | v1.0.0 | 2025-10-20 |
| Content    | ✅ Complete  | v1.1.0 | 2025-10-27 |
| Payments & Payouts | ✅ Complete | v1.2.0 | 2025-11-06 |
| Storage    | ✅ Complete   | v1.3.0 | 2025-11-06 |
| Feeds      | ✅ Complete   | v1.4.0 | 2025-11-06 |
| Revenue    | ✅ Complete   | v1.5.0 | 2025-11-06 |
| Analytics  | ✅ Complete   | v1.6.0 | 2025-11-06 |

## 📊 Complete Specification Coverage

### Services Implemented: 7/7 ✅

| Service | Version | Endpoints | Examples | Status |
|---------|---------|-----------|----------|--------|
| Identity | v1.0.0 | 22 | 8 workflows | ✅ Complete |
| Content Registry | v1.0.0 | 20 | 6 workflows | ✅ Complete |
| Payments & Payouts | v1.0.0 | 26 | 6 workflows | ✅ Complete |
| Storage Gateway | v1.0.0 | 12 | 4 workflows | ✅ Complete |
| Feed Generator | v1.0.0 | 7 | 3 workflows | ✅ Complete |
| Revenue Services | v1.0.0 | 16 | 3 workflows | ✅ Complete |
| Analytics | v1.0.0 | 11 | 4 workflows | ✅ Complete |
| **Total** | **v2.0.0** | **114** | **34** | ✅ **Production Ready** |

### Schema Coverage

* **JSON Schemas**: 50+ data models
* **JSON-LD Schemas**: 3 semantic types (Article, Video, Image)
* **Event Schemas**: 10+ lifecycle events
* **Brand Safety**: IAB Taxonomy v3.0 + adjacency controls
* **Fraud Detection**: 3 fraud event types
* **Error Catalog**: RFC 7807 compliant

### Security & Privacy

* **OAuth2 Scopes**: 60+ fine-grained scopes
* **RBAC Policies**: User, Admin, Service, Auditor roles
* **Privacy Guarantees**: Differential privacy, RTBF, consent management
* **Security Standards**: OWASP API Top 10, PCI DSS (delegated), TAG IVT

### Standards Compliance

* ✅ OpenAPI 3.1.0
* ✅ JSON Schema Draft 2020-12
* ✅ RFC 7807 (Problem Details)
* ✅ RFC 8594 (Deprecation Headers)
* ✅ OAuth 2.0 & OIDC
* ✅ W3C Trace Context
* ✅ OpenTelemetry Semantic Conventions
* ✅ ISO 8601 Timestamps
* ✅ ISO 4217 Currency Codes
* ✅ IAB Content Taxonomy v3.0
* ✅ TAG IVT Guidelines
* ✅ MRC Viewability Standards
* ✅ Schema.org for Metadata

### Repository Health

* **Lines of Specification**: 25,000+
* **Validation Status**: ✅ All specs pass Spectral linting
* **CI/CD**: ✅ GitHub Actions automated validation
* **Documentation**: ✅ Comprehensive README, CHANGELOG, ADRs
* **Examples**: ✅ 34 complete workflow examples
* **Test Fixtures**: ✅ Conformance test structure ready

### 🎯 Next Steps

Now that all specifications are complete:

* **SDK Generation** (Phase 5a)
  * Generate TypeScript SDK: `registryaccord-sdk-ts`
  * Generate Python SDK: `registryaccord-sdk-py`
  * Generate Go SDK: `registryaccord-sdk-go`
  * Generate Java SDK: `registryaccord-sdk-java`
  * Generate .NET SDK: `registryaccord-sdk-dotnet`
* **Conformance Harness** (Phase 5b)
  * Build automated test harness: `registryaccord-conformance`
  * Implement security scorecard
  * Create public dashboard
* **Reference Implementation** (Phase 5c)
  * Build reference implementations for validation
  * Deploy to staging environment
  * Document deployment patterns
* **Documentation Site** (Phase 5d)
  * Generate API reference documentation
  * Create interactive API explorer
  * Publish integration guides
* **Community Launch** (Phase 6)
  * Public announcement
  * RFC process activation
  * TSC formation
  * Ecosystem builder onboarding

## 🔧 Services

### 1. Identity Service (Section 5.1)

Authentication, authorization, consent management, and audit.

**Key Features:**
- WebAuthn/Passkey primary authentication
- OAuth2/OIDC flows for apps
- Granular consent with 24hr withdrawal SLA
- RBAC/ABAC with fine-grained scopes

**Endpoints:** 22 (all documented)

### 2. Content Registry (Section 5.2)

Structured, versioned, licensed digital content with provenance.

**Key Features:**
- JSON-LD semantic metadata
- Version control with diff/merge
- License attachment and enforcement
- Content collections
- Webhook subscriptions
- Provenance tracking

**API Coverage:** 100% of Section 5.2 requirements

### 3. Payments & Payouts (Section 5.3)

Global payments infrastructure with fraud detection and dispute resolution.

**Key Features:**
- PCI-compliant payment processing
- Idempotent payment intents
- Revenue split rules
- Subscription billing
- Double-entry ledger accounting
- Payout fraud holds
- Dispute workflows
- Programmable fraud hooks

**API Coverage:** 100% of Section 5.3 requirements

### 4. Storage Gateway (Section 5.4)

Distributed, encrypted, content-addressed storage with streaming.

**Key Features:**
- Content-addressed (SHA-256) deduplication
- End-to-end encryption
- Streaming upload/download
- Resumable transfers
- CDN integration
- Retention policies
- KMS integration
- Checksum verification

**API Coverage:** 100% of Section 5.4 requirements

**OpenAPI Spec:** `openapi/storage/v1/openapi.yaml`
**Examples:** `examples/storage/`

### 5. Feed Generator (Section 5.5)

Personalized, algorithmic feeds with real-time updates.

**Key Features:**
- Timeline and algorithmic ranking
- Real-time event streaming
- Custom feed definitions
- Engagement metrics
- Content moderation
- Trending topics
- A/B testing for ranking algorithms
- Custom rankers

**API Coverage:** 100% of Section 5.5 requirements

**OpenAPI Spec:** `openapi/feeds/v1/openapi.yaml`
**Examples:** `examples/feeds/`

### 6. Revenue Services (Section 5.6)

Advertising platform with real-time bidding, brand safety, viewability, and IVT detection.

**Key Features:**
- Real-time bidding (RTB) with fraud detection
- Brand safety and viewability measurement
- Invalid Traffic (IVT) detection and refunds
- Campaign and budget management
- Performance reporting and attribution
- A/B testing for ad creatives

**API Coverage:** 100% of Section 5.6 requirements

**OpenAPI Spec:** `openapi/revenue/v1/openapi.yaml`
**Examples:** `examples/revenue/`

### 7. Analytics Service (Section 5.7)

Event ingestion, metrics querying, and privacy-compliant analytics with differential privacy.

**Key Features:**
- Event collection and schema registry
- Metrics querying with dimensions and filters
- Data export jobs
- Differential privacy with privacy budget management
- A/B testing
- Cohort analysis

**API Coverage:** 100% of Section 5.7 requirements

**OpenAPI Spec:** `openapi/analytics/v1/openapi.yaml`
**Examples:** `examples/analytics/`

## 🤝 Contributing

We welcome contributions! Please see:
- `CONTRIBUTING.md` - How to contribute
- `CODE_OF_CONDUCT.md` - Community standards
- `GOVERNANCE.md` - Decision-making process

### RFC Process

Major changes require an RFC (Request for Comments):
1. Create RFC document in `rfcs/`
2. Submit PR
3. 14-day public comment period
4. TSC vote for acceptance

## 📖 Documentation

- **Full Requirements**: `SPECS_REQUIREMENTS.md`
- **API Design Standards**: See Section 4 of requirements
- **Service Specifications**: See Section 5 of requirements

## 🔒 Security

For security vulnerabilities, see `SECURITY.md`.

## 📄 License

Apache-2.0 - See `LICENSE`

## 🔗 Links

- GitHub: https://github.com/RegistryAccord/registryaccord-specs
- Documentation: https://docs.registryaccord.com (coming soon)
- Conformance Harness: `registryaccord-conformance` (separate repo, planned)
- SDKs: Separate language-specific repositories (e.g., `registryaccord-sdk-ts`, `registryaccord-sdk-py`, `registryaccord-sdk-go`)

## 💬 Community

- GitHub Discussions: https://github.com/RegistryAccord/registryaccord-specs/discussions
- Issues: https://github.com/RegistryAccord/registryaccord-specs/issues

Built with ❤️ by the RegistryAccord community

## 🤖 AI-Native Development

This repository is optimized for AI-assisted development. Whether you use Cursor, Windsurf, Claude, or any other AI coding assistant:

### Quick Start for AI Agents
1. **Read First**: `AGENTS.md` - Your entry point.
2. **Workflows**: Check `.ai/prompts/` for task templates.
3. **Rules**: Follow `.ai/rules/generic-rules.md`.

### For Humans
- **Requirements**: `docs/requirements/*.md`
- **Style Guide**: `.ai/knowledge/style-guide.md`
- **Validation**: Run `npm run lint` (if spectral is configured)

### Common AI Commands
```bash
# Draft a new OpenAPI spec
# Ask AI: "Use .ai/prompts/draft-openapi.md to create a new Users API spec"

# Review a PR
# Ask AI: "Use .ai/prompts/spec-review.md to review this PR"

# Validate specs
# Ask AI: "Use .ai/prompts/validate-specs.md to check all YAML files"
```

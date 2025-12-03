# ADR-009: Seven-Service Architecture (Not Monolithic)

- **Status:** Accepted
- **Author:** RegistryAccord Team
- **Created:** 2025-11-18
- **Updated:** 2025-11-18

## Summary
RegistryAccord defines seven independent service APIs—Identity, Content, Storage, Payments, Feeds, Revenue, and Analytics—instead of a single monolithic interface. Each has its own OpenAPI spec, authentication scopes, and conformance tests. The architecture allows ecosystem builders to implement only the services they need, scale workloads independently, and maintain clear compliance boundaries.

## Context
Goals for the protocol include modular adoption, decentralized implementations, regulatory isolation (e.g., PCI only for payments), and technology flexibility. Use cases range from full-stack deployments to niche providers (e.g., algorithmic feed services) that rely on other operators for the remaining capabilities. A monolithic API would force all-or-nothing adoption and tightly couple scaling, compliance, and technology choices.

## Decision
Publish and maintain seven separate OpenAPI specifications located under `openapi/<service>/v1/openapi.yaml`, each secured via JWTs issued by the Identity service. Service-to-service calls use REST over HTTPS with mTLS, propagate W3C Trace Context headers, and include `X-Correlation-ID`. Conformance suites, policy files, and SDK surface areas mirror this separation.

## Rationale
1. **Modular implementation:** Builders can deploy subsets (e.g., Identity + Content) without running Feeds or Analytics.
2. **Independent scaling:** Services exhibit unique performance profiles (e.g., Identity = read-heavy token checks; Analytics = write-heavy ingestion) and can be scaled accordingly.
3. **Compliance isolation:** Payments handles PCI scope; Analytics and Identity satisfy GDPR residency requirements independently.
4. **Technology diversity:** Teams can choose optimal stacks per service (Go for Identity, Rust for Storage, Python for Feeds experimentation, etc.).
5. **Ecosystem diversity:** Multiple vendors can interoperate—one might specialize in Feeds, another in Payments—while remaining protocol-compliant.

## Consequences
**Positive:** Modular adoption, better scaling economics, clearer compliance boundaries, easier ownership per team, and improved ecosystem interoperability.

**Negative:** Larger overall API surface area, increased operational complexity (seven deployments/monitoring stacks), and the need for orchestration across services which can introduce latency and distributed transaction considerations.

## Alternatives Considered
1. **Monolithic API:** Simpler docs and zero inter-service latency but fails modularity/compliance goals.
2. **Shared database microservices:** Tighter coupling via shared schemas undermines bounded contexts and creates a single point of failure.
3. **Pure event-driven design:** Provides strong decoupling but increases implementation complexity for v1; REST remains primary with events layered on later.

## Implementation
- Repository structure already mirrors the separation (`openapi/identity`, `openapi/content`, etc.).
- Security schemes reference Identity-issued JWTs with service-scoped permissions.
- Conformance tests live under `tests/conformance/<service>/` and certify each API independently.
- SDKs offer namespaced clients (e.g., `client.identity.*`, `client.content.*`).
- Cross-service workflows (e.g., content publish flow) rely on trace propagation for observability.

## References
- `SPECS_REQUIREMENTS.md` §§3 & 5
- OpenAPI specs in `openapi/*/v1/`
- Policy files defining scopes per service

## Related ADRs
- ADR-001 (WebAuthn) – Identity service auth baseline
- ADR-003 (RFC 7807 Errors) – consistent envelope across services
- ADR-008 (Hybrid Versioning) – applies uniformly to all specs

_Last updated: 2025-11-18_

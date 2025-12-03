# ADR-007: Fairness Audit Framework for Ranking Algorithms

## Status

Accepted

## Summary

RegistryAccord requires semi-annual independent fairness audits for all widely deployed feed ranking algorithms (rankers). Audits assess demographic bias, content equity, and compliance with published documentation, with results exposed via public scorecards. This framework enforces algorithmic accountability, funds audits through a neutral pool, and provides a structured dispute process.

## Context

The RegistryAccord ecosystem supports pluggable ranking algorithms and feed generators, allowing third-party builders to develop custom rankers. This flexibility creates a potential conflict of interest when builders control both the audience app and the ranking algorithm.

Without independent oversight, there is a risk of:
- Algorithmic bias disadvantaging certain demographic groups or content types
- Manipulation for commercial gain or competitive advantage
- Lack of accountability due to proprietary "black box" algorithms
- Erosion of trust among creators, users, and regulators

We needed a comprehensive fairness framework that:
- Ensures independent, regular audits of all deployed rankers
- Funds audits through a neutral, platform-pooled mechanism
- Provides transparent dispute resolution with clear SLAs
- Balances IP protection with auditor access requirements
- Publishes fairness metrics for external oversight

## Decision

We will implement a mandatory, independent fairness audit framework for all certified ranking plugins and feed systems in the RegistryAccord ecosystem.

### 1. Independent Auditing Requirements

**Frequency:** Semi-annual audits for all widely deployed rankers

**Independence:**
- Auditors selected by RA governance board
- Zero financial ties to ranker owners
- Maximum 3-year tenure per ranker
- 1-year cooling-off period before re-engagement

**Scope:**
- Signal definitions and weighting mechanisms
- Historical performance across demographic groups
- Compliance with published documentation
- Dispute handling processes
- A/B test methodology and statistical validity

### 2. Platform-Pooled Audit Funding

**Funding Source:** 1-3% of platform revenue (transaction fees, ad revenue, subscriptions)

**Rationale:**
- Eliminates conflicts of interest (ranker owners don't pay auditors directly)
- Ensures consistent funding regardless of ranker profitability
- Enables emergency audits without budget constraints

**Governance:**
- Audit fund managed by RA governance board
- Annual review and transparent publication of allocation
- Emergency audit provisions for critical issues

### 3. Three-Tier Dispute Resolution

**Tier 1 (Standard):**
- 2-day acknowledgment
- 10-day resolution
- Platform review + ranker owner response

**Tier 2 (Escalated):**
- 20-day resolution
- Independent appeals board review
- Detailed outcome publication

**Tier 3 (Ombudsperson):**
- 30-day binding decision
- Neutral external ombudsperson
- Full case study published (anonymized)

### 4. Public Transparency

**Fairness Scorecards:** Public API (`/v1/feeds/scorecards/{ranker_id}`) with:
- Demographic parity metrics (0-100 score)
- Content equity metrics
- Engagement fairness metrics
- Certification status (CERTIFIED, SUSPENDED, REVOKED)
- Violation history
- Active dispute count

**Audit Reports:** Published with standardized format including:
- Executive summary
- Methodology
- Findings by category (severity levels)
- Remediation recommendations
- Auditor conflict-of-interest statement

**Quarterly Reports:** RA governance publishes:
- Total disputes filed/resolved
- Breakdown by dispute type
- Average resolution times
- Actions taken (warnings, suspensions, revocations)
- Audit fund utilization

### 5. IP Protection Balance

**Auditor Access:** Full access to ranker logic under NDA:
- Signal definitions and weightings
- Historical performance data
- Anonymized user-impact data

**Proprietary Protection:**
- NDAs protect commercially sensitive methods
- Only necessary details for fairness review disclosed
- Public reports anonymized and aggregated

**Non-Negotiable:** Refusal to provide auditor access = immediate decertification

### 6. Progressive Violation Consequences

1. **1st Violation:** Public warning + mandatory re-audit
2. **2nd Violation:** 30-day marketplace suspension
3. **3rd Violation:** Certification revoked, ranker delisted

### 7. Filing Cost Structure

- **First-time complainants:** Free
- **Repeat filers (3+ disputes in 90 days):** Refundable fee (returned if upheld)

**Rationale:** Prevents system abuse while maintaining accessibility

## Consequences

### Positive

**For Creators:**
- Objective recourse against perceived unfairness
- Transparent fairness metrics inform platform choice
- Confidence that bias is monitored and addressed

**For Users:**
- Assurance that ranking algorithms meet fairness standards
- Visibility into dispute resolution processes
- Trust in ecosystem governance

**For Builders:**
- Clear certification requirements
- IP protection while demonstrating fairness
- Level playing field (all rankers subject to same standards)

**For the Ecosystem:**
- Industry-leading algorithmic accountability
- Differentiation from opaque, proprietary platforms
- Regulatory compliance (anticipated AI/algorithm transparency laws)
- Foundation for neutral governance transition

### Negative

**Implementation Complexity:**
- Requires audit fund management infrastructure
- Ongoing governance board operational overhead
- Auditor onboarding and training

**Cost:**
- 1-3% platform revenue is significant (~$1-3M annually at $100M revenue)
- Audit fund reserves must cover 12 months of costs

**Potential Friction:**
- Builders may resist auditor access requirements
- Disputes may create adversarial dynamics
- False positives in fairness testing

### Mitigation

**Complexity:**
- Start with 2-3 certified auditors
- Standardized audit playbooks
- Automated fairness testing supplements manual reviews

**Cost:**
- Transparent ROI analysis (trust = user retention = revenue)
- Gradual fund buildup (start at 1%, scale to 3%)
- Audit efficiency improvements over time

**Friction:**
- Clear IP protection guarantees via NDAs
- Appeal mechanisms prevent arbitrary decisions
- Collaborative remediation (not punitive) for first violations

## Alternatives Considered

### 1. Self-Certification Only

**Rejected:** Conflicts of interest unaddressed, low trust

### 2. Reactive-Only Audits (Post-Complaint)

**Rejected:** Allows bias to persist until reported, reactive not proactive

### 3. Ranker-Funded Audits

**Rejected:** Creates perverse incentives, auditors beholden to ranker owners

### 4. Annual (Not Semi-Annual) Audits

**Rejected:** Too infrequent given algorithm update pace

### 5. No IP Protection (Full Public Disclosure)

**Rejected:** Would deter builders, enable gaming and spam

## Implementation

### Fairness Scorecard API

**Public scorecard (`GET /v1/feeds/scorecards/{ranker_id}`):** Returns certification status, last/next audit dates, fairness scores (demographic parity, content equity), violation history, and dispute counts.

**Audit history (`GET /v1/feeds/audits/{ranker_id}`):** Lists historical audits with auditor info, result (PASSED/FAILED/CONDITIONAL), findings, and report URLs.

### Dispute Submission & Statistics

**Submit dispute (`POST /v1/feeds/disputes`):** Allows creators/users/auditors/advocates to file fairness complaints with evidence. Response includes dispute ID, status, acknowledgment SLA (2 days), and resolution SLA (10 days Tier 1).

**Dispute stats (`GET /v1/feeds/disputes/stats`):** Public aggregates showing counts by ranker/outcome and average resolution time.

### Audit Fund Transparency

**Audit fund status (`GET /v1/feeds/audit-fund/status`):** Publishes fund size, revenue percentage (1-3%), allocations per audit, pending audits, and last review date.

### Auditor Registry & Certification Flow

**Auditor list (`GET /v1/feeds/auditors`):** Public registry including accreditation, active/completed audits, enforcing independence rules (max 3-year tenure, 1-year cooling-off, no financial ties).

**Certification workflow:** Ranker owners submit via `/v1/feeds/certification`, auditors get NDA-bound access to ranker logic, audit results update scorecards, statuses (PENDING, CERTIFIED, SUSPENDED, REVOKED) enforced based on findings.

### Violation Handling & Reporting

- Violations tracked via scorecards; progressive penalties (warning, suspension, revocation) enforced per Section 9.4.
- Transparency reports (`GET /v1/feeds/transparency-reports`) published quarterly with dispute volume, outcomes, certification changes, and fund usage.

### Implementation Status

- ✅ Scorecard, audit history, dispute submission/stats, audit fund, and auditor registry endpoints defined in `openapi/feeds/v1/openapi.yaml`.
- ✅ Schemas stored under `schemas/audits/fairness-audit.json`.
- ✅ Three-tier dispute SLAs documented in `SPECS_REQUIREMENTS.md` §6.4.
- ✅ Certification statuses enumerated (CERTIFIED, SUSPENDED, REVOKED, PENDING) with fairness metrics.

### Certification & Enforcement Process

1. Ranker submits for certification; RA governance assigns independent auditor.
2. Auditor reviews signals, datasets, experiments; report published via audit history endpoint.
3. Scorecards updated with results; dispute API enables remediation requests.
4. Repeat every six months; emergency audits triggered via governance vote.

### Audit Fund Operations

- Governance board allocates 1-3% platform revenue; allocations and spending published via audit-fund endpoint.
- Supports emergency audits, ombudsperson investigations, and dispute mediation costs.

## Related Decisions

## Related Decisions

- ADR-001: WebAuthn as Primary Authentication
- ADR-002: Cursor-Based Pagination
- ADR-003: RFC 7807 Problem Details
- ADR-005: Double-Entry Ledger Accounting

## References

- SPECS_REQUIREMENTS.md Section 5.5 (Feed Generator & Ranking API)
- SPECS_REQUIREMENTS.md Section 6.4 (Fairness Audit Framework)
- SPECS_REQUIREMENTS.md Section 9.4 (Dispute Resolution & Reporting)
- IAB Content Taxonomy v3.0
- TAG IVT Guidelines
- ACM Code of Ethics and Professional Conduct

## Decision Date

November 7, 2025

## Approved By

RegistryAccord Technical Steering Committee

## Implementation Target

v2.0.0 (Q1 2026)

# Payments NFRs (Design-Only, Phase 1)

Scope
- Applies to design artifacts and gateway stubs; no production endpoints in Phase 1.

Latency targets
- Synchronous calls p95 ≤ 300ms for donate/subscribe/unlock stubs under nominal load.

Availability targets
- 99.9% monthly for read paths; write stubs follow gateway uptime.

Reconciliation
- Daily batch reconciliation; deterministic rounding rules documented and testable.

Rounding
- Bankers rounding to 2 decimals for fiat; credits ledger retains higher precision internally.

Idempotency
- Required for all mutating calls with replay-safe semantics and 24h window.

Observability
- Correlation IDs, structured logs, and specific error codes for payment flows.

Compliance
- PCI boundaries documented; KYC triggers and jurisdiction gating declared in design docs.

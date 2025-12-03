# ADR-005: Double-Entry Ledger Accounting for Payments

## Status

Accepted

## Summary

The Payments Service maintains all financial activity using a double-entry ledger. Every transaction posts balanced debit and credit entries across creator, platform, escrow, payout, or liability accounts so balances remain mathematically sound, disputes have full history, and programmable revenue splits are auditable.

This approach provides the rigor required for revenue sharing, payout holds, refunds, and compliance reporting across the decentralized ecosystem.

## Context

The Payments & Payouts service requires a robust accounting system to maintain financial integrity, ensure auditability, and support dispute resolution. Traditional single-entry systems are insufficient for tracking the complex flow of funds in a platform that handles revenue splits, refunds, and payouts.

Key requirements include:
- Immutable audit trail of all financial transactions
- Real-time balance verification
- Support for complex revenue split scenarios
- Compliance with financial regulations
- Dispute resolution with clear transaction history

## Decision

We will implement a double-entry ledger accounting system where every financial transaction is recorded as two entries: a debit and a credit. This approach ensures that the sum of all debits equals the sum of all credits, providing mathematical proof of transaction integrity.

### Ledger Structure

Each ledger entry will contain:
- Unique entry ID
- Entry type (PAYMENT_RECEIVED, PAYOUT_SENT, FEE_COLLECTED, REFUND_ISSUED, SPLIT_DISTRIBUTED)
- Debit account identifier
- Credit account identifier
- Amount and currency
- Reference to the source transaction
- Description
- Timestamp

### Account Types

1. **Platform Escrow Account**: Holds funds during transaction processing
2. **Creator Revenue Accounts**: Individual accounts for each content creator
3. **Platform Fee Accounts**: Collects platform fees and commissions
4. **Payout Destination Accounts**: External bank accounts or wallets
5. **Dispute Reserve Accounts**: Temporarily holds disputed funds
6. **Refund Liability Accounts**: Tracks refund obligations

### Transaction Examples

1. **Payment Processing**:
   - Debit: Customer's payment method
   - Credit: Platform escrow account

2. **Revenue Split**:
   - Debit: Platform escrow account
   - Credit: Creator revenue account
   - Debit: Creator revenue account
   - Credit: Platform fee account

3. **Payout Processing**:
   - Debit: Creator revenue account
   - Credit: Payout destination account

4. **Refund Issuance**:
   - Debit: Platform escrow account or creator revenue account
   - Credit: Customer's payment method

## Consequences

### Positive

- **Financial Integrity**: Mathematical proof of transaction accuracy
- **Auditability**: Complete, immutable record of all financial movements
- **Dispute Resolution**: Clear transaction history for dispute investigation
- **Regulatory Compliance**: Meets accounting standards for financial services
- **Real-time Balances**: Instant verification of account balances
- **Fraud Detection**: Anomaly detection through ledger analysis

### Negative

- **Increased Storage**: Double the entries compared to single-entry systems
- **Complexity**: More complex than simple balance tracking
- **Performance**: Additional writes for each transaction

### Neutral

- **Implementation Effort**: Significant initial development investment
- **Operational Overhead**: Requires understanding of double-entry principles

## Implementation

### Ledger Schema & Endpoints

- `LedgerEntry` schema (in `openapi/payments/v1/openapi.yaml`) includes `transaction_id`, `account_id`, `amount` (integer cents), `currency`, `type` (DEBIT/CREDIT), and `balance_after` for audit trails.
- `/v1/ledgers` supports filtering by `account_id`, date range, and pagination to stream entries.
- `/v1/ledgers/balance` returns current balances for any account.

### Double-Entry Enforcement

- Payment flows (intents, captures, refunds, payouts) emit ledger transactions where debits equal credits.
- Split rules (`SplitRule` schema) describe programmable revenue allocations (%, min amounts) and drive ledger postings.
- Validation layer rejects any transaction where total debits ≠ credits.

### Precision & Currency Handling

- All monetary fields stored as integers in smallest currency unit (ISO 4217) to avoid floating-point drift.
- Currency code required on every entry; balances aggregated per currency.

### Disputes & Audits

- `/v1/disputes` references `transaction_id` so investigators can trace ledger entries.
- SQL queries and monitoring jobs verify each `transaction_id` nets to zero and flag anomalies.
- Audit logs exported via `/v1/ledgers/export` (NDJSON) for regulators.

### Implementation Status

- ✅ Ledger schemas/endpoints defined across Payments spec.
- ✅ Spectral rules ensure all money fields use integer cents.
- ✅ Example workflows (payments, payouts, refunds) include ledger snippets.
- ✅ Conformance tests assert debit/credit totals match for sample transactions.

## Validation

- All ledger entries sum to zero across the entire system
- Account balances match expected values after transaction processing
- Ledger queries support regulatory audit requirements
- Performance meets SLA requirements for transaction processing

## References

- [Double-Entry Bookkeeping](https://en.wikipedia.org/wiki/Double-entry_bookkeeping)
- RegistryAccord Payments & Payouts Service Requirements (Section 5.3)
- Financial Services Regulatory Requirements

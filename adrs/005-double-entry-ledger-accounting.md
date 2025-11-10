# ADR-005: Double-Entry Ledger Accounting for Payments

## Status

Accepted

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

## Implementation Plan

1. **Ledger Service**: Create dedicated ledger service with REST API
2. **Entry Creation**: Automatically generate debit/credit pairs for transactions
3. **Balance Calculation**: Implement efficient balance aggregation queries
4. **Audit Endpoints**: Provide ledger querying for compliance and dispute resolution
5. **Monitoring**: Add metrics for ledger integrity verification

## Validation

- All ledger entries sum to zero across the entire system
- Account balances match expected values after transaction processing
- Ledger queries support regulatory audit requirements
- Performance meets SLA requirements for transaction processing

## References

- [Double-Entry Bookkeeping](https://en.wikipedia.org/wiki/Double-entry_bookkeeping)
- RegistryAccord Payments & Payouts Service Requirements (Section 5.3)
- Financial Services Regulatory Requirements

# Analytics Service Requirements

## 1. Analytics & Telemetry API

  * **Endpoints:**
      * `/v1/events`: Event ingestion.
      * `/v1/schemas`: **Schema registry** for all content types and events.
      * `/v1/metrics`: Derived metrics.
      * `/v1/exports`: Data export jobs.
      * `/v1/analytics/privacy-budget/status`: A visibility endpoint for data analysts.
  * **Audience Privacy Features:**
      * **Purpose Limitation:** Must *enforce* purpose limitation tags on all event schemas (e.g., data tagged for "ranking" cannot be used for "profiling").
      * **Differential Privacy:** Must provide "privacy budget" APIs to enforce differential privacy guarantees on queries and define warning thresholds for budget consumption.
      * **No Shadow Profiles:** Must prohibit data collection before explicit consent.
  * **NFRs:**

## Version History

| Version | Date       | Change Type | Description        | Related ADR |
|---------|------------|-------------|--------------------|-------------|
| 1.0.0   | 2025-12-04 | Initial     | Base Specification | N/A         |

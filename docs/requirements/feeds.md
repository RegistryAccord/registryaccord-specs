# Feeds Service Requirements

### 5.5. Feed Generator & Ranking API

  * **Endpoints:**
      * `/v1/feeds/query`: Feed generation.
      * `/v1/feeds/signals`: Signal definitions.
      * `/v1/feeds/experiments`: A/B testing.
      * **`/v1/feeds/scorecards/{ranker_id}`**: Public fairness scorecard. The response must include fields such as `ranker_id`, `last_audit_date`, `next_audit_date`, `fairness_scores` (e.g., `demographic_parity`, `content_equity`), `certification_status` (`CERTIFIED`, `SUSPENDED`, `REVOKED`), `violations`, and `dispute_count`.
      * **`/v1/feeds/audits/{ranker_id}`**: Audit history and results.
      * **`/v1/feeds/disputes`**: Submit fairness disputes.
      * **`/v1/feeds/disputes/stats`**: Aggregated dispute statistics.
  * **Key Features:**
      * Pluggable signals (recency, engagement, etc.).
      * Deterministic baseline ranking.
      * **Custom ranker support** via a `Ranker` registry (plugin interface for 3rd-party builders).
  * **Algorithmic Fairness & Auditing:**
      * **Fairness Testing:** All rankers must undergo automated and manual fairness testing (quarterly) against bias in demographic groups, content types, and engagement proxies.
      * **Published Metrics:** Fairness metrics must be published alongside conformance scorecards.
      * **Certification:** Biased rankers must be updated and re-certified before use.
      * **Independent Audits:** All widely deployed rankers (especially those operated by app owners) must undergo **regular (semi-annual), independent, third-party fairness audits**. (See *Section 6.4*)
  * **Transparency & Trust Features:**
      * **Tiered Explainability:** Define explanation depth (high-level for users, detailed for auditors) to provide transparency without enabling gaming.
      * **Ranking Signal Obfuscation:** Define requirements to prevent reverse-engineering of ranking factors by spammers.
  * **NFRs:** Low latency (p95 targets); caching; A/B switchability.

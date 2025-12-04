# Revenue Service Requirements

### 5.6. Revenue Services (Ads) API

  * **Endpoints:**
      * `/v1/ads/lineitems`: Campaign line items.
      * `/v1/ads/segments`: Audience segments.
      * `/v1/ads/creatives`: Creative assets.
      * `/v1/ads/auction`: Real-time bidding.
      * `/v1/ads/reports`: Attribution reports.
      * `/v1/ads/budget`: Real-time budget burn APIs.
      * `/v1/ads/refunds`: For processing IVT-related refunds.
  * **Advertiser Trust Features:**
      * **Pre-Bid Classification API:** Must include endpoints for real-time content category verification (see *Section 8.1*).
      * **Viewability & Verification:** Must include hooks for **IAB/MRC viewability measurement** and **3rd-party verification** (e.g., IAS, DoubleVerify). Implementations should provide a path for **MRC accreditation**.
      * **IVT Standards:** Detection must meet **Trustworthy Accountability Group (TAG)** guidelines for both baseline and sophisticated IVT.
      * **Adjacency Controls:** Must support exclusion lists for specific content types or creators.
      * **Discrepancy Resolution:** Must define protocols for resolving differences between RA analytics and advertiser tracking.
  * **Data Model:** `Campaign`, `LineItem`, `Segment`, `Creative`, `AuctionRequest`, `AuctionResult`.
  * **NFRs:**
      * Real-time bidding latency targets (\<100ms p95).
      * **Differential Privacy for Auction Logs:** Auction logs must use differential privacy with a defined **epsilon budget** and aggregation thresholds (e.g., **k-anonymity \>= 1000**) to prevent competitive intelligence leakage.

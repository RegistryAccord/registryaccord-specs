# Security Threats (Outline)

Identity
- Threats: key compromise, replay of session nonces, DID document tampering.
- Mitigations: signed nonce exchange, short-lived JWTs with `aud`, key rotation runbook, append-only operation log.

CDV write path
- Threats: schema bypass, forged authorship, integrity loss.
- Mitigations: schema validation at edges, author DID verification, content-addressed URIs, checksums on media finalize.

Event bus
- Threats: unauthorized publish/subscribe, message tampering, replay.
- Mitigations: NATS credentials per service, TLS, dedup windows, durable consumers with idempotency.

Webhooks
- Threats: signature forgery, replay, endpoint discovery.
- Mitigations: HMAC signatures, timestamped headers, nonce/replay window, rotate secrets.

Payments design
- Threats: rounding exploitation, reconciliation mismatch, jurisdictional bypass.
- Mitigations: deterministic rounding rules, reconciliation cadence, regional gating checks.

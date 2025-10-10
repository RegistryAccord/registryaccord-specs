# Eventing Specification

Bus
- NATS JetStream with TLS and per-service credentials.

Streams
- RA_RECORDS: subjects `cdv.records.*`, retention=limits, duplicates window=2m.
- RA_MEDIA: subjects `cdv.media.*`.

Subjects
- cdv.records.post.created
- cdv.records.comment.created
- cdv.media.finalized

Envelope
- `{ type: string, version: string, occurredAt: string, correlationId: string, payload: object }`
- `payload` conforms to corresponding schema version.

Consumers
- GATEWAY_FANOUT: delivers to gateway for indexing and feed/search stubs.
- DURABLE_DEVTOOLS: durable mirror for tooling and replay in dev.

Delivery
- At-least-once; consumers must be idempotent with dedup keys on `correlationId`.

Security
- NKEYS/JWT auth for NATS; rotate credentials per runbook; per-env isolation.

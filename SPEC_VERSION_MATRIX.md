# Spec Version Matrix (Phase 1)

Purpose
- Declare target schema versions per client/service to ensure demo and conformance alignment.

Matrix (example)
- identity-go: DID/session → stable schemas (none required)
- cdv-go: profile 1.0.0, post 1.0.0, mediaAsset 1.0.0
- gateway-go: federation draft v0 samples referencing post 1.0.0
- sdk-ts: generated types for profile 1.0.0, post 1.0.0
- cli-ts: reads/writes compatible with 1.0.0

Notes
- Update this file with each schema release; clients lagging versions must provide fallbacks.

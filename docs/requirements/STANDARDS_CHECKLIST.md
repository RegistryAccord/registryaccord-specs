# API Standards Checklist for SDK Consumers

> **Context**: When generating SDKs from these specs, ensure the generator config respects:

## Global Standards (from `global-standards.md`)
- [ ] **Date/Time**: Handle `format: date-time` as native Date objects (ISO 8601).
- [ ] **IDs**: Handle `format: int64` as BigInt or String (to prevent overflow).
- [ ] **Errors**: Must implement RFC 7807 `ProblemDetails` parsing.
- [ ] **Auth**: Support both `Bearer` (JWT) and `ApiKey` schemes.
- [ ] **Versioning**: Inject `RA-API-Version` header in all requests.

## Validation
- [ ] Does the SDK `BaseClient` inject the version header?
- [ ] Are 4xx/5xx errors strictly typed?

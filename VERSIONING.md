# RegistryAccord Versioning Policy

## Two-Layer Versioning

RegistryAccord uses a hybrid approach (Stripe-inspired) for API stability and developer experience.

### Layer 1: API Specifications (Date-Based)

**Format**: `YYYY-MM-DD` (e.g., `2025-11-01`)

**How it works**:
- All API requests include `RA-API-Version: 2025-11-01` header
- Accounts are pinned to API version on first request
- Developers explicitly upgrade to new API versions (no automatic changes)

**Why date-based**:
- Clear staleness signals (`2023-06-15` is obviously 2+ years old)
- Explicit breaking changes (new date = deliberate protocol change)
- No surprise upgrades via dependency resolution
- Strong governance for open protocol

**Example**:
```typescript
const client = new RegistryAccord({
  apiKey: 'sk_test_...',
  apiVersion: '2025-11-01'  // Explicit version pin
})
```

### Layer 2: SDK Packages (Semantic Versioning)

**Format**: `MAJOR.MINOR.PATCH` (e.g., `1.2.3`)

**Versioning rules**:
- **MAJOR**: Breaking API changes (new API date version with breaking changes)
- **MINOR**: New features, backward-compatible additions
- **PATCH**: Bug fixes only, no API changes

**Why SemVer**:
- Package manager compatibility (npm, pip, go mod)
- Dependency constraints work as expected (`^1.2.0`, `~1.2.3`)
- Clear upgrade safety signals (1.2.3 → 1.2.4 safe, 1.2.3 → 2.0.0 risky)

**Example**:
```bash
npm install @registryaccord/sdk@^1.2.0
```

---

## API Version Lifecycle

### 1. Release (Day 0)
- New API version announced with changelog
- Migration guide published
- SDK updated with corresponding major version

### 2. Support Window (18 months)
- Full feature support and bug fixes
- Security patches applied
- Documentation and examples maintained

### 3. Deprecation Notice (6 months before EOL)
- Email notification to all API key owners
- Public announcement in changelog
- Deprecation headers added to responses:
  ```
  Deprecation: true
  Sunset: Sat, 01 Feb 2026 00:00:00 GMT
  Link: <https://docs.registryaccord.com/migration>; rel="deprecation"
  ```

### 4. End-of-Life
- API version enters maintenance mode
- Security patches only (no new features)
- Users strongly encouraged to upgrade

---

## Breaking vs. Non-Breaking Changes

### What Qualifies as Breaking:
- Removing endpoints or fields
- Changing field types or validation rules
- Changing authentication mechanisms
- Modifying error response structure
- Changing pagination format
- Changing default behavior

### What is NOT Breaking:
- Adding new optional fields
- Adding new endpoints
- Adding new error codes
- Improving performance
- Bug fixes that restore intended behavior
- Adding new status values to enums (if additive)

### Breaking Change Process:
1. **RFC Discussion** (14-day minimum review)
2. **TSC Approval** (Technical Steering Committee vote)
3. **Migration Guide** (detailed upgrade instructions)
4. **90-Day Deprecation** (minimum notice period)
5. **New API Version** (date-based, e.g., 2026-05-15)
6. **SDK Major Bump** (e.g., 1.x.x → 2.0.0)

---

## SDK Versioning Strategy

### Major Version Bumps
Triggered by:
- Breaking API changes (new API date version with breaking changes)
- Removing deprecated SDK methods
- Changing SDK architecture (rare)

Example: SDK v1.x.x → v2.0.0 when API version changes from 2025-11-01 → 2026-05-15

### Minor Version Bumps
Triggered by:
- New API features (backward-compatible)
- New SDK convenience methods
- Performance improvements
- Bug fixes that restore intended behavior

Example: SDK v1.2.0 → v1.3.0 when new optional API fields added

### Patch Version Bumps
Triggered by:
- Bug fixes (no API/SDK changes)
- Documentation updates
- Internal refactoring

Example: SDK v1.2.3 → v1.2.4 for bug fixes

---

## Deprecation Headers

All deprecated endpoints return RFC 8594 compliant headers:

```http
Deprecation: true
Sunset: Sat, 01 Feb 2026 00:00:00 GMT
Link: <https://docs.registryaccord.com/api/migration-guide-v2>; rel="deprecation"
```

---

## Support Policy

| API Version Status | Support Level | Security Patches | New Features | SDK Support |
|---|---|---|---|---|
| **Current** | ✅ Full | ✅ Yes | ✅ Yes | Latest major version |
| **Current - 1** | ✅ Full | ✅ Yes | ❌ No | Previous major version |
| **Deprecated** | ⚠️ Maintenance | ✅ Yes | ❌ No | Maintenance mode |
| **End-of-Life** | ❌ None | ❌ No | ❌ No | Not supported |

---

## Version Mapping

See [versions.md](./versions.md) for complete mapping of API date versions to SDK semantic versions.

---

## Contact

Questions about versioning? 
- Open an issue on GitHub
- Email: info@registryaccord.com

Last updated: 2025-11-17

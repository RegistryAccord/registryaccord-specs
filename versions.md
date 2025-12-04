# RegistryAccord Version Mapping

This document maps API date versions to SDK semantic versions, bridging RegistryAccord's two-layer versioning strategy.

---

## Why Two Versioning Schemes?

**API Specs: Date-Based** (e.g., `2025-11-01`)
- Governance and stability for the open protocol
- Clear staleness signals
- Explicit breaking changes
- Account pinning (no surprise upgrades)

**SDK Packages: Semantic Versioning** (e.g., `1.2.3`)
- Package manager compatibility (npm, pip, go mod)
- Dependency constraints work as expected
- Clear upgrade safety signals

See [VERSIONING.md](./VERSIONING.md) for detailed policy.

---

## Current API Versions

| API Version | Release Date | Status | SDK Compatibility | Support Until | Breaking Changes |
|---|---|---|---|---|---|
| `2025-11-01` | Nov 1, 2025 | ✅ **Current** | SDK v1.x | May 1, 2027 | Initial release (stable) |

---

## SDK Version History

### TypeScript SDK (`@registryaccord/sdk`)

| SDK Version | API Versions | Release Date | Notes | NPM Link |
|---|---|---|---|---|
| `1.0.0` - `1.9.x` | `2025-11-01` | Nov 1, 2025 | Initial SDK release | [@registryaccord/sdk](https://npmjs.com/package/@registryaccord/sdk) |

**Installation**:
```bash
npm install @registryaccord/sdk@^1.0.0
```

### Python SDK (`registryaccord`)

| SDK Version | API Versions | Release Date | Notes | PyPI Link |
|---|---|---|---|---|
| `1.0.0` - `1.9.x` | `2025-11-01` | Nov 1, 2025 | Initial SDK release | [registryaccord](https://pypi.org/project/registryaccord) |

**Installation**:
```bash
pip install registryaccord>=1.0.0,<2.0.0
```

### Go SDK (`github.com/registryaccord/sdk-go`)

| SDK Version | API Versions | Release Date | Notes | Go Package |
|---|---|---|---|---|
| `v1.0.0` - `v1.9.x` | `2025-11-01` | Nov 1, 2025 | Initial SDK release | [github.com/registryaccord/sdk-go](https://pkg.go.dev/github.com/registryaccord/sdk-go) |

**Installation**:
```bash
go get github.com/registryaccord/sdk-go@v1
```

---

## Upgrade Paths

### Future: API `2025-11-01` → `2026-05-15` (When Released)

Example scenario (when a new API version is released):

**Breaking Changes**: 
- Removed `/v1/legacy` endpoint
- Changed pagination format from offset to cursor

**Migration**:
1. Read Migration Guide: 2025-11-01 → 2026-05-15 (Future)
2. Update SDK: `npm install @registryaccord/sdk@^2.0.0` 
3. Update API version in client code:
   ```typescript
   const client = new RegistryAccord({
     apiKey: 'sk_test_...',
     apiVersion: '2026-05-15'  // Upgrade from 2025-11-01
   })
   ```
4. Fix breaking changes per migration guide
5. Test thoroughly before deploying

---

## FAQ

**Q: What version should I use?**
A: Use the latest SDK version for the current API version. Check the "Current API Versions" table above.

**Q: Can I use an old SDK with a new API version?**
A: No. Each SDK major version is tied to a specific API date version. Upgrade the SDK when you upgrade the API version.

**Q: Can I use a new SDK with an old API version?**
A: Generally no, since SDKs are built for specific API versions. To use an old API version, install the corresponding SDK version.

**Q: When should I upgrade my API version?**
A: When you need new features from a newer API version, or when your current version approaches end-of-life (6-month notice period). We'll email you 6 months before end-of-life.

**Q: What happens if I don't upgrade before end-of-life?**
A: Your integration will continue to work in maintenance mode, but you'll stop receiving security patches and support. We strongly recommend staying within the 18-month support window.

**Q: Can I run multiple API versions simultaneously?**
A: Not in a single client instance. Create separate client instances for different API versions if needed:
```typescript
const clientV1 = new RegistryAccord({
  apiVersion: '2025-11-01'
})

const clientV2 = new RegistryAccord({
  apiVersion: '2026-05-15'
})
```

**Q: How do I know if an SDK upgrade will break my code?**
A: Check the SDK version number:
- `1.2.3` → `1.2.4`: No breaks (patch), safe to upgrade
- `1.2.3` → `1.3.0`: Likely safe (minor), but read changelog
- `1.2.3` → `2.0.0`: Breaking changes (major), must read migration guide

---

## Support Windows

Each API version has an 18-month support window:

```
Release           6 Months        12 Months       18 Months (EOL)
|================|================|================|
Day 0            Day 180         Day 360         Day 540

↑ Full Support   ↑ EOL Notice Sent
```

---

## Releases & Announcements

New API versions and SDK releases are announced in:
- [GitHub Releases](https://github.com/RegistryAccord/registryaccord-specs/releases)
- [Changelog](./CHANGELOG.md)
- Email to registered API key owners
- [RegistryAccord Blog](https://registryaccord.com/blog)

Subscribe to release notifications on GitHub.

---

## Contact

- **General Questions**: info@registryaccord.com
- **SDK Issues**: [GitHub Issues](https://github.com/RegistryAccord/registryaccord-specs/issues)
- **Security Issues**: Use the private security contact (see SECURITY.md)

Last updated: 2025-11-17

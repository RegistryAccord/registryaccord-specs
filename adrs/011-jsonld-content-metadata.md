# ADR-011: JSON-LD for Content Metadata (Schema.org)

- **Status:** Accepted
- **Author:** RegistryAccord Team
- **Created:** 2025-11-18
- **Updated:** 2025-11-18

## Summary
RegistryAccord standardizes content metadata using JSON-LD with Schema.org vocabulary. Every content record embeds a JSON-LD document describing its semantic type, attributes, relationships, and rights information. This decision delivers interoperability with existing web tooling, unlocks SEO/knowledge-graph benefits, and eliminates the need to maintain proprietary metadata schemas.

## Context
The protocol must describe diverse content types (articles, videos, audio, posts, events, products) while supporting semantic queries, rights enforcement, and federation with third-party platforms. Proprietary JSON schemas or legacy RSS/Atom feeds fail to capture rich relationships and lack search-engine support.

## Decision
Use JSON-LD as the serialization format and Schema.org as the base vocabulary for all content metadata:
- `metadata` field on Content Registry objects stores JSON-LD.
- `@context` defaults to `https://schema.org`; `@type` follows Schema.org types (Article, VideoObject, SocialMediaPosting, etc.).
- Analytics service exposes `/v1/schemas` registry for validating metadata against JSON Schema representations of Schema.org types.
- SDKs provide helpers to validate and embed JSON-LD payloads.

## Rationale
- **Interoperability:** Schema.org is supported by Google, Microsoft, and major CMSs; JSON-LD works natively with JavaScript/JSON tooling.
- **Semantic richness:** Linked data expresses relationships (isPartOf, comment, remixOf) and rights metadata (license, attribution).
- **SEO & discovery:** Rich snippets, knowledge graph inclusion, and voice-assistant compatibility rely on Schema.org.
- **Extensibility:** Schema.org covers 800+ types and can be extended with custom terms when necessary.

## Consequences
**Positive:** Consistent metadata across content types, instant compatibility with search engines and aggregators, reduced need for bespoke schemas, easier validation via shared registry.

**Negative:** JSON-LD is more verbose, requires developer education, and some niche content may need custom extensions. Larger metadata payloads may marginally increase storage/bandwidth (mitigated by compression).

## Alternatives Considered
1. **Proprietary JSON schema:** Simple but lacks semantics/interoperability and duplicates Schema.org effort.
2. **RSS/Atom XML:** Legacy format limited to blogs, poor developer experience for modern content.
3. **ActivityStreams 2.0:** Useful for social interactions but lacks Schema.org breadth and SEO benefits; would introduce a second vocabulary.
4. **Hybrid Schema.org + ActivityStreams:** Adds complexity without clear benefits for v1.

## Implementation
- Content API requires `metadata` JSON-LD payloads and validates via schema registry endpoints.
- Examples in `schemas/jsonld/` showcase Article, VideoObject, and SocialMediaPosting templates.
- SDKs include helper builders and validators for JSON-LD objects.
- Documentation references how to embed metadata into HTML (`<script type="application/ld+json">`).

## References
- `SPECS_REQUIREMENTS.md` §2.2 and §5.2
- Schema.org, JSON-LD specifications
- `schemas/jsonld/` examples in this repository

## Related ADRs
- ADR-004 (Content integrity hashing) – metadata hashed alongside content.
- ADR-009 (Service separation) – Content service owns metadata schema enforcement.

_Last updated: 2025-11-18_

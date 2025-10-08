# Migration for atproto Developers

Conventions
- Lexicon v1, NSIDs, and record/query/procedure shapes follow common atproto norms for easy porting.

Mapping
- Identity: com.registryaccord.identity (record + create).
- Posts: com.registryaccord.feed.post (record + list).

Differences
- Discovery/publication are governed by RegistryAccord; Lexicon is used as a schema DSL and validator, not as a network binding.

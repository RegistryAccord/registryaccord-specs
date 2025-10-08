# Schema Standards

Naming
- NSIDs: com.registryaccord.*; file name matches id; property names are lowerCamelCase.

Types and constraints
- Use string with format (datetime, uri) and integer bounds where applicable; cap text fields via maxLength with rationale.

Required fields
- Keep minimal; prefer optional with defaults where reasonable; promote to required only when interop demands it.

Refs and reuse
- Factor shared shapes with defs and ref to avoid drift; no dead or unused defs.

Examples
- Provide minimal and full examples; ensure validation passes; link examples from schemas/INDEX.md.

# Style Guide

Naming
- JSON properties: camelCase; enums: SCREAMING_SNAKE_CASE.
- Namespaces: lowercase dot-delimited; schema names: kebab-case.

Descriptions
- One-line summary + constraints; avoid ambiguity; specify invariants and regex where relevant.

IDs and references
- Use clear field names: did, uri, assetId; avoid synonyms.

Errors
- Prefix codes by domain; keep messages user-readable and deterministic.

Docs
- Keep examples small and focused; include negative cases with specific failure reasons.

Diagrams
- Use Mermaid for sequence and state diagrams; store alongside related docs.

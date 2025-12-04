# Generic AI Rules

> **Apply these rules to every interaction.**

## 1. Context First
- Always check `AGENTS.md` to understand the repo map.
- Before editing any file, read its corresponding Requirement in `docs/requirements/{service}.md` or `docs/requirements/global-standards.md`.

## 2. Validation
- **OpenAPI**: Must be valid YAML (OpenAPI 3.1).
- **Linting**: If `scripts/validate.sh` exists, run it after changes.
- **Links**: Ensure no broken `$ref` links.

## 3. Style
- Follow `.ai/knowledge/style-guide.md` strictly.
- Use Kebab-case for filenames and URL paths.
- Use PascalCase for Schemas.

## 4. Safety
- Never delete `openapi/common/` files without explicit instruction.
- Do not commit secret keys or credentials.

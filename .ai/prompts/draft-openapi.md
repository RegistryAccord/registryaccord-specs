# Draft OpenAPI Spec Prompt

**Context**: Create or update an OpenAPI 3.1 definition.

**Instructions**:
1. Read `docs/requirements/{service}.md` and `docs/requirements/global-standards.md`.
2. Follow the folder structure: `openapi/{service}/{version}/openapi.yaml`.
3. Use standard components from `openapi/common/`.
4. Ensure every endpoint has:
   - `operationId` (verbObject style, e.g., `getUser`).
   - `summary` and `description`.
   - 4xx and 5xx error responses (referencing `ProblemDetails`).
5. Validate YAML syntax before saving.

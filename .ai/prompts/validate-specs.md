# Spec Validation Prompt

**Context**: Validate OpenAPI files for correctness.

**Instructions**:
1. **Linting**: Run `npx spectral lint {file_path}`.
2. **Consistency**: Check if the new spec uses shared components from `openapi/common/`.
3. **Links**: Verify that all `$ref` paths resolve correctly.
4. **Mocking**: (Optional) Verify if a mock server can generate valid examples from the schema.

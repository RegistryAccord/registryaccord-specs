# Spec Review Prompt

**Context**: Review a pull request containing OpenAPI changes or ADRs.

**Checklist**:
1. **Compliance**: Does it match `docs/requirements/global-standards.md` and the specific service requirement file?
2. **Style**: Does it follow `.ai/knowledge/style-guide.md`? (Naming, Types, formats)
3. **Structure**:
   - Are `summary` and `description` fields populated?
   - Are `operationId`s unique and correctly formatted?
   - Are error responses (4xx, 5xx) defined?
4. **Breaking Changes**: Does this change break existing clients? (Check for removal of fields/endpoints).
5. **Scenario Check**: Does the spec support flows defined in `docs/scenarios/`?

# AGENTS.md
> **AI Entry Point for Specs**

## 🗺️ Context
- **Repo Purpose**: Source of truth for RegistryAccord API Definitions.
- **Requirements Index**: `docs/requirements/INDEX.md`
- **Global Standards**: `docs/requirements/global-standards.md`
- **Service Specs**: `docs/requirements/{service}.md`
- **Scenarios**: `docs/scenarios/`
- **Format**: OpenAPI 3.1 (YAML).

## 🤖 Standard Workflows
1. **Draft Spec**: Use `.ai/prompts/draft-openapi.md`.
2. **Write ADR**: Use `.ai/prompts/draft-adr.md`.
3. **Review**: Use `.ai/prompts/spec-review.md`.
4. **Validate**: Use `.ai/prompts/validate-specs.md`.

## 🚨 Critical Rules
- **No JSON**: All specs must be YAML.
- **Linting**: All specs must pass `spectral` validation.
- **Versioning**: Follow `openapi/{service}/v1/` structure.
- **Ids**: All schemas must have explicit `title` and `description`.

## 🌍 Generic AI Support
If you are not using Cursor, please read:
- **Rules**: `.ai/rules/generic-rules.md`
- **Lessons**: `.ai/knowledge/lessons-learned.md`

## 🚀 Release Workflow
- **Prepare Release**: Use `.ai/prompts/release-prep.md`

## 🔗 Downstream Dependencies
- **SDK Consumers**: Refer to `docs/requirements/STANDARDS_CHECKLIST.md` for implementation rules.

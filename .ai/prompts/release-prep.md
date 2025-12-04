# Release Preparation Prompt

**Context**: Prepare the specs for a new version release.

**Instructions**:
1. **Versioning**: Update the `info.version` in `openapi/{service}/v1/openapi.yaml`.
2. **Changelog**: summarizing changes in `CHANGELOG.md`.
   - Group by Service (Identity, Content, etc.).
   - Label as Added, Changed, Deprecated, or Removed.
3. **Validation**: Run full validation suite.
4. **Freeze**: Ensure no "WIP" comments remain in the spec.

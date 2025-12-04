# Lessons Learned & Feedback

> **AI Instructions**: Read this before starting complex tasks. If a user corrects you, append the correction here.

- [ ] **Always Log Changes**: When modifying a spec, you MUST update the requirement file's history table. Git history is not enough for context.

## Common Mistakes to Avoid
- [ ] Don't use JSON for OpenAPI specs; use YAML.
- [ ] Don't forget `operationId` in new endpoints.
- [ ] Don't remove `x-internal-id` extensions from legacy schemas.

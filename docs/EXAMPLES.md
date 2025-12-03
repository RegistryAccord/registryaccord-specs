# Endpoint Example Workflow

Every OpenAPI endpoint must have at least one documented request/response example. The repository enforces this requirement automatically.

## Regenerating Examples

1. Ensure your OpenAPI changes are committed locally (or staged) so the generator can diff outputs.
2. Run the generator:
   ```bash
   python3 scripts/generate_endpoint_examples.py
   ```
   This refreshes `examples/generated/<service>/...` and rewrites `examples/examples-map.json`.
3. Review diffs for the generated files and adjust any hand-authored examples if needed.

## Validating Coverage

CI (and `npm run validate`) call the metadata checker:
```bash
python3 scripts/check_examples.py
```
This script ensures:
- Every endpoint listed in `openapi/*/v1/openapi.yaml` has a corresponding entry in `examples/examples-map.json`.
- Each map entry points to an existing YAML/JSON file.
- No stale entries exist when endpoints are removed.

Commit the regenerated examples and the metadata map alongside the spec changes so the validation step passes locally and in CI.

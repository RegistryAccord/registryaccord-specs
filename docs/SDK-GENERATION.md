# SDK Generation

RegistryAccord maintains official SDKs in separate repositories, auto-generated from the OpenAPI specs in this repository.

## Official SDKs

| Language   | Repository             | Package                | Installation                          |
|------------|------------------------|------------------------|----------------------------------------|
| TypeScript | `registryaccord-sdk-ts` | `@registryaccord/sdk`  | `npm install @registryaccord/sdk`      |
| Python     | `registryaccord-sdk-py` | `registryaccord`       | `pip install registryaccord`           |
| Go         | `registryaccord-sdk-go` | `github.com/registryaccord/sdk-go` | `go get github.com/registryaccord/sdk-go` |

## Versioning

SDKs use Semantic Versioning (MAJOR.MINOR.PATCH):

- SDK v1.x → API `2025-11-01`
- SDK v2.x → Next API version (when released)

See [versions.md](../versions.md) for the complete mapping between API dates and SDK releases.

## Generator

SDKs are generated using **OpenAPI Generator 7.0+** from OpenAPI 3.1 specs located under `openapi/*/v1/`.

Generator compatibility:

- OpenAPI Generator (preferred)
- Speakeasy
- Fern

Each SDK repository contains:

- Generation scripts
- Custom templates for RegistryAccord-specific features
- Tests and runnable examples

## Contributing

SDK generation is automated in each SDK repository. To contribute:

1. Open an issue in the language-specific SDK repository.
2. Submit specification changes as a PR to this `registryaccord-specs` repository.
3. Submit SDK implementation changes as a PR to the corresponding SDK repository.

_Last updated: 2025-11-18_

# API Style Guide

## Naming Conventions
- **Paths**: Kebab-case, plural nouns (e.g., `/users`, `/billing-records`).
- **Schemas**: PascalCase (e.g., `UserProfile`, `ErrorResponse`).
- **Properties**: camelCase (e.g., `createdAt`, `isActive`).

## Data Types
- Use `string` + `format: date-time` for timestamps (ISO 8601).
- Use `integer` + `format: int64` for IDs.

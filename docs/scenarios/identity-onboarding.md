# Scenario: User Onboarding

## Flow: Register and Login
1. **Given** a new user with email "test@example.com"
2. **When** they POST to `/identity/v1/registrations`
3. **Then** they receive a `201 Created` with a `userId`
4. **And** they can immediately POST to `/identity/v1/login` to get a JWT.

## AI Validation Check
- Does `openapi/identity/v1/openapi.yaml` have these endpoints?
- Do the request/response schemas match?

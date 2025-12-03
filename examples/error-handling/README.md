# Error Handling Examples

This directory contains RFC 7807 Problem Details examples for all common error scenarios in the RegistryAccord API.

## Purpose

- Demonstrate proper error response format
- Show correlation ID usage
- Illustrate retry hints
- Provide developer reference

## Files

- `400-bad-request.json` - Validation errors
- `401-unauthorized.json` - Authentication failures
- `403-forbidden.json` - Authorization/permission errors
- `404-not-found.json` - Resource not found
- `429-rate-limit.json` - Rate limiting with Retry-After
- `500-internal-error.json` - Server errors
- `503-service-unavailable.json` - Temporary unavailability

## Standards

All errors follow RFC 7807 with:
- `type` (URI identifier)
- `title` (short description)
- `status` (HTTP status code)
- `detail` (human-readable explanation)
- `instance` (API endpoint)
- `correlation_id` (UUID for tracing)

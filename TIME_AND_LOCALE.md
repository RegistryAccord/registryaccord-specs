# Time and Locale

Timestamps
- RFC 3339 in UTC (e.g., 2025-10-10T12:34:56Z) for all payloads and logs.

Client display
- Local rendering is a client concern; protocol remains UTC to ensure deterministic ordering.

Locale and language
- BCP 47 language tags where needed for content and UI hints.

Clock considerations
- Services should tolerate minor clock skew; avoid rejecting requests solely due to small drifts.

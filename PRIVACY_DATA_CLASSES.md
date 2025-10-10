# Privacy Data Classes

Classes
- Public profile data: displayName, avatar, bio, links; default public.
- Social graph references: follows, reposts, likes; retention per product policy.
- Content records: posts and comments; creator-owned with sharing controls.
- Media assets: referenced by content; integrity protected by checksums.
- Session and auth metadata: minimal retention for security auditing.

Selective disclosure
- Identity and CDV must support creator-controlled sharing.
- Discovery and analytics use privacy-preserving aggregation where feasible.

Retention
- Default retention documented per class; deletion and export paths defined in service repos.

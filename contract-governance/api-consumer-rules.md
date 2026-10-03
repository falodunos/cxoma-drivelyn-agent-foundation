# API consumer rules

The API repository owns the authoritative API contract. Mobile consumes that contract through a repository-local copy suitable for independent clones. Mobile must not depend on API implementation; API must not depend on Android internals.

Cross-repository context is limited to endpoint contracts, DTO/schema, enums, error codes, nullability, telemetry limits and retry/idempotency semantics. Review contract changes with affected consumers and record their local contract version/evidence. No contract comparison automation is introduced here.

Keep database/JPA internals in the API repository. Keep Room, Compose, lifecycle, permissions, foreground-service and device behavior in mobile. Shared policy owns principles, not scoring implementation, provider adapters or platform architecture.

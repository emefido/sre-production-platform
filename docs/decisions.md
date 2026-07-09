# Architecture Decisions

## ADR-001

### Decision

Use Docker Compose instead of individual Docker commands.

### Reason

The platform will consist of multiple services.

Docker Compose allows all services to be managed from a single configuration.

## ADR-002

### Decision

Build the application before adding monitoring.

### Reason

Monitoring systems require a running application to observe.

Applications produce metrics, logs, and traces that observability tools collect.

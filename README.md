# Production-Grade SRE Observability Platform

> A production-style Site Reliability Engineering portfolio demonstrating monitoring, observability, reliability engineering, distributed tracing, synthetic monitoring, and CI/CD.

![Platform](docs/architecture.png)

---

## Executive Summary

This repository demonstrates how to design, build, monitor, operate, and troubleshoot a production-style application platform from scratch.

The focus is operational excellence rather than infrastructure provisioning. Every component was added incrementally and validated to build a complete observability platform suitable for demonstrating Senior Site Reliability Engineering skills.

## Architecture

```text
                    GitHub
                       │
             GitHub Actions CI
                       │
                       ▼
                Docker Compose
                       │
 ┌─────────────────────┼──────────────────────┐
 │                     │                      │
 ▼                     ▼                      ▼
FastAPI            PostgreSQL              Redis
 │
 ├──────────── Metrics ─────────────┐
 │                                  │
 ▼                                  ▼
Prometheus                   Blackbox Exporter
 │
 ├──────── Alerts ───────────────► Alertmanager
 │
 ▼
Grafana
 ▲
 │
 ├──────────────┬───────────────┐
 │              │               │
 ▼              ▼               ▼
Loki          Tempo        Prometheus
 ▲              ▲
 │              │
Promtail   OpenTelemetry
```

## Technology Stack

| Area | Technology |
|------|------------|
| API | FastAPI |
| Database | PostgreSQL |
| Cache | Redis |
| Metrics | Prometheus |
| Dashboards | Grafana |
| Alerting | Alertmanager |
| Logging | Loki + Promtail |
| Tracing | OpenTelemetry + Tempo |
| Synthetic Monitoring | Blackbox Exporter |
| Container Monitoring | cAdvisor |
| Host Monitoring | Node Exporter |
| Database Monitoring | PostgreSQL Exporter |
| CI | GitHub Actions |
| Runtime | Docker Compose |

## Features

- FastAPI application
- PostgreSQL and Redis
- Prometheus metrics
- Recording Rules and Burn Rate alerts
- Grafana dashboards
- Alertmanager integration
- Loki centralized logging
- OpenTelemetry + Tempo tracing
- Blackbox synthetic monitoring
- GitHub Actions CI

## Dashboards

### Database
- PostgreSQL Availability
- Active Connections
- Database Size
- Transactions/sec
- Locks
- Connection Utilization

### Reliability
- Synthetic Availability
- Probe Latency
- HTTP Status Code
- Error Budget Burn Rate
- HTTP 5xx Error Rate

### Logs
- Loki Explore

### Traces
- Tempo Explore

## Repository Structure

```text
.
├── apps/
├── platform/
├── docs/
├── scripts/
├── automation/
├── docker-compose.yml
└── README.md
```

## CI Pipeline

- Checkout repository
- Install dependencies
- Validate Docker Compose
- Validate Prometheus configuration
- Build Docker image

## Quick Start

```bash
git clone https://github.com/emefido/sre-production-platform.git
cd sre-production-platform
cp .env.example .env
docker compose up -d
```

## Skills Demonstrated

- Site Reliability Engineering
- Observability
- Monitoring
- Alerting
- Distributed Tracing
- Synthetic Monitoring
- CI/CD
- Docker

## Future Improvements

- Kubernetes deployment
- Horizontal scaling
- Production TLS

## License

Educational and portfolio purposes.

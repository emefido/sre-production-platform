# SRE Production Platform

A production-style Site Reliability Engineering and Platform Engineering project built from scratch.

## Purpose

This repository demonstrates how to design, build, monitor, operate, and improve a production-like platform using modern SRE practices.

## Planned Components

- Docker Compose
- Nginx
- FastAPI
- PostgreSQL
- Redis
- Prometheus
- Grafana
- Alertmanager
- Loki
- OpenTelemetry
- GitHub Actions
- Health checks
- Backups
- Incident simulation
- Auto-remediation
- Runbooks and architecture documentation

## Architecture Philosophy

This platform starts with the application before adding observability tools such as Prometheus, Grafana, Loki, and Alertmanager.

The reason is simple: monitoring systems exist to observe real workloads. Prometheus needs metrics to scrape, Grafana needs data to visualize, Loki needs logs to search, and Alertmanager needs failure signals to act on.

So the platform is built in this order:

```text
Application
  ↓
Supporting services
  ↓
Observability
  ↓
Alerting
  ↓
Automation
  ↓
Incident response
## Current Status

Milestone 1: Project skeleton and repository standards.

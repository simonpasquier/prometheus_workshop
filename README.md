This repository contains the documentation and materials for running a
Prometheus and AlertManager workshop.

# Pre-requisites

The workshop assumes that Docker is installed on your machine.

You can pull the following images in advance:

* prom/prometheus:v2.0.0
* prom/node-exporter:v0.15.2
* prom/blackbox-exporter:v0.11.0
* prom/alertmanager:v0.12.0
* grafana/grafana:4.6.3
* simonpasquier/instrumented_app:latest

If Docker isn't an option, you can download the binaries from the
[Prometheus](https://prometheus.io/download/) and
[Grafana](https://grafana.com/grafana/download).

# [Getting started with Prometheus](GettingStarted.md)

# [PromQL, the query language](PromQL.md)

# [Alerting](Alerting.md)

# [Building dashboards with Grafana](Grafana.md)

# [Service discovery](ServiceDiscovery.md)

# [Instrumenting applications](Instrumentation.md)

# [High-availability](HighAvailability.md)

# [Advanced topics](AdvancedTopics.md)


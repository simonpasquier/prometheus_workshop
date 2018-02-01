This repository contains the documentation and materials for running a
Prometheus and AlertManager workshop.

# Pre-requisites

1) Clone this repository.

2) Download the following binaries:

* prometheus
* node-exporter
* blackbox-exporter
* alertmanager

Since these applications are written in Golang, the binaries are available for
all major platforms from the [Prometheus](https://prometheus.io/download/).

You also need to install [Grafana](https://grafana.com/grafana/download). The
procedure depends on your operating system but again all major platforms are
supported.

3) Python3 and virtualenv are required for the "Instrumenting applications" part.

Once downloaded, extract the archives and copy the executables to your PATH.

# [Getting started with Prometheus](GettingStarted.md)

# [PromQL, the query language](PromQL.md)

# [Alerting](Alerting.md)

# [Building dashboards with Grafana](Grafana.md)

# [Service discovery](ServiceDiscovery.md)

# [Instrumenting applications](Instrumentation.md)

# [High-availability](HighAvailability.md)

# [Advanced topics](AdvancedTopics.md)


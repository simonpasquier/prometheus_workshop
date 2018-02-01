## Grafana

While the Prometheus UI is good for exploring the metrics and checking the
state of Prometheus, it isn't the right tool for for visualizing and graphing
time series. For this, Grafana is the de-facto solution.

### Grafana installation

Install Grafana on your system following the instructions from the official
[documentation](http://docs.grafana.org/#installing-grafana).

Go to <http://localhost:3000/> to access the Grafana UI.

Configure the Prometheus datasource pointing to <http://localhost:9090>.

*Exercise: Create a dashboard displaying the CPU, RAM and disk usage metrics.*

[< Previous](Alerting.md) - [Next >](ServiceDiscovery.md)

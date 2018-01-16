## Grafana

While the Prometheus UI is good for exploring the metrics and checking the
state of Prometheus, it isn't the right tool for for visualizing and graphing
time series. For this, Grafana is the de-facto solution.

### Grafana installation

Start Grafana:

```
docker run -d --network prometheus --name grafana -p 127.0.0.1:3000:3000 grafana/grafana:4.6.3
```

Go to <http://localhost:3000/> to access the Grafana UI.

Configure the Prometheus datasource pointing to <http://localhost:9090>.

*Exercise: Create a dashboard displaying the CPU, RAM and disk usage metrics.*


[< Previous](Alerting.md) - [Next >](ServiceDiscovery.md)

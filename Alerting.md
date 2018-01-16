## Alerting

### AlertManager installation

```
docker run -d --network prometheus --name alertmanager -p 127.0.0.1:9093:9093 \
  -v $PWD/conf/alerting/alertmanager.yml:/etc/alertmanager/config.yml  prom/alertmanager:v0.12.0
```

Restart Prometheus with the updated configuration

```
docker run -d --network prometheus --name prometheus -p 127.0.0.1:9090:9090 \
  -v $PWD/data:/prometheus \
  -v $PWD/conf/alerting/prometheus.yml:/etc/prometheus/prometheus.yml \
  -v $PWD/conf/alerting/rules.yml:/etc/prometheus/rules.yml prom/prometheus:v2.0.0
```

Go to <http://localhost:9093/> to access the AlertManager web UI.

Verify that the alert is firing in the Prometheus UI. After 1 minute or so, it
should propagate to the AlertManager.

*Exercise: create an alert that fires when the percentage of CPU idle time is less than 50%.*

[< Previous](PromQL.md) - [Next >](Grafana.md)

## Alerting

### AlertManager installation

Start AlertManager:

```
alertmanager --config.file=conf/alerting/alertmanager.yml --storage.path=data/alertmanager
```

Start the web hook receiver:

```
docker run -d --network prometheus --name webhook -p 127.0.0.1:8080:8080 \
  quay.io/simonpasquier/http_logger
```

Restart Prometheus with the updated configuration

```
prometheus --config.file=conf/alerting/prometheus.yml --storage.tsdb.path=./data/prometheus
```

Go to <http://localhost:9093/> to access the AlertManager web UI.

Verify that the alert is firing in the Prometheus UI. After 1 minute or so, it
should propagate to the AlertManager.

*Exercise: create an alert that fires when the percentage of CPU idle time is less than 50%.*

[< Previous](PromQL.md) - [Next >](Grafana.md)

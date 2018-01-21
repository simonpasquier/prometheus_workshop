## High Availability

How do you deploy a highly-available Prometheus installation? What are the limitations?

### AlertManager

AlertManager uses a Gossip-based protocol to keep track of the silences and
notifications, ensuring (at least) once delivery. Usually 2 instances are
deployed, the second instance being responsible for establishing the connection
to the first one.

Deploy the first instance

```
docker run -d --network prometheus --name alertmanager-1 -p 127.0.0.1:9093:9093 \
  -v $PWD/conf/high_availability/alertmanager.yml:/etc/alertmanager/config.yml  prom/alertmanager:v0.12.0
```

Deploy the second instance

```
docker run -d --network prometheus --name alertmanager-2 -p 127.0.0.1:9094:9093 \
  -v $PWD/conf/high_availability/alertmanager.yml:/etc/alertmanager/config.yml  prom/alertmanager:v0.12.0 \
  --config.file=/etc/alertmanager/config.yml --storage.path=/alertmanager --mesh.peer=alertmanager-1:6783
```

*Exercise: create a silence on the second AlertManager instance. Check that it
appears on the first instance too. Expire it from there and verify again that
all instances are synced.*

### Prometheus

On the Prometheus side, high availability requires to deploy (at least) 2
Prometheus servers scraping the same targets and evaluating the same rules.
This is a shared-nothing architecture to keep the operational model simple.

It means that the targets are scraped twice but it is generally not a concern
since the scrape operation has a low overhead.

One benefit with deploying 2 Prometheus servers is the ability to be alerted
when one of the servers has a problem (meta-monitoring).

Deploy the first instance

```
docker run -d --net prometheus --name prometheus-1 -p 127.0.0.1:9090:9090 \
  -v $PWD/conf/high_availability/rules.yml:/etc/prometheus/rules.yml \
  -v $PWD/conf/high_availability/prometheus.yml:/etc/prometheus/prometheus.yml \
  prom/prometheus:v2.0.0
```

Deploy the second instance

```
docker run -d --net prometheus --name prometheus-2 -p 127.0.0.1:9091:9090 \
  -v $PWD/conf/high_availability/rules.yml:/etc/prometheus/rules.yml \
  -v $PWD/conf/high_availability/prometheus.yml:/etc/prometheus/prometheus.yml \
  prom/prometheus:v2.0.0
```

*Exercise: Stop one of the Prometheus instances. Verify that the alert fired and that one notification is received.*

[< Previous](Instrumentation.md) - [Next >](AdvancedTopics.md)

## High Availability

How do you deploy a highly-available Prometheus installation? What are the limitations?

### AlertManager

AlertManager uses a Gossip-based protocol to keep track of the silences and
notifications, ensuring (at least) once delivery. Usually 2 instances are
deployed, the second instance being responsible for establishing the connection
to the first one.

Deploy the second instance

```
alertmanager --config.file=conf/alerting/alertmanager.yml --storage.path=data/alertmanager2 \
  --mesh.peer=127.0.0.1:6783 --mesh.listen-address=127.0.0.1:6784 --mesh.peer-id=00:00:00:00:00:02 \
  --web.listen-address=:9094
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

Restart the first instance with the updated configuration

```
prometheus --config.file=conf/high_availability/prometheus.yml --storage.tsdb.path=./data/prometheus
```

Start the second instance

```
prometheus --config.file=conf/high_availability/prometheus.yml --storage.tsdb.path=./data/prometheus --web.listen-address=:9091
```

*Exercise: Stop one of the Prometheus instances. Verify that the alert fired and that one notification is received.*

[< Previous](Instrumentation.md) - [Next >](AdvancedTopics.md)

## Getting started

All commands have to be executed in the `prometheus_workshop` directory.

### node_exporter installation

[node_exporter](https://github.com/prometheus/node_exporter) is a program
that collects hardware and OS metrics for Prometheus.

Start node_exporter in a terminal:

```
node_exporter
```

Go to <http://localhost:9100/> and check the results.


### Prometheus installation

Start Prometheus in another terminal:

```
prometheus --config.file=conf/getting_started/prometheus.yml --storage.tsdb.path=./data/prometheus
```

The [configuration file](conf/getting_started/prometheus.yml) tells Prometheus to scrape metrics from 3 targets:

* Prometheus itself.
* node_exporter (running on localhost).
* An fake instance that can't be reached.


### Prometheus dashboard

Go to <http://localhost:9090/> to access the Prometheus web UI.

Visit the [Targets](http://localhost:9090/targets) and check that the 3 targets
are listed, node_exporter and Prometheus should be UP.

You can click on the Prometheus target link to view the exposed metrics.

Go to the [Graph](http://localhost:9090/graph) and execute the following query:

```
up
```

The `up` metric isn't found in the metrics exposed by the endpoints, it is
instead added by Prometheus itself everytime it scrapes the target.

There are other metrics like `up` which are generated by Prometheus. To find them, execute the following query:

```
{job="unreachable"}
```

It should return something similar to:

```
scrape_duration_seconds{instance="127.0.0.1:80",job="unreachable"}                0.003171684
scrape_samples_post_metric_relabeling{instance="127.0.0.1:80",job="unreachable"}  0
scrape_samples_scraped{instance="127.0.0.1:80",job="unreachable"}                 0
scrape_series_added{{instance="127.0.0.1:80",job="unreachable"}                   0
up{instance="127.0.0.1:80",job="unreachable"}                                     0
```

You can check other metrics. For instance:

```
process_resident_memory_bytes
```

Note that we got 2 results here. Switch between *Console* & *Graph* and see what differs.

[Next >](PromQL.md)

## Getting started

### node_exporter installation

[node_exporter](https://github.com/prometheus/node_exporter) is a program
that collects hardware and OS metrics for Prometheus.

Start node_exporter:

```
docker run -d --net=host --pid=host --name node_exporter prom/node-exporter:v0.15.2
```

*node_exporter is usually not launched in Docker as it needs access to the
system host. For simplicity and consistency, we'll use Docker for everything so
we need the `--net=host` and `--pid=host` flags here. Note that non-root mount
points aren't visible to node_exporter unless bind-mounted to the container.*

Go to <http://localhost:9100/> and check the results.


### Prometheus installation

Edit the <conf/getting_started/prometheus.yml> file and replace the node_exporter's IP
address (10.0.2.15) by the IP address of your host. This configuration tells
Prometheus to scrape metrics from 3 targets:

* Prometheus itself
* node_exporter
* An fake instance that can't be reached.

Now start Prometheus:

```
docker run -d --name prometheus -p 127.0.0.1:9090:9090 \
  -v $PWD/data:/prometheus \
  -v $PWD/conf/getting_started/prometheus.yml:/etc/prometheus/prometheus.yml  prom/prometheus:v2.0.0
```

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

There are other metrics like `up`. To find them, execute the following query:

```
{job="unreachable"}
```

It should return something similar to:

```
scrape_duration_seconds{instance="127.0.0.1:80",job="unreachable"}                0.003171684
scrape_samples_post_metric_relabeling{instance="127.0.0.1:80",job="unreachable"}  0
scrape_samples_scraped{instance="127.0.0.1:80",job="unreachable"}                 0
up{instance="127.0.0.1:80",job="unreachable"}                                     0
```

You can check other metrics like for instance:

```
process_resident_memory_bytes
```

Note that we got 2 results here. Switch between *Console* & *Graph* and see what differs.


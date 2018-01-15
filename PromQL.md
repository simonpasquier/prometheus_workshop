### Prometheus data model

Everything's you need to know is very well explained in the (Prometheus
documentation)[https://prometheus.io/docs/concepts/data_model/].

At its core, the data model represents time series as a metric name followed by
a set of label names and values. Time series store timestamped float
values, the samples.

One metric with different labels:

```
process_resident_memory_bytes{instance="10.0.2.15:9100",job="node_exporter"}
process_resident_memory_bytes{instance="127.0.0.1:9090",job="prometheus"}
```

The type of a metric can be one of:
* Counter (`node_cpu`)
* Gauge (`node_memory_MemFree`)
* Histogram (`prometheus_tsdb_compaction_chunk_size_bucket`)
* Summary (`go_gc_duration_seconds`)

Histogram and summary are related and offer different trade-offs. The main
difference from a user's perspective is that histograms can be aggregated while
summaries can't (in general).

Visit again the metric endpoints and check the different metric types.

### Prometheus query language (PromQL)

PromQL is a powerful language that allows to slice and dice the data as needed.

An expression can get you all time series for a given metric name

```
node_cpu
```

It can filter to a particular CPU

```
node_cpu{cpu="cpu0"}
```

And then to a specific CPU mode

```
node_cpu{cpu="cpu0",mode="idle"}
```

But getting the total number of seconds that one CPU has spent in a given mode
isn't really meaningful. What if you want to get the percentage of time spent.
This is where we need to introduce range vectors and functions (`rate()` in particular).

Up to now, we only used instant vector selectors which return a single sample for every time serie matched by the expression. With range vector selectors, Prometheus a set of samples for every time serie.

```
node_cpu{cpu="cpu0",mode="idle"}[5m]
```

Again this expression isn't terribly useful by itself but this is where `rate()` comes to the rescue:


```
rate(node_cpu{cpu="cpu0",mode="idle"}[5m])
```

###


* Prometheus data model (labels, instant and range vectors)
* Operators (aggregation)
* Vector matching
* Functions

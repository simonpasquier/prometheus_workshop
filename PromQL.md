## PromQL

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

*Exercise: visit again the metric endpoints and check the different metric types.*

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

*Exercise: write a query that returns the percentage of idle CPU time.*

### More examples

You can aggregate metric values by arbitrary dimensions using `by` or `without`:

```
sum(node_scrape_collector_duration_seconds) without (collector)
```

Those aggregation operators are familiar if you already know SQL. PromQL has also `min()`, `max()`, `avg()`, `count()` and [more](https://prometheus.io/docs/prometheus/latest/querying/operators/#aggregation-operators).

*Exercise: write a query that returns the 5 collectors taking the most time to scrape.*


PromQL also supports vector matching for binary and arithmethic operations. Lets generate invalid requests to Prometheus:

```
curl  localhost:9090/api/v1/query
```

And now we can ask Prometheus about the percentage of HTTP requests that returned a 400 status code.

```
100 * sum(rate(http_requests_total{code="400"}[5m])) / sum(rate(http_requests_total[5m]))
```

*Exercise: modify the query to compute the percentage of HTTP requests that returned a status code between 400 and 499.*

Lets compute some percentiles now. The method depends on whether the metric is a summary or a histogram. Summaries can be recognized by their `quantile` label while histograms have a `le` label which represents the histogram's bucket (le = less or equal).

```
histogram_quantile(0.9, sum(rate(prometheus_tsdb_compaction_chunk_samples_bucket[24h])) by (job, le))
```

Summaries and histograms also track the sum and count of observed samples which can be used to compute the average value:

```
sum(rate(http_request_duration_microseconds_sum[5m])) by (job, handler)
 /
sum(rate(http_request_duration_microseconds_count[5m])) by (job, handler)
```

*Exercise: exclude the NaN values and convert to seconds.*

[< Previous](GettingStarted.md) - [Next >](Alerting.md)

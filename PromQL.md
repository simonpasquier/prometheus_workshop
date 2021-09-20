## PromQL

### Prometheus data model

Everything's you need to know is very well explained in the [Prometheus
documentation](https://prometheus.io/docs/concepts/data_model/).

At its core, the data model represents time series as a metric name followed by
a set of label names and values. Samples are numerical values
([double-precision
floating-point](https://en.wikipedia.org/wiki/Double-precision_floating-point_format)
values to be precise) associated to a timeseries at a given timestamp.

Here is the representation of a metric with different labels:

```
process_resident_memory_bytes{instance="127.0.0.1:9100",job="node_exporter"}
process_resident_memory_bytes{instance="127.0.0.1:9090",job="prometheus"}
```

The type of a metric can be one of:
* Counter (`node_cpu_seconds_total`)
* Gauge (`node_memory_MemFree_bytes`)
* Histogram (`prometheus_http_request_duration_seconds`)
* Summary (`go_gc_duration_seconds`)

Histogram and summary are related and offer different trade-offs. The main
difference from a user's perspective is that histograms can be aggregated while
summaries can't (in general).

*Exercise: visit again the Prometheus's metrics endpoint and check the different metric types.*

### Prometheus query language (PromQL)

PromQL is a powerful language that allows to slice and dice the data as needed.

An expression can get you all time series for a given metric name:

```
node_cpu_seconds_total
```

Add a label selector to filter down a particular CPU:

```
node_cpu_seconds_total{cpu="0"}
```

But getting the total number of seconds that a CPU has spent in each mode
isn't really meaningful. What if you want to get the percentage of time spent?
This is where we need to introduce range vectors and functions (`rate()` in particular).

Up to now, we've only used instant vector selectors which return a single sample
for every timeseries matching the given label selectors. With range vector
selectors, Prometheus returns the list of samples in the given time range for every timeseries.

```
node_cpu_seconds_total{cpu="0"}[5m]
```

Again this expression isn't terribly useful by itself but this is where `rate()` comes to the rescue:

```
rate(node_cpu_seconds_total{cpu="0"}[5m])
```

*Exercise: Write a query that returns the percentage of idle CPU time (hint: PromQL supports arithmetic operators).*

<details>
  <summary>Solution</summary>

```
100 * rate(node_cpu_seconds_total{cpu="0",mode="idle"}[5m])
```
</details>

### More examples

You can aggregate metric values by arbitrary dimensions using `by` or `without`:

```
sum without(collector) (node_scrape_collector_duration_seconds)
```

Those aggregation operators are familiar if you already know SQL. PromQL has also `min()`, `max()`, `avg()`, `count()` and [more](https://prometheus.io/docs/prometheus/latest/querying/operators/#aggregation-operators).

*Exercise: write a query that returns the 5 collectors taking the most time during scrapes.*

<details>
  <summary>Solution</summary>

```
topk(5, node_scrape_collector_duration_seconds)
```
</details>

PromQL also supports vector matching for binary and arithmethic operations. Lets generate invalid requests to Prometheus:

```
for i in {1..10}; do \
  # generate 400 status code response \
  curl localhost:9090/api/v1/query;
  # generate 404 status code response \
  curl localhost:9090/static/notfound;
  sleep 5
done
```

And now we can ask Prometheus about the percentage of HTTP requests that returned a 400 status code.

```
100 * sum(rate(prometheus_http_requests_total{code="400"}[5m])) / sum(rate(prometheus_http_requests_total[5m]))
```

*Exercise: modify the query to compute the percentage of HTTP requests that returned a status code between 400 and 499.*

<details>
  <summary>Solution</summary>

```
100 * sum(rate(prometheus_http_requests_total{code=~"4.."}[5m])) / sum(rate(prometheus_http_requests_total[5m]))
```
</details>

Lets compute [quantiles](https://en.wikipedia.org/wiki/Quantile) now. The method depends on whether the metric is a summary or a histogram. Summaries can be recognized by their `quantile` label while histogram metrics have a `le` label which represents the histogram's bucket (le = less or equal).

Here is an example of summary metric.

```
go_gc_duration_seconds
```

Prometheus exposes histogram metrics measuring the size of HTTP responses.

```
prometheus_http_response_size_bytes_bucket{handler="/api/v1/query"}
```

The `histogram_quantile()` function applied to histogram metrics returns an estimate of the n-th quantile.

```
histogram_quantile(0.9, rate(prometheus_http_response_size_bytes_bucket{handler="/api/v1/query"}[5m]))
```

Summaries and histograms also track the sum and count of observed samples which can be used to compute mean values:

```
sum by(job,handler) (rate(prometheus_http_request_duration_seconds_sum[5m]))
 /
sum by(job,handler) (rate(prometheus_http_request_duration_seconds_count[5m]))
```

*Exercise: understand why the result contains NaN values and find a way to exclude them.*

<details>
  <summary>Solution</summary>

```
sum by(job,handler) (rate(prometheus_http_request_duration_seconds_sum[5m]))
 /
( sum by(job,handler) (rate(prometheus_http_request_duration_seconds_count[5m])) > 0 )

```
</details>

[< Previous](GettingStarted.md) - [Next >](Alerting.md)

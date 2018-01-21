## Advanced topics

Lets now get into more advanced use cases.

### Recording rules

With recording rules, Prometheus creates new time series from existing time series, improving the response time for queries which are often executed.

*Exercise: Create a recording rule that stores the percentage of CPU idle across all CPUs.*

### Advanced relabeling

*Insert Blackbox exporter example*

### Pitfalls and gotchas

* Instrumentation
** Limit the number of values per label (a `user_id` label is probably a bad idea).
** Avoid missing time series.
** Respect the naming conventions.
* Avoid dropping labels in alerts.
* Use the `for` clause in alerts and make it neither too short (< 1m) nor too long (> 1h).
* Don't scrape targets sparsely. The maximum recommended scrape interval is 2
  minutes because otheriwse Prometheus may mark time series as stale.
* Always `rate()` before `sum()`.

### Federation

Federation allows a single Prometheus instance to gather metrics from multiple
Promethei. It is important to remember that only a subset of the original
metrics should be pulled.

### Remote storage

When you want to keep metrics around for longer than a couple of months or when you want to consolidate metrics from different locations (≠ federation), you want to look at remote storage options.

[< Previous](HightAvailability.md)

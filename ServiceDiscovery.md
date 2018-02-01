## Service Discovery

Until now, we have only declared static targets in the Prometheus configuration
file. This is the simplest way to configure targets but also the most tedious
since any update involves editing the main configuration file and reloading
Prometheus.

In this section, we will see how to configure the file service discovery. Note
that many other service discovery mechanisms exist.

### Configure the file service discovery

Restart Prometheus with the updated configuration

```
prometheus --config.file=conf/service_discovery/prometheus.yml --storage.tsdb.path=./data/prometheus
```

_Exercise: Add a target file to monitor the Grafana instance._

### Relabeling

With service discovery, it is often desirable to amend the labels attached to
the targets. In the example above, all targets have the same `job` label value.
Using the `relabel_configs` option, we could define by convention that the job
label should be equal to the filename minus the `.yml` suffix.

```
- job_name: file_sd
  file_sd_configs:
  - files:
    - /etc/prometheus/targets/*.yml
  relabel_configs:
  - source_labels:
    - __meta_filepath
    regex: .*/([^/]+).yml
    action: replace
    target_label: job
```

_Exercise: Add a relabel_config stanza to drop targets which have the `skip` label equal to `true`._

[< Previous](Grafana.md) - [Next >](Instrumentation.md)

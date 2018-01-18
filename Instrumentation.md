## Instrumenting applications

For this exercise, we'll use a very simple web application available [here](python/server.py).

```
python3 python/server.py
```

Check that the application is responding on <http://localhost:8080>.

### Add process instrumentation

Prometheus ships a [client
package](https://github.com/prometheus/client_python) to instrument Python
applications. At the minimum the library can be used to get metrics about the Python
process itself.

First, we need to install the package in a virtual environment:

```
virtualenv3 .venv
. .venv/bin/activate
pip3 install prometheus_client
```

*Exercise: implement the `metrics()` function to return Prometheus metrics.
Once done, <http://localost:8080/metrics> should return Prometheus metrics.
Hint: generate_latest() is your friend.*

### Add application metrics

It is now fairly easy to add more application metrics to the code base.

Note that the support of metric types varies from one programming language to another. For
instance, the Python client doesn't fully support summaries.

*Exercise: record request's latencies for the '/' path in a histogram.*

[< Previous](ServiceDiscovery.md) - [Next >](HighAvailability.md)

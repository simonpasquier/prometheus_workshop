## Instrumenting applications

For this exercise, we'll use a very simple web application available [here](https://github.com/simonpasquier/simple_flask_application).

```
git clone https://github.com/simonpasquier/simple_flask_application
cd simple_flask_application
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
HTTP_PORT=8000 ./run.sh
```

Check that the application is responding on <http://localhost:8000/?name=Simon>.

### Add process instrumentation

Prometheus ships a [client
package](https://github.com/prometheus/client_python) to instrument Python
applications. At the minimum the library can be used to get metrics about the Python
process itself.

First, we need to install the package in a virtual environment:

```
pip install prometheus_client
```

*Exercise: implement the `/metrics` handler to return Prometheus metrics.
Once done, <http://localost:8080/metrics> should return Prometheus metrics.*

<details>
  <summary>Solution</summary>

Check the [client_python documentation](https://github.com/prometheus/client_python/#flask) for Flask applications.

```python
from flask import Flask, escape, request, abort
from werkzeug.wsgi import DispatcherMiddleware
from prometheus_client import make_wsgi_app

[...]

app_dispatch = DispatcherMiddleware(app, {
    '/metrics': make_wsgi_app()
})
```
</details>


### Add application metrics

It is now fairly easy to add more application metrics to the code base.

Note that the support of metric types varies from one programming language to another. For
instance, the Python client doesn't fully support summaries.

*Exercise: add a counter metric tracking the number of requests received and another one tracking the number of requests that failed.*

```python
from flask import Flask, escape, request, abort
from werkzeug.wsgi import DispatcherMiddleware
from prometheus_client import make_wsgi_app, Counter

[...]


HELLO_COUNTER = Counter('hellos', 'Total number of hellos')
HELLO_FAILED_COUNTER = Counter('hellos_failed', 'Total number of failed hellos')

@app.route('/')
def hello():
    HELLO_COUNTER.inc()
    try:
        name = request.args["name"]
        return f'Hello, {escape(name)}!'
    except:
        HELLO_FAILED_COUNTER.inc()
        abort(500)

[...]
```

### Scrape metrics with Prometheus

Now Prometheus should be instructed to collect metrics from the application.

*Exercise: following what we've learned in the [previous section](ServiceDiscovery.md), reconfigure Prometheus to scrape the `/metrics` endpoint.*

[< Previous](ServiceDiscovery.md) - [Next >](HighAvailability.md)

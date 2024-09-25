#public

### Python integration

https://github.com/prometheus/client_python

### Bridges → Graphite

It is also possible to expose metrics to systems other than Prometheus. This allows you to take advantage of Prometheus instrumentation even if you are not quite ready to fully transition to Prometheus yet.

Metrics are pushed over TCP in the Graphite plaintext format.

```python
from prometheus_client.bridge.graphite import GraphiteBridge

gb = GraphiteBridge(('graphite.your.org', 2003))
# Push once.
gb.push()
# Push every 10 seconds in a daemon thread.
gb.start(10.0)
```

### Multiprocess apps

Prometheus client libraries presume a threaded model, where metrics are shared across workers. This doesn't work so well for languages such as Python where it's common to have processes rather than threads to handle large workloads.

### TODO

Regarder OpenTelemetry: https://opentelemetry.io/docs/instrumentation/python/

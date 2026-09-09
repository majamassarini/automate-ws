[![Build Status](https://travis-ci.com/majamassarini/automate-ws.svg?branch=main)](https://travis-ci.com/majamassarini/automate-ws)
[![codecov](https://codecov.io/gh/majamassarini/automate-ws/branch/main/graph/badge.svg?token=tPHRNf4csz)](https://codecov.io/gh/majamassarini/automate-ws)

## automate-home web server

The simplest user interface I was able to develop for the [automate-home project](https://github.com/majamassarini/automate-home).

## Configuration

### Grafana Loki logs link

The navbar can show a **Logs** link pointing to a Grafana Loki explore URL.
It is only visible to users with the `configure` permission, and only when configured.

Provide only the Grafana base URL (e.g. `http://your-grafana-host:3000`). The webserver
constructs the full Loki explore link automatically, opening the Loki datasource with
all logs for the last hour.

**Via INI config file** (`[webserver]` section):

```ini
[webserver]
loki_base_url = http://your-grafana-host:3000
loki_datasource_uid = P8E80F9AEF21F6940
```

The datasource UID can be found in Grafana → Connections → Data sources → Loki → the UID shown in the URL or settings page.

**Via CLI flags**:

```
--webserver-loki-base-url "http://your-grafana-host:3000"
--webserver-loki-datasource-uid "P8E80F9AEF21F6940"
```

**Via environment variables** (field test server only):

```
export LOKI_BASE_URL=http://your-grafana-host:3000
export LOKI_DATASOURCE_UID=P8E80F9AEF21F6940
```

When `loki_base_url` is not set, the Logs link is hidden.
If `loki_datasource_uid` is omitted, Grafana will try to resolve the Loki datasource by name.

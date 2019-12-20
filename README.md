[![license](https://img.shields.io/github/license/RedisTimeSeries/grafana-redistimeseries.svg)](https://github.com/RedisTimeSeries/grafana-redistimeseries)
[![CircleCI](https://circleci.com/gh/RedisTimeSeries/grafana-redistimeseries/tree/master.svg?style=svg)](https://circleci.com/gh/RedisTimeSeries/grafana-redistimeseries/tree/master)
[![GitHub issues](https://img.shields.io/github/release/RedisTimeSeries/grafana-redistimeseries.svg)](https://github.com/RedisTimeSeries/grafana-redistimeseries/releases/latest)
[![Codecov](https://codecov.io/gh/RedisTimeSeries/grafana-redistimeseries/branch/master/graph/badge.svg)](https://codecov.io/gh/RedisTimeSeries/grafana-redistimeseries)

# Jason addition
I have added a data directory and a Python program to load net asset value as well as stock ticker quotes of a few companies to test out redis.  This is included in a separate README file called README_ticker.md

# RedisTimeSeries-Datasource
Grafana Datasource for RedisTimeSeries

## QuickStart
You can tryout the `Grafana Datasource for RedisTimeSeries` with RedisTimeSeries and Grafana in a single docker compose
```bash
cd compose
docker-compose up
```
Grafana can be accessed on port 3000 (admin:admin)

## Grafana Datastore API Server
### Overview
A HTTP Server to serve metrics to Grafana via the simple-json-datasource

### Grafana configuration

1. install SimpleJson data source: https://grafana.net/plugins/grafana-simple-json-datasource/installation
2. in Grafana UI, go to Data Sources
3. Click `Add data source`
    3.1 choose Name
    3.2 Type: `SimpleJson`
    3.3 URL: point to the URL for your GrafanaDatastoreServer.py
    3.4 Access: direct (unless you are using a proxy)

4. Query the datasource by a specific key, or * for a wildcard, for example: `stats_counts.http.*`

### Dependencies
To install the needed dependencies just run: pip install -r requirements.txt

### GrafanaDatastoreServer.py Usage
```
usage: GrafanaDatastoreServer.py [-h] [--host HOST] [--port PORT]
                                 [--redis-server REDIS_SERVER]
                                 [--redis-port REDIS_PORT]

optional arguments:
  -h, --help            show this help message and exit
  --host HOST           server address to listen to
  --port PORT           port number to listen to
  --redis-server REDIS_SERVER
                        redis server address
  --redis-port REDIS_PORT
                        redis server port
```

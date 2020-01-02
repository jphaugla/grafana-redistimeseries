# net asset value demo
Initially, I wrote this as an independant github but then becamse aware of existing
github with a docker-compose ready grafana for redistimeseries.  
I forked that github 
https://github.com/jphaugla/grafana-redistimeseries

I am modifying the fork to add timeseries measures loaded from sample files from 
[yahoo finance web site](https://finance.yahoo.com/quote/TSLA/history?p=TSLA).  I pulled one year of daily
history for major indexes and then 5 years of history for several individual tickers.

For majority of information, look to the main readme
Two options for setting the environment are given:  
  * run with docker-compose using a flask and redis container
  * installing for mac os
docker-compose is much easier and is main method documented here the other method is below.

## docker compose startup
Follow the docker-compose up directions in the main README.md

### execute the load program
```bash
docker exec grafana_redis_source sh -c "python redisTS.py"
```
## Queries
By account, risk group, and instrument
```bash
ts.mrange 1576216800000 1576476000000 FILTER Account=ACCT2 RiskGroup=RG2 Instrument=N225
```
By account, risk group
```bash
ts.mrange 1576216800000 1576476000000 FILTER Account=ACCT2 RiskGroup=RG1
```
## Run on grafana
the source is all set up, so just add query and select one of the time series

##  installing on mac
1. install xcode
2. install homebrew
```bash
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```
3. verify homebrew
```bash
brew doctor
```
4. install python
```bash
brew install python
```
5. install redis-py
```bash
pip install redis
```
6.  install flask
```bash
pip install flask
```
6. clone repository
```bash
git clone https://github.com/jphaugla/reidTimeSeriesPy.git
```
7. install redis
```bash
brew install redis
```
8. start redis 
	redis-server /usr/local/etc/redis.conf


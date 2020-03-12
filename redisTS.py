import json
import csv
import redis
from datetime import datetime


def connect():
    r = redis.Redis("redis", 6379)
    return r


def datestr_to_ts(datestr):
    dt = datetime.strptime(datestr, "%Y-%m-%d")
    ts = int(dt.strftime('%s'))*1000
    return ts


def load_json_to_db(con, datafile, timeseries):
    data = json.loads(open(datafile, "r").readline())
    i = 0
    for t in data["date"]:
        ts = datestr_to_ts(t)
        v = data["values"][i]
        print("{} - {} : {}".format(timeseries, ts, v))
        con.execute_command("TS.ADD", timeseries, ts, v)
        i += 1

def load_csv_to_db_with_labels(con, datafile, instrument_id, risk_group, account_id):
    #  label_string = "labels={'Account':'" + account_id + "','RiskGroup':'" + risk_group +
    #            "','Instrument':'" + instrument_id + "'}"
    label_string = "LABELS Account " + account_id + " RiskGroup " + risk_group + " Instrument " + instrument_id
    # print("label string is " + label_string)

    hash_key = "NAV:" + account_id + ':' + risk_group + ':' + instrument_id
    # print("hash_key is " + hash_key)
    load_csv_to_db(con, datafile, hash_key, label_string)


def load_csv_to_db(con, datafile, hash_key, label_string):
    # clean up by deleting existing key
    con.delete(hash_key)
    create_command = "TS.CREATE " + hash_key + " " + label_string
    print(create_command)
    con.execute_command(create_command)
    with open(datafile) as csv_file:
        # file is comma delimited
        csv_reader = csv.reader(csv_file, delimiter=',', quoting=csv.QUOTE_NONE)
        idx = 0
        fields = next(csv_reader, None)
        #  go through all rows in the file
        for row in csv_reader:
            idx += 1
            # file columns
            # 0)Date 1)Open 2)High 3)Low 4)Close 5)Adj close 6)Volume
            ts = datestr_to_ts(row[0])
            adjusted_close = str(row[5])
            #  some files have values with the word null so ignore those
            if adjusted_close != "null":
                add_command = "TS.ADD " + hash_key + " " + str(ts) + " " + str(row[5])
                print(add_command)
                con.execute_command(add_command)
        csv_file.close()


con = connect()
con.ping()
load_csv_to_db_with_labels(con, "/data/DJI.csv", "DJI", "RG1", "ACCT1")
load_csv_to_db_with_labels(con, "/data/BTC-USD.csv", "BTC", "RG1", "ACCT1")
load_csv_to_db_with_labels(con, "/data/GSPC.csv", "GSPC", "RG1", "ACCT1")
load_csv_to_db_with_labels(con, "/data/IXIC.csv", "IXIC", "RG2", "ACCT1")
load_csv_to_db_with_labels(con, "/data/N225.csv", "N225", "RG2", "ACCT1")
load_csv_to_db_with_labels(con, "/data/TNX.csv", "TNX", "RG2", "ACCT1")

load_csv_to_db_with_labels(con, "/data/DJI.csv", "DJI", "RG1", "ACCT2")
load_csv_to_db_with_labels(con, "/data/BTC-USD.csv", "BTC", "RG1", "ACCT2")
load_csv_to_db_with_labels(con, "/data/GSPC.csv", "GSPC", "RG1", "ACCT2")
load_csv_to_db_with_labels(con, "/data/IXIC.csv", "IXIC", "RG2", "ACCT2")
load_csv_to_db_with_labels(con, "/data/N225.csv", "N225", "RG2", "ACCT2")
load_csv_to_db_with_labels(con, "/data/TNX.csv", "TNX", "RG2", "ACCT2")

load_csv_to_db(con, "/data/AAPL.csv", "APPL", "LABELS ticker AAPL")
load_csv_to_db(con, "/data/GOOG.csv", "GOOG", "LABELS ticker GOOG")
load_csv_to_db(con, "/data/IBM.csv", "IBM", "LABELS ticker IBM")
load_csv_to_db(con, "/data/TSLA.csv", "TSLA", "LABELS ticker TSLA")

print("successful completion")








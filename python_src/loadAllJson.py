#!/usr/bin/python3
import csv, json, os
from loadFiles import load_json_to_db, connect


con = connect()
json_base_directory= "/Users/jasonhaugland/Documents/Customers/Occ/json/5min/"
# read the csv and add the data to a dictionary
cnt = 0
for (dirpath, dirnames, filenames) in os.walk(json_base_directory):
    print("dirpath=" + dirpath)
    json_dirpath = dirpath + "/"
    for file in filenames:
        cnt += 1
        # print("file=" + file)
        if("json" in file):
             # print("json=" + json_name)
             # print(csv_dirpath + file)
             timeseries = file.replace(".json", "")
             load_json_to_db(con, json_dirpath + file, timeseries)
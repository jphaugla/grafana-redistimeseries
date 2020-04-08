#!/usr/bin/python3
import csv, json, os
from loadFiles import convert_csv_to_json

base_directory = "/Users/jasonhaugland/Documents/Customers/Occ/csv/5min/"
json_base_directory= "/Users/jasonhaugland/Documents/Customers/Occ/json/5min/"
# read the csv and add the data to a dictionary
cnt = 0
for (dirpath, dirnames, filenames) in os.walk(base_directory):
    print("dirpath=" + dirpath)
    json_dirpath = dirpath.replace("csv","json") + "/"
    csv_dirpath = dirpath + "/"
    print("json_dirpath=" + json_dirpath)
    for file in filenames:
        # print("file=" + file)
        if("txt" in file):
             json_name = file.replace("txt", "json")
             # print("json=" + json_name)
             # print(dirpath + file, json_dirpath + file)
             # print(json_dirpath + json_name)
             # print(csv_dirpath + file)
             convert_csv_to_json(csv_dirpath+file, json_dirpath+json_name)
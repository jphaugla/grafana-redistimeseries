#!/usr/bin/python3
import csv, json, os, datetime, sys
from loadFiles import load_json_to_db, connect



def main(argv):
  con = connect()
  print("Number of arguments:" + str(len(argv)) +  " arguments.")
  print("Argument List:" +  str(argv))

  json_base_directory=argv[0] 
  time_series_suffix=argv[1]
  # read the csv and add the data to a dictionary
  filecnt = 0
  reccnt = 0
  for (dirpath, dirnames, filenames) in os.walk(json_base_directory):
    now = datetime.datetime.now()
    print ("Start dirpath=" + dirpath + " at " + now.strftime("%Y-%m-%d %H:%M:%S"))
    json_dirpath = dirpath + "/"
    for file in filenames:
        filecnt += 1
        # print("file=" + file)
        if("json" in file):
             # print("json=" + json_name)
             # print(csv_dirpath + file)
             timeseries = file.replace(".json", "") + time_series_suffix
             thiscount = load_json_to_db(con, json_dirpath + file, timeseries)
             reccnt += thiscount
    now = datetime.datetime.now()
    print(str(reccnt) + " rows loaded")
    print(str(filecnt) + " files loaded")
    print ("end dirpath=" + dirpath + " at " + now.strftime("%Y-%m-%d %H:%M:%S"))

if '__main__' == __name__:
    main(sys.argv[1:])

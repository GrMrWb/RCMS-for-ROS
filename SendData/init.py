import socket
import json
import time,os,requests

## Determine whether to start

seagull = requests.get("https://192.168.0.100:8080/topic=/SeaGull_Topic_Bool")

seaGullMessage = seagull.text

indexForMessage = seaGullMessage.find("</h1>")

seaGullBool= seaGullMessage[indexForMessage:indexForMessage+4]
with open("UserInterface/static/home/js/data.json", "r") as f:
    datafile = json.load(f)
    datafile["Warning"]["seagull"]= if seaGullBool=="True": "1" else: "0"
    datafile["Warning"]["tide"]= if seaGullBool=="True": "1" else: "0"
    f.close

with open("UserInterface/static/home/js/data.json", "w+") as f:
    json.dump(datafile,f)
    f.close
"""
seaGullBool= seaGullMessage[indexForMessage:indexForMessage+4]
with open("UserInterface/static/home/js/data.json", "r") as f:
    datafile = json.load(f)
    datafile["Warning"]["seagull"]= if seaGullBool=="True": "1" else: "0"
    datafile["Warning"]["tide"]= if seaGullBool=="True": "1" else: "0"
    f.close

with open("UserInterface/static/home/js/data.json", "w+") as f:
    json.dump(datafile,f)
    f.close

seaGullBool= seaGullMessage[indexForMessage:indexForMessage+4]
with open("UserInterface/static/home/js/data.json", "r") as f:
    datafile = json.load(f)
    datafile["Warning"]["seagull"]= if seaGullBool=="True": "1" else: "0"
    datafile["Warning"]["tide"]= if seaGullBool=="True": "1" else: "0"
    f.close

with open("UserInterface/static/home/js/data.json", "w+") as f:
    json.dump(datafile,f)
    f.close

seaGullBool= seaGullMessage[indexForMessage:indexForMessage+4]
with open("UserInterface/static/home/js/data.json", "r") as f:
    datafile = json.load(f)
    datafile["Warning"]["seagull"]= if seaGullBool=="True": "1" else: "0"
    datafile["Warning"]["tide"]= if seaGullBool=="True": "1" else: "0"
    f.close

with open("UserInterface/static/home/js/data.json", "w+") as f:
    json.dump(datafile,f)
    f.close"""

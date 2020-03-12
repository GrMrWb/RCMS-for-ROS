import requests

r=requests.get("http://192.168.0.100:8080/stream_viewer?topic=/Seagull_Topic_Bool")

print(r.text)
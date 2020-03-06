import requests

r=requests.get("http://192.168.0.100:8080/stream_viewer?topic=/topcam/image_raw")

print(r.text)
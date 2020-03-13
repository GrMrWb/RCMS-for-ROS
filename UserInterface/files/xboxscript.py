import requests

i=0
while i<100:
    r=requests.get("http://localhost:8000/instruction/"+ str(i) + "/120")
    r=requests.get("http://localhost:8000/current/"+ str(i+100) + "/120")
    print(r.text)
    i+=1

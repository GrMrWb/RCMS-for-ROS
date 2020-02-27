import socket
import json
import time
from ConnectSignal import ImpIrt

with open("UserInterface/static/home/js/data.json", "r") as f:
    dataf = json.load(f)
    termi = dataf["Termination"]
f.close()

print("Give the IP of the server")
a=input()
b=input(".")
c=input(".")
d=input(".")
IP=ImpIrt.getIP(a,b,c,d)

print("Give the port")
port=input()

while termi !="1":
    UDP_IP = IP
    UDP_PORT = port
    MESSAGE = termi

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))

    time.sleep(100)

else:

    termi = input("Ready to start")

    while termi !="1":
        UDP_IP = IP
        UDP_PORT = port
        MESSAGE = termi

        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))

        time.sleep(100)


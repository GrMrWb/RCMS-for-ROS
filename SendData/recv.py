import socket
import json
from SendData.datasending import ThreadingRecv

# IP address of the compute
v=1.0
with open("data.json",r) as f:
    term=json.load(f)
    termi=term["termination"]

try:
    UDP_IP = "127.0.0.1"
    UDP_PORT = 2150
    MESSAGE="READY"
    readySock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    readySock.sendto((MESSAGE)(UDP_IP, UDP_PORT)) 
    readySock.close()
    time.sleep(20)
except:
    UDP_IP = "127.0.0.1"
    UDP_PORT = 2150
    MESSAGE="READY"
    readySock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    readySock.sendto((MESSAGE)(UDP_IP, UDP_PORT)) 
    readySock.close()
    time.sleep(10)
readSock.close()

while termi!="0":
    # Processing
    UDP_IP = "127.0.0.1"
    UDP_PORT = 2145
    procSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    procSock.bind((UDP_IP, UDP_PORT))
    procdata, addr = procSock.recvfrom(16)

    # PowerBoard
    UDP_IP = "127.0.0.1"
    UDP_PORT = 2147
    prbSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    prbSock.bind((UDP_IP, UDP_PORT))
    prbdata, addr = procSock.recvfrom(16)

    # Seagull
    UDP_IP = "127.0.0.1"
    UDP_PORT = 2149
    seaGullSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    seaGullSock.bind((UDP_IP, UDP_PORT))
    seaGulldata, addr = seaGullSock.recvfrom(2)

    # Bin Allocation
    UDP_IP = "127.0.0.1"
    UDP_PORT = 2153
    binSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    binSock.bind((UDP_IP, UDP_PORT))
    bindata, addr = binSock.recvfrom(16)

    with open("UserInterface/static/home/js/data.json", "r") as f:
        dataf = json.load(f)
        termi =dataf["Termination"]
    f.close()

    dataf["v"]=v.__str__

    procdatanew=procdata.split(':'), i=0
    for x in procdatanew:
        if i==0:
            if dataf["TriTrackDataMic"]["PiStat"]!=x:
                dataf["TriTrackDataMic"]["PiStat"]=x
                
            i+=1
        if i==1:
            if dataf["TriTrackDataMic"]["Pi4procTri"]!=x:
                dataf["TriTrackDataMic"]["Pi4procTri"]=x
            i+=1  
        if i==2:
            if dataf["TriTrackDataMic"]["BrdStat"]!=x:
                dataf["TriTrackDataMic"]["BrdStat"]=x
            i+=1
        if i==3:
            if dataf["TriTrackDataMic"]["BrdProc"]!=x:
                dataf["TriTrackDataMic"]["BrdProc"]=x
            i+=1

    prbdatanew=prbdata.split(':'), i=0
    for x in prbdatanew:
        if i==0:
            if dataf["TriTrackPowerBoard"]["Consumption"]!=x:
                dataf["TriTrackPowerBoard"]["Consumption"]=x
            i+=1
        if i==1:
            if dataf["TriTrackPowerBoard"]["CapA"]!=x:
                dataf["TriTrackPowerBoard"]["CapA"]=x
            i+=1  
        if i==2:
            if dataf["TriTrackPowerBoard"]["CapB"]!=x:
                dataf["TriTrackPowerBoard"]["CapB"]=x
            i+=1

    bindatanew=bindata.split(':'), i=0
    for x in bindatanew:
        if i==0:
            if dataf["Rubbish"]["BinA"]!=x:
                dataf["Rubbish"]["BinA"]=x
            i+=1
        if i==1:
            if dataf["Rubbish"]["BinB"]!=x:
                dataf["Rubbish"]["BinB"]=x
            i+=1  
        if i==2:
            if dataf["Rubbish"]["BinC"]!=x:
                dataf["Rubbish"]["BinC"]=x
            i+=1

    dataf["Rubbish"]["ColRub"] = int(dataf["Rubbish"]["BinA"]) + int(dataf["Rubbish"]["BinA"]) + int(dataf["Rubbish"]["BinA"])

    if seaGulldata=="True":
        dataf["Warning"]["seagull"]=1
    else:
        dataf["Warning"]["seagull"]=0


    with open("UserInterface/static/home/js/data.json", "w+") as f:
        f.write = json.dumps(f)
    f.close()

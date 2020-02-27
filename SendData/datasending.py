import json
import socket, socketserver, ipaddress

#ignore any problem which will appear
import rospy
from std_msgs.msg import String

termi="0"

def seagullDetect(data):
    
    with open('data.json',"r+") as f:
        dataToSend = json.load(f)
        dataToSend["Warning"]["Seagull"]=data
    f.close()

    with open('data.json',"w+") as f:
        f.write(json.dumps(dataToSend))
    f.close()

def procInfo(data):
    # Processing
    MESSAGE=data
    UDP_IP = "127.0.0.1"
    UDP_PORT = 2145
    procSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    procSock.sendto((MESSAGE)(UDP_IP, UDP_PORT)) 

def prbInfo(data):
    # PowerBoard
    MESSAGE=data
    UDP_IP = "127.0.0.1"
    UDP_PORT = 2147
    prbSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    prbSock.sendto((MESSAGE)(UDP_IP, UDP_PORT))

def binalloInfo(data):
    # Bin Allocation
    MESSAGE=data
    UDP_IP = "127.0.0.1"
    UDP_PORT = 2146
    binSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    binSock.sendto((MESSAGE)(UDP_IP, UDP_PORT))

def seagullInfo(data):
    # Seagull
    MESSAGE=data
    UDP_IP = "127.0.0.1"
    UDP_PORT = 2148
    seaGullSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    seaGullSock.sendto((MESSAGE)(UDP_IP, UDP_PORT)) 
        

def listener():
    while termi !="1":
        with open('data.json', "r+") as f:
            dataToSend = json.load(f)
        f.close()

        termi = dataToSend["Termination"]

        rospy.init_node('Seagull_Topic_Bool') # define the name of the node
        rospy.Subscriber("chatter", String, seagullDetect)
        # spin() simply keeps python from exiting until this node is stopped
        rospy.spin()

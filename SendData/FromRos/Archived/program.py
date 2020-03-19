import json,time
import socket, socketserver, ipaddress
from SendData.datasending import IntegrateData, ThreadingSend

#ignore any problem which will appear
import rospy
from std_msgs.msg import String

readymsg=""
while readymsg !="READY":
    UDP_IP = "127.0.0.1"
    UDP_PORT = 2150
    readSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    readSock.bind((UDP_IP, UDP_PORT))
    readymsg, addr = readSock.recvfrom(10)
readSock.close()

termi=ThreadingSend()

while termi =='1':
    # define the name of the node
    nodeName=""
    
    # === Processing
    topic_name="Processing_Topic" # UDP_PORT = 2145
    rospy.init_node(nodeName) 
    rospy.Subscriber(topic_name, String,IntegrateData.sendInfoProcess)
    time.sleep(50)

    # === PowerBoard
    topic_name="Processing_Topic" # UDP_PORT = 2147
    rospy.init_node(nodeName)
    rospy.Subscriber(topic_name, String,IntegrateData.sendInfoPowerBoard)
    time.sleep(50)

    # === SeaGull
    topic_name="SeaGull_Topic_Bool" # UDP_PORT = 2148
    rospy.init_node(nodeName)
    rospy.Subscriber(topic_name, String,IntegrateData.sendInfoSeaGull)
    time.sleep(50)

    termi=ThreadingSend.IsTerminated

    time.sleep(320)
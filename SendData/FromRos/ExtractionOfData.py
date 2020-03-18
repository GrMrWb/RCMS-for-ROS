import json,time,requests
import socket, socketserver, ipaddress

#ignore any problem which will appear
import rospy
from std_msgs.msg import String

ip="192.168.0.102"

def position(data):
    r=requests.get("https://"+ ip +"/cordsFromRos/"+data)
    print(r.text)

def dataProc(data):
    r=requests.get("https://"+ ip +"/data/"+data)
    print(r.text)

def warning(data): 
    r=requests.get("https://"+ ip +"/warning/"+ data + "/" + data)
    print(r.text)

def listener():
    # Position
    rospy.init_node('node_name')
    rospy.Subscriber("position", String, position)

    # Processing    
    rospy.init_node('node_name')
    rospy.Subscriber("processing", String, callback)

    # Warning
    rospy.init_node('node_name')
    rospy.Subscriber("warning", String, callback)

    rospy.spin()


    
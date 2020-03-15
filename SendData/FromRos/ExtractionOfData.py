import json,time,requests
import socket, socketserver, ipaddress

#ignore any problem which will appear
import rospy
from std_msgs.msg import String

def postion(data):
    
    

def listener():

    # Position
    rospy.init_node('node_name')
    rospy.Subscriber("chatter", String, callback)

    rospy.spin()

def __main__():

    
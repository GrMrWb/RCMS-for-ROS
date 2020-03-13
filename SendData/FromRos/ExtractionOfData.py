import json,time
import socket, socketserver, ipaddress

#ignore any problem which will appear
import rospy
from std_msgs.msg import String

def postion(data):
    rospy.loginfo("I heard %s",data.data)
def __main__():

    
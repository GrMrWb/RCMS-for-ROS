import json
import socket, socketserver, ipaddress
import threading, time

#ignore any problem which will appear
import rospy
from std_msgs.msg import String

termi="0"

class IntegrateData(object):
    def __init__(self):
        self.dataProcess=""
        self.dataPowerBoard=""
        self.dataSeaGull=""
        self.UDP_IP = "127.0.0.1"
        self.UDP_PORT = 2145

    def sendInfoProcess(self,data):
        if self.dataProcess!=data:
            self.dataProcess=data
            self.UDP_PORT= 2145
            procSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            procSock.sendto((self.dataProcess)(self.UDP_IP, self.UDP_PORT)) 
            procSock.close()
            pass
        else:
            pass

    def sendInfoPowerBoard(self,data):
        if self.dataPowerBoard!=data:
            self.dataPowerBoard=data
            self.UDP_PORT= self.UDP_PORT+2
            prbSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            prbSock.sendto((self.dataPowerBoard)(self.UDP_IP, self.UDP_PORT)) 
            prbSock.close()
            pass
        else:
            pass

    def sendInfoSeaGull(self,data):
        if self.sendInfoSeaGull!=data:
            self.dataSeaGull=data
            self.UDP_PORT= self.UDP_PORT+2
            seaGullSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            seaGullSock.sendto((self.dataSeaGull)(self.UDP_IP, self.UDP_PORT)) 
            seaGullSock.close()
            pass    
        else:
            pass

class ThreadingSend(object):

    """ 
    Threading example class
    The run() method will be started and it will run in the background until the application exits.
    """

    def __init__(self, interval=20, data=None):
        self.interval = interval
        self.data=data
        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True                            
        thread.start()

    def IsTerminated(self):
        termination=self.data
        return termination

    def run(self):
        UDP_IP = "127.0.0.1"
        UDP_PORT = 2150
        termSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        termSock.bind((UDP_IP, UDP_PORT))
        termination, addr = termSock.recvfrom(6)

        self.data=termination

        time.sleep(self.interval)

class ThreadingRecv(object):
    
    """ 
    Threading example class
    The run() method will be started and it will run in the background until the application exits.
    """

    def __init__(self, interval=20, data=None):
        self.interval = interval
        self.data=data
        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True                            
        thread.start()

    def IsTerminated(self):
        termination=self.data
        return termination

    def run(self):
        with open("data.json",r) as f:
            term=json.load(f)
            MESSAGE=term["termination"]
            f.close()

        UDP_IP = "127.0.0.1"
        UDP_PORT = 2150
        readySock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        readySock.sendto((MESSAGE)(UDP_IP, UDP_PORT)) 
        readySock.close()



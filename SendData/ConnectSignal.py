import os
import socket

class ImpIrt:

    def _init_(self, termination):
        termination = 0

    def isTerminated(self):
        self.termination
        return termination

    def getIP(self,a,b,c,d):
        IP= a + "." + b + "." + c + "."+ d
        return IP

    def establishUDPConn(self,IP):
        UDP_IP = IP
        UDP_PORT = 2144
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind((UDP_IP, UDP_PORT))
        return 0
    
    

import socket
import time

HOST = "169.254.121.4"
PORT  = 30002

class Connect:
    def __init__(self):
        global HOST
        global PORT
        self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        self.s.bind((HOST,PORT))
        self.s.listen(5)
        c, addr = self.s.accept()
        self.c = c

    def sendAndGetMessage(self,message):
        self.c.send(message.encode())
        time.sleep(1)

        msg = self.c.recv(1024)
        #print(msg)
        self.c.close()
        self.s.close()

        return msg

    def onlySendMessage(self,message):
        self.c.send(message.encode())
        time.sleep(1)

        self.c.close()
        self.s.close()

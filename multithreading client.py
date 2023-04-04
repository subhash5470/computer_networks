import socket
from threading import *

class Chat(Thread):
    def __init__(self,con):
        Thread.__init__(self)
        self.con=con
    def run(self):
         name=current_thread().getName()

         while True:
            if name=='sender':
               data=input('server:')
               self.con.send(bytes(data,'utf-8'))
            elif name=='receiver':
               recvdata = self.con.recv(1024).decode()
               print('client:', recvdata)

port=8821
host='127.0.0.1'
clt=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clt.connect((host,port))

sender=Chat(clt)
sender.setName('sender')
receiver=Chat(clt)
receiver.setName('receiver')
sender.start()
receiver.start()
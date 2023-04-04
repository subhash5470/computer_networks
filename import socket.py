import socket

clt=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
clt1=("192.168.56.1",8500)
clt.connect(clt1)
#message=input("Enter the message")
# clt.send(bytes(str(message),"utf-8"))
#data=clt.recv(1000)

# clt=socket.socket()
# clt1=("localhost",5999)
# clt.connect(clt1)
print(clt.recv(1024).decode())
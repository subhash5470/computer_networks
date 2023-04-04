import socket
c=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host=socket.gethostname()
port=9809
c.connect((host,port))
c.send(bytes('hi server','utf-8'))

with open('hello.txt','wb') as f:
    print('file is opened')
    while True:
        data=c.recv(2000)
        print(data)
        if not data:
           break
        f.write(data)
f.close()
print('Successfully get the file')
c.close()
print('connection closed')
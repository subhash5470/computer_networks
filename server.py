import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host=socket.gethostname()
port=9809
s.bind((host,port))
s.listen(5)
print('server is started')
while True:
    c,caddr=s.accept()
    print(caddr)
    data=c.recv(2000)
    print(data.decode())
    fn='hello.txt'
    f=open(fn,'rb')
    m=f.read(2000)
    while(m):
        print(c.send(bytes(str(m), 'utf-8')))
        m = f.read(2000)
    f.close()
    print('sending completed')
    c.send(bytes('connected', 'utf-8'))
    c.close()
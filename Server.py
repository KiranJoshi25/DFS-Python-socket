import socket
from os import listdir

port = 1234
    
i=0
path = '.'
    

while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('10.0.0.99', port))
    s.listen(10)
    clientsocket, address = s.accept()
    print("connection ",i)
    print(f"Connection from {address} has been established.")
    msg = clientsocket.recv(1024)
    msg = msg.decode("utf-8")
    print(msg)
    if msg == 'list':
        test=''
        Flist = [f for f in listdir(path)]
        for x in Flist:
            test+=x+'\n'
            print(x)
        #clientsocket.send(bytes('\0','utf-8'))
        clientsocket.send(bytes(test,'utf-8'))
    elif msg == 'read':
        clientsocket.send(bytes("enter the name of file",'utf-8'))
        msg1 = clientsocket.recv(1024)
        msg1 = msg1.decode('utf-8')
        f = open('C:/Users/Kiran/Desktop/%s' % msg1, 'r')
        test=''
        for x in f:
            test+=x+'\n'
            print(x)
        clientsocket.send(bytes(test,'utf-8'))
    elif msg == 'write':
        clientsocket.send(bytes("enter the name of file",'utf-8'))
        msg1 = clientsocket.recv(1024)
        msg1 = msg1.decode('utf-8')
        print(msg1)
        f = open(msg1,'a')
        clientsocket.send(bytes("enter the data to be appended in a file:",'utf-8'))
        msg2 = clientsocket.recv(1024)
        msg2 = msg2.decode('utf-8')
        f.write(msg2)
        f.close()
        f = open(msg1, 'r')
        test=''
        for x in f:
            test+=x+'\n'
            print(x)
        clientsocket.send(bytes(test,'utf-8'))
    i+=1
    s.close()

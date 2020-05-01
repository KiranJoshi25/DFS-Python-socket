import socket
from os import listdir
import time

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
            
        #clientsocket.send(bytes('\0','utf-8'))
        clientsocket.send(bytes(test,'utf-8'))
    elif msg == 'read':
        clientsocket.send(bytes("enter the name of file",'utf-8'))
        msg1 = clientsocket.recv(1024)
        msg1 = msg1.decode('utf-8')
        f = open(msg1, 'r')
        test=''
        for x in f:
            test+=x+'\n'
        
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
        f.write('\n'+msg2)
        f.close()
       
        clientsocket.send(bytes('file written successfully','utf-8'))
    elif msg == 'View':
        clientsocket.send(bytes("enter the name of file",'utf-8'))
        msg1 = clientsocket.recv(1024)
        msg1 = msg1.decode('utf-8')
        f = open(msg1, 'r')
        test=f.read(5000)
       
        while True:
            clientsocket.send(bytes(test,'utf-8'))
            time.sleep(1)
            test = f.read(5000)
        
        
    
    s.close()

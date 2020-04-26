import socket
from os import listdir
port = 1234
print('connected to the remote server:',socket.gethostname(),'port 1234')


print('server is listening')
def main():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('10.0.0.99', port))

        print('--------------------------------------------')
        print('Make your choice')
        print('1)List : list of all the files in system')
        print('2)Read : Read the specified file')
        print('3)Write : Append data the specified file')
        print('--------------------------------------------')
        client_input = int(input('enter a your choice'))
        if client_input == 1:
            s.send(bytes("list",'utf-8'))
            
            msg = s.recv(5000)
            msg = msg.decode("utf-8")
            print(msg)
            
        if (client_input == 2):
            s.send(bytes("read",'utf-8'))
            msg = s.recv(1024)
            msg = msg.decode('utf-8')
            print(msg)
            i = input('enter a filename')
            s.send(bytes(i,'utf-8'))
            msg = s.recv(50000)
            msg = msg.decode("utf-8")
            print(msg)
        if (client_input == 3):
            s.send(bytes("write",'utf-8'))
            msg = s.recv(1024)
            msg = msg.decode('utf-8')
            print(msg)
            i = input("enter file name to write:")
            s.send(bytes(i,'utf-8'))
            msg1 = s.recv(1024)
            msg1 = msg1.decode('utf-8')
            Data = input('Enter data to be appended')
            s.send(bytes(Data,'utf-8'))
            msg3 = s.recv(50000)
            msg3 = msg3.decode("utf-8")
            print(msg3)
            
if __name__ == "__main__":
    main()
    
    


       

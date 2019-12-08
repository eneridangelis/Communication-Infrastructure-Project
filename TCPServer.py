from socket import *
import os


dnsAddress = ("0.0.0.0", 1080)
serverName = "localhost"

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((serverName, serverPort))

serverSocket.listen(1)

print('The server is ready to recieve')

while True:
    connectionSocket, addr = serverSocket.accept()
    print('Got connection from' + repr(addr))
    sentence = connectionSocket.recv(1024)
    print('Server recieved' + sentence)
    connectionSocket.send('Ready for requests')
    while True:
        op = connectionSocket.recv(1024)
        if op == '1':
            dir_list = os.listdir('Arquivos')
            print(dir_list)
            files = ''
            for i in dir_list:
                files += './' + i + '\n'
            connectionSocket.send(files)
            list_response = connectionSocket.recv(1024)
            print(list_response)
        elif op == '2':
            connectionSocket.send('Type file name: ')
            filename = connectionSocket.recv(1024)
            f = open('Arquivos/' + filename, 'rb')
            filesize = str(os.path.getsize('Arquivos/' + filename))
            print(filesize)
            connectionSocket.send(filesize)
            ready = connectionSocket.recv(1024)
            print(ready)
            l = f.read(1024)
            while (l):
                connectionSocket.send(l)
                l = f.read(1024)
            f.close()
            print('Done Sending')
            
        else:
            connectionSocket.close()

from socket import *
import os

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('The server is ready to recieve')
while True:
    connectionSocket, addr = serverSocket.accept()
    print('Got connection from' + repr(addr))
    sentence = connectionSocket.recv(1024)
    print('Server recieved' + sentence)
    
    dir_list = os.listdir('Arquivos')
    print(dir_list)
    files = ''
    for i in dir_list:
        files += './' + i + '\n'
    connectionSocket.send(files)
    
    list_response = connectionSocket.recv(1024)
    print(list_response)

    filename = connectionSocket.recv(1024)
    f = open('Arquivos/' + filename, 'rb')
    l = f.read(1024)
    while (l):
        connectionSocket.send(l)
        l = f.read(1024)
    f.close()

    print('Done Sending')
    # connectionSocket.send('Thank you for connecting')
    connectionSocket.close()
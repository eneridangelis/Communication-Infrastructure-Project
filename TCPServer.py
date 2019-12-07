from socket import *
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
    
    filename = 'doggo.jpg'
    f = open(filename, 'rb')
    l = f.read(1024)
    while (l):
        connectionSocket.send(l)
        print('Sent ' + l)
        l = f.read(1024)
    f.close()

    print('Done Sending')
    # connectionSocket.send('Thank you for connecting')
    connectionSocket.close()
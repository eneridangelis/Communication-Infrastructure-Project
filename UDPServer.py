from socket import *
import pickle 

sendSeq = 0
sendACK = 0
expectedSeq = 0
expectedACK = 0

def rdtSend(serverSocket, clientAddress, message):
    global sendSeq
    global sendACK
    packet = (sendSeq, sendACK, message)   
    data = pickle.dumps(packet)
    serverSocket.sendto(data, clientAddress)
    while True:
        try:
            recvData = serverSocket.recvfrom(1024)
        except:
            print('temporizador estourou')
            serverSocket.sendto(data, clientAddress)
        else:
            recvSeq, recvACK, recvMessage = pickle.loads(recvData[0])
            if recvACK == sendACK:
                if sendACK == 0:
                    sendACK = 1
                    sendSeq = 1
                else:
                    sendACK = 0
                    sendSeq = 0
                return 

def rdtRecv(serverSocket):
    global expectedACK
    while True:
        try: 
            recvData = serverSocket.recvfrom(1024)
        except:
            print('temporizador estourou')
        else:
            recvSeq, recvACK, recvMessage = pickle.loads(recvData[0])
            if recvSeq == expectedACK:
                packet = (expectedSeq, expectedACK, '')
                data = pickle.dumps(packet)
                serverSocket.sendto(data, recvData[1])
                if expectedACK == 0:
                    expectedACK = 1
                else:
                    expectedACK = 0
                return (recvMessage, recvData[1])
            else:
                if expectedACK == 0:
                    packet = (expectedSeq, 1, '')
                    data = pickle.dumps(packet)
                    serverSocket.sendto(data, recvData[1])
                else:
                    packet = (expectedSeq, 0, '')
                    data = pickle.dumps(packet)
                    serverSocket.sendto(data, recvData[1])

dnsPort = 15000
dnsHost = '127.0.0.1'

serverAlias = 'luneri.com'
serverPort = 12000
serverHost = '127.0.0.1'

dnsSocket = socket(AF_INET, SOCK_DGRAM)
message = serverAlias + ' ' + serverHost
dnsSocket.sendto(message, (dnsHost, dnsPort))
recvMessage = dnsSocket.recvfrom(1024)[0]
print(recvMessage)
dnsSocket.close()


serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.settimeout(2.0)
serverSocket.bind((serverHost, serverPort))
print("The server is ready to recieve")
message, clientAddress = rdtRecv(serverSocket)
print(message)
message, clientAddress = rdtRecv(serverSocket)
print(message)
    
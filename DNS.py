from socket import *

dnsPort = 1080
dnsSocket = socket(AF_INET, SOCK_DGRAM)

dnsSocket.bind(('', dnsPort))

serverName, serverAddress = dnsSocket.recvfrom(2048)

while 1:
	message, clientAddress = dnsSocket.recvfrom(2048)
	if (message.decode() != serverName.decode()):
		response = "Nao foi possivel conectar com '" + message.decode() + "'."
	else:
		response1 = serverAddress[0]
		response2 = str(serverAddress[1])

	dnsSocket.sendto(response1.encode(), clientAddress)
	dnsSocket.sendto(response2.encode(), clientAddress)



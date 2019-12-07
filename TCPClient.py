from socket import *

#172.22.70.249
serverName = '172.22.68.47'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
sentence = 'Hello Server'
clientSocket.send(sentence)

listinha = clientSocket.recv(1024)
print(listinha) 

clientSocket.send('Received List')

file_name = raw_input('Type file name:')
clientSocket.send(file_name)

with open('Downloads/' + file_name,'wb') as f:
	while 1:
		print('Receiving Data...')
		data = clientSocket.recv(1024)
		if not data:
			break
		f.write(data)
		

f.close()
print('File Received')
clientSocket.close()
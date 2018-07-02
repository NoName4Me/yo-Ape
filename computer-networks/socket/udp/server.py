from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print('The server is ready to receive')
while 1:
    message, clientAdress = serverSocket.recvfrom(2048)
    print('get a messge: ',message.decode())
    modifiedMessage = message.upper()
    serverSocket.sendto(modifiedMessage, clientAdress)
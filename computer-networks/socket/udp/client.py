from socket import *

def raw_input(tip):
    return input(tip).encode() # string --> bytes

serverName = 'localhost'
serverPot = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM) #ipv4, UDP
while 1:
    message = raw_input('Input lowercase sentence:')
    clientSocket.sendto(message, (serverName, serverPot))
    modifiedMessage, serverAdress  = clientSocket.recvfrom(2048)
    print(modifiedMessage.decode())
    
clientSocket.close()

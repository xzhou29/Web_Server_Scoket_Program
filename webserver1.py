#import socket module
from socket import *

serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket

#Fill in start

HOST, PORT = '108.222.245.14', 8910

try:
        serverSocket.bind((HOST, PORT))
except socket.error as e:
        print(str(e))
serverSocket.listen(1)

print ('Serving HTTP on port %s ...' % PORT)

#Fill in end

while True:
#Establish the connection
    print ('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(1024)
        print message
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()
        #Send one HTTP header line into socket
        
        #Fill in start
        connectionSocket.send('HTTP/1.1 200 OK\r\n\r\n')
        #Fill in end
        
        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i])
        connectionSocket.close()
    except IOError:
            
    #Send response message for file not found
    #Fill in start
        connectionSocket.send('HTTP/1.1 200 OK\r\n\r\n 404 File Not Found!\r\n\r\n')
    #Fill in end
    #Close client socket
    #Fill in start
        connectionSocket.close()
    #Fill in end


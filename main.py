import sys
from socket import *
import threading

serverPort = 11000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('Server is ready to listen')

def handleClient(connectionSocket, addr):
    while True:
        print(addr)
        sentence = connectionSocket.recv(1024).decode()
        print('Received:', sentence)
        words = sentence.strip().split()

        if 'reverse:' in words:
            revSentence = sentence[::-1]
            connectionSocket.send(revSentence.encode())

        elif 'upper:' in words:
            capSentence = sentence.upper()
            connectionSocket.send(capSentence.encode())

        elif 'lower:' in words:
            lowSentence = sentence.lower()
            connectionSocket.send(lowSentence.encode())

        elif 'close;' in words:
            connectionSocket.close()
            break
        else:
            capSentence = sentence.upper()
            connectionSocket.send(capSentence.encode())








while True:
    connectionSocket, addr = serverSocket.accept()
    threading.Thread(target=handleClient, args=(connectionSocket, addr)).start()





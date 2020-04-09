import socket
import struct
import json

TCP_IP = 'localhost'
TCP_PORT = 3001      
BUFFER_SIZE = 4096
data = str(json.load(open('profile.json'))).encode('utf-8')

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

totalSent = 0
while totalSent < len(data):
    sent = s.send(data[totalSent:])
    totalSent += sent

if totalSent == len(data):
    print("Sent !")
    msg = s.recv(BUFFER_SIZE)
        

print("received data:", msg.decode('utf-8'))
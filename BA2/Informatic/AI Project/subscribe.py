import socket, os, json
from transmitJSON import sendJSON

HOST = '127.0.0.1'
PORT = 3001
ROOT = os.path.abspath(os.getcwd())

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

with open ('profile.json', 'r') as file:
    data = json.load(file)
    
sendJSON(client, data)

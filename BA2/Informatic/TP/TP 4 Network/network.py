import socket
import sys
import threading

def network():
    print(socket.getfqdn('www.ecam.be'))
    print(socket.gethostname())
    print(socket.gethostbyname('www.ecam.be'))  
    print(socket.gethostbyaddr('172.17.0.99'))

    s = socket.socket()  
    s.connect(('www.python.org', 80)) #connection à une machine
    print(s.getsockname()) #adresse IPV4, port de l'hôte
    s.close() #ferme la connexion

def UDPSend(): 
    s = socket.socket(type=socket.SOCK_DGRAM)
    data = "Hello World !".encode() #conversion en binaire
    sent = s.sendto(data, ('localhost', 5000))
    if sent == len(data):
        print("Sent !")

def UDPReceive():
    s = socket.socket(type=socket.SOCK_DGRAM)
    s.bind(('O.O.O.O', 5000))

    data = s.recvfrom(512)[0].Decode()
    print('Received', len(data), 'octets : ')
    print(data)

class Chat():
    def __init__(self, host = "0.0.0.0", port = 5000) :
        self.__s = socket.socket(type=socket.SOCK_DGRAM)
        self.__s.settimeout(0.5)
        self.__s.bind((host, port))
        print(f"Listen on {host}:{port}")

    def _exit(self):
        self.__running = False
        self.__address = None
        self.__s.close()

    def _quit():
        self.__address = None

    def _join(self, param):
        tokens = param.split(' ')
        if len(tokens) == 2:
            self.__address = (socket.gethostbyaddr(tokens[0])[0], int(tokens[1]))

    def _send(self, param):
        if self.__address is not None:
            message = param.encode()
            totalsent = 0
            while totalsent < len(message):
                sent = self.__s.sendto(message[totalsent:], self.__address)
                totalsent += sent

    def _receive(self):
        while self.__running:
            try:
                data, address = self.__s.recvfrom(1024)
                print(data.decode())
            except socket.timeout:
                pass
    def run(self):
        handlers = {
            '/exit': self._exit,
            '/quit': self._quit,
            '/join': self._join,
            '/send': self._send
        }
        self.__running = True
        self.__address = None
        threading.Thread(target=self._receive).start()

        while self.__running:
            line = sys.stdin.readline().rstrip() + ' '
            command = line[:line.index(' ')]
            param = line[line.index(' ')+1:].rstrip()
            if command in handlers:
                handlers[command]() if param == '' else handlers[command](param)
            else :
                print('Unknown command: ', command)

port = int(sys.argv[1])
Chat().run()
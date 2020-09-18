import socket, json, transmitJSON, cherrypy, sys, copy, time
from random import randint
from ai.ai import AI

HOST = '0.0.0.0'
PORT = 8081

directions = {'RIGHT': [0, 1], 'LEFT': [0, -1], 'UP': [-1, 0], 'DOWN': [1, 0],
              'UPRIGHT': [-1, 1], 'UPLEFT': [-1, -1], 'DOWNRIGHT': [1, 1], 'DOWNLEFT': [1, -1]}


class Server:
    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def move(self):
        # Deal with CORS
        cherrypy.response.headers['Access-Control-Allow-Origin'] = '*'
        cherrypy.response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
        cherrypy.response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization, X-Requested-With'
        if cherrypy.request.method == "OPTIONS":
            return ''

        body = cherrypy.request.json
        for key, value in body.items():
            if key == "game":
                map = value
            if key == "players":
                player = value
            if key == "you":
                me = value
        if player[0] == me:
            pawn = 0
        if player[1] == me:
            pawn = 1
        ai = AI(map, pawn)
        return ai.run()

    @cherrypy.expose
    def ping(self):
        return "pong"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    else:
        port = PORT

    cherrypy.config.update({'server.socket_host': HOST, 'server.socket_port': port})
    cherrypy.quickstart(Server())

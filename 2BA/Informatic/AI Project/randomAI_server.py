import socket, os, json, transmitJSON, cherrypy, sys, copy
from random import randint

HOST = '0.0.0.0'
PORT = 8082
ROOT = os.path.abspath(os.getcwd())

'''map = [
		[[], [], [], [], [], [], [], [], []],
		[[], [], [], [], [], [], [0, 1], [], []],
		[[], [], [], [], [], [0, 0, 0, 1, 1], [], [], []],
		[[], [], [], [1], [], [1, 1], [], [], [0, 1]],
		[[], [], [1], [0, 0, 1], [], [0, 0, 0, 1], [1], [0, 0, 0, 1, 1], []],  
		[[], [1, 0, 0], [0], [1], [0], [1], [0], [], []],
		[[], [0, 1], [], [], [1, 1, 1, 0], [0], [1], [], []],
		[[], [1], [0, 0], [], [], [1, 1], [], [], []],
		[[], [], [], [], [], [0], [], [], []]
	]'''

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
        if player[0] == me :
            pawn = 0
        else :
            pawn = 1
        ai = AI(map, pawn)
        return ai.run()

    @cherrypy.expose
    def ping(self):
        return "pong"

class AI():
	def __init__(self, map, pawn):

		self.map = copy.deepcopy(map)
		self.pawn = pawn
		self.score = self.getScore(self.map)

	def show_map(self, position):
		for row in position:
			print(row)

	def run(self):	
		self.show_map(self.map)
		available_moves = self.availableMoves(self.map)
		random_pawn = randint(0, len(available_moves))
		random_direction = randint(0, len(available_moves[random_pawn][2])-1)
		x, y = available_moves[random_pawn][0], available_moves[random_pawn][1]
		direction = available_moves[random_pawn][2][random_direction]
		self.map, x2, y2 = self.move(x, y, direction, self.map)
		move = {"move": {"from": [x, y], "to": [x2, y2]}, "message": "I'm am the random AI !"}
		print("My move : ", move)
		self.show_map(self.map)
		return move

	def availableMoves(self, position):
		available_moves = []
		totalMove = 0
		available_pawns = self.availablePawns(position)
		for pawn in available_pawns:
			available_directions = self.checkDirections(pawn[0], pawn[1], position)
			if available_directions:
				available_moves.append(available_directions)
				totalMove += len(available_directions[2])
		#print("Total possible moves : ", totalMove)
		return available_moves
		
	def availablePawns(self, position):
		available_pawn = []
		for x in range(len(position)):
			for y in range(len(position)):
				if len(position[x][y]) > 0 and len(position[x][y]) < 5:
					available_pawn.append([x,y])
		return available_pawn

	def checkDirections(self, x, y, position):
		availableDirections = []
		for key, value in directions.items():                       				# Check if we move a pawn in a certain direction, the final position is possible. 
			if (x+value[0]) >= 0 and (y+value[1]) >= 0:             				# By checking first if were not out of bound.
				if (x+value[0]) <= 8 and (y+value[1]) <= 8:
					if len(position[x+value[0]][y+value[1]]) > 0 and len(position[x+value[0]][y+value[1]]) <= 5 :        			# And if the final position is not on an empty place or full place
						availableDirections.append(key)
		if len(availableDirections) != 0:
			return [x, y, availableDirections]
		else :
			return None

	def move(self, x1, y1, direction, position): 
		current_position = copy.deepcopy(position)									# Takes starting coordinate of the pawn and move it in the direction mentionned.		                      				
		for key, value in directions.items():
			if direction == key :
				x2 = x1+value[0]                                    				# Find the moving coordinates for the pawn.
				y2 = y1+value[1]
				
		for pawn in current_position[x1][y1]:                                		# Move the pawn to the new coordinate.
			current_position[x2][y2].append(pawn)

		current_position[x1][y1] = []
		return current_position, x2, y2                                         			# Remove previous location of the pawn.
	
	def getScore(self, positions):
		redScore = 0
		blackScore = 0
		for i in range(len(positions)):
			for j in range(len(positions)):
				if len(positions[i][j]) > 0:										# Check if there is a turret with minimum 1 pawn
					a = len(positions[i][j]) - 1									
					if positions[i][j][a] == 1 :									# Check if the last pawn is black 
						blackScore += 1 											
					else:															# Or red
						redScore += 1
		if self.pawn == 1:
			return blackScore-redScore												# Return black pawn score
		else :
			return redScore-blackScore

if __name__ == "__main__":
    if len(sys.argv) > 1:
        port=int(sys.argv[1])
    else:
        port=PORT

    cherrypy.config.update({'server.socket_host': HOST, 'server.socket_port': port})
    cherrypy.quickstart(Server())

'''ai = AI(map, 0)
move = ai.run()
print(move)'''
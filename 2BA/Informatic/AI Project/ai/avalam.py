import copy, cProfile, time, os
from random  import randint

map = [
		[ [],  [],  [], [0], [1],  [],  [],  [],  []],
		[ [],  [],  [], [1], [0], [1], [0], [1],  []],
		[ [],  [], [1], [0], [1], [0], [1], [0], [1]],
		[ [],  [], [0], [1], [0], [1], [0], [1], [0]],
		[ [], [0], [1], [0],  [], [0], [1], [0],  []],
		[[0], [1], [0], [1], [0], [1], [0],  [],  []],
		[[1], [0], [1], [0], [1], [0], [1],  [],  []],
		[ [], [1], [0], [1], [0], [1],  [],  [],  []],
		[ [],  [],  [],  [], [1], [0],  [],  [],  []]
	]

test1 = [
		[ [1], [],  [0]],
		[ [], [0], []],
		[ [1], [], []]
	]

test2 = [
		[ [], [0],  []],
		[ [], [0], []],
		[ [1], [1], []]
	]

directions = {'RIGHT': [0, 1], 'LEFT': [0, -1], 'UP': [-1, 0], 'DOWN': [1, 0], 
'UPRIGHT': [-1, 1], 'UPLEFT': [-1, -1], 'DOWNRIGHT': [1, 1], 'DOWNLEFT': [1, -1]}

BLACKPAWN = 1
REDPAWN = 0
AI_MODE = 1
RANDOM_MODE = 0
TIMEOUT = 1
ROOT = os.path.abspath(os.getcwd()) + "/2BA/Informatic/res/"

class MapPool():
    def __init__(self, position):
        self.size = 20
        self.pool = None

    def create(self, position):
        self.pool = {'free': [], 'busy': []}
        for i in range(self.size):
        	self.pool['free'].append(copy.deepcopy(position))

    def borrow(self, data):
        if not self.pool:
            self.create(data)
        if not self.pool['free']:
            return None
        else:
            pool_object = self.pool['free'].pop()
            self.pool['busy'].append(pool_object)
            return pool_object

    def give_back(self, pool_object):
        self.pool['busy'].remove(pool_object)
        self.pool['free'].append(pool_object)

class AI():
	def __init__(self, position, pawn):
		self.timeout = time.time() + TIMEOUT
		self.pawn = pawn
		self.position = position
		self.pool = MapPool(self.position)
		self.pool.create(self.position)

	def show_map(self, position):
		for row in position:
			print(row)

	def run(self):	
		for i in range(1, 10):
			print("depth : ", i)
			x1, y1, x2, y2 = self.best_move(self.position, 0, i, -1000, 1000)
			if time.time() < self.timeout:
				move = {"move": {"from": [x1, y1], "to": [x2, y2]}, "message": "I'm the alpha beta AI !"}
			else:
				break
		print("My move : ", move)
		return move

	def alpha_beta(self, position, current_depth, target_depth, alpha, beta, my_turn):
		if time.time() > self.timeout:
			return 0	
		possibleMoves = self.availableMoves(position)											
		if current_depth == target_depth or not possibleMoves:
			return self.getScore(position)
		else: 
			if my_turn:
				best_score = -1000
				for move in possibleMoves:
					x, y, = move[0], move[1]
					for direction in move[2]:
						max_copy_position = self.pool.borrow(position)
						new_map, _, _ = self.move(x, y, direction, max_copy_position)
						best_score = max(best_score, self.alpha_beta(new_map, current_depth+1, target_depth, alpha, beta, False))
						self.pool.give_back(max_copy_position)
						alpha = max(alpha, best_score)
					if alpha >= beta:
						break
				return best_score
			elif not my_turn:
				best_score = 1000
				for move in possibleMoves:
					x, y, = move[0], move[1]
					for direction in move[2]:
						min_copy_position = self.pool.borrow(position)
						new_map, _, _ = self.move(x, y, direction, min_copy_position)
						best_score = min(best_score, self.alpha_beta(new_map, current_depth+1, target_depth, alpha, beta, True))
						beta = min(beta, best_score)
						self.pool.give_back(min_copy_position)
					if alpha >= beta:
						break
				return best_score

	def best_move(self, position, current_depth, target_depth, alpha, beta):
		if time.time() > self.timeout:
			return 0	
		possibleMoves = self.availableMoves(position)												# Store all the possible moves
		if current_depth == target_depth or not possibleMoves:
			return self.getScore(position)
		else: 
			best_score = -1000
			for move in possibleMoves:
				x, y, = move[0], move[1]
				for direction in move[2]:
					new_map, x2, y2 = self.move(x, y, direction, position)
					new_score = self.alpha_beta(new_map, current_depth+1, target_depth, alpha, beta, False)
					if new_score > best_score:
						best_move = x, y, x2, y2
						best_score = new_score
			return best_move

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

	def checkDirections(self, x, y, position):																		# Check if we move a pawn in a certain direction, the final position is possible.  	
		availableDirections = []
		for key, value in directions.items():                       												# By checking first if were not out of bound.
			if (x+value[0]) >= 0 and (x+value[0]) <= 8 and (y+value[1]) >= 0 and (y+value[1]) <= 8:					# ATTENTION : change 2 by 8 after finishing testing
				if len(position[x+value[0]][y+value[1]]) > 0 and len(position[x+value[0]][y+value[1]]) + len(position[x][y]) < 5 :       # And if the final position is not on an empty place or full place
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
		return current_position, x2, y2                                       			# Remove previous location of the pawn.
	
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
			return  blackScore-redScore											# Return black pawn score
		else :
			return redScore-blackScore												# Return red pawn score

def update(x1, y1, x2, y2, position):
	while len(position[x1][y1]) > 0 :
		position[x2][y2].append(position[x1][y1][0])
		del position[x1][y1][0]
	return position

def unpack(move):
	coordinate = move["move"]
	start = coordinate["from"]
	end = coordinate["to"]
	x1 = start[0]
	y1 = start[1]
	x2 = end[0]
	y2 = end[1]
	move = (x1, y1, x2, y2)
	return move

def game():
	board = map
	running = True
	my_turn = True
	history = []
	while running:
		state_ai = AI(board, 1)
		state = len(state_ai.availableMoves(board))
		print("Available Move : ", state)
		if state != 0:
			if my_turn:
				print("BLACK TURN")
				ai = AI(board, BLACKPAWN)
				data = ai.run()
				x1, y1, x2, y2 = unpack(data)
				update(x1, y1, x2, y2, board)
				ai.show_map(board)
				del ai
				history.append([x1, y1, x2, y2])
				my_turn = False
			else:
				print("RED TURN")
				ai_bad = AI(board, REDPAWN)
				data = ai_bad.run()
				x1, y1, x2, y2 = unpack(data)
				update(x1, y1, x2, y2, board)
				ai_bad.show_map(board)
				del ai_bad
				history.append([x1, y1, x2, y2])
				my_turn = True
		else:
			ai = AI(board, BLACKPAWN)
			ai_bad = AI(board, REDPAWN)
			print("GAME OVER ! FINAL SCORE : ", ai.getScore(board), " FOR BLACK and ", ai_bad.getScore(board), " FOR RED")
			running = False

"""with open(ROOT + 'history.txt', 'w') as output_file:
	for move in history:
		output_file.writelines(str(move))"""

cProfile.run('game()')															# Allow to see time run for every function (for performance)

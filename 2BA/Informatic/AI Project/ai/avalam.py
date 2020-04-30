import copy, cProfile, time
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
TIMEOUT = 1000

class AI():
	def __init__(self, map, pawn):
		self.timeout = time.time() + 8
		self.map = copy.deepcopy(map)
		self.pawn = pawn
		self.score = self.getScore(self.map)

	def show_map(self, position):
		for row in position:
			print(row)
	
	def update(self, position):
		self.map = position

	def run(self):	
		for i in range(1, 10):
			print("depth : ", i)
			x1, y1, x2, y2 = self.best_move(self.map, 0, i, -1000, 1000)
			if time.time() < self.timeout:
				move = {"move": {"from": [x1, y1], "to": [x2, y2]}, "message": "I'm the alpha beta AI !"}
			else:
				break
		print("My move : ", move)
		return move

	def random(self):	
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
						new_map, _, _ = self.move(x, y, direction, position)
						best_score = max(best_score, self.alpha_beta(new_map, current_depth+1, target_depth, alpha, beta, False))
						alpha = max(alpha, best_score)
					if alpha >= beta:
						break
				return best_score
			elif not my_turn:
				best_score = 1000
				for move in possibleMoves:
					x, y, = move[0], move[1]
					for direction in move[2]:
						new_map, _, _ = self.move(x, y, direction, position)
						best_score = min(best_score, self.alpha_beta(new_map, current_depth+1, target_depth, alpha, beta, True))
						beta = min(beta, best_score)
					if alpha >= beta:
						break
				return best_score
					
	def minimax(self, current_depth, target_depth, position, my_turn):
		possibleMoves = self.availableMoves(position)												# Store all the possible moves
		if current_depth == target_depth or not possibleMoves:
			return self.getScore(position)
		else : 
			if my_turn:																					# AI's turn
				best_score = -1000																		# Set the score to the worst possible (-infinite), -1000 is sufficient here
				for move in possibleMoves:
					x, y = move[0], move[1]	
					for direction in move[2]:										
						new_map, _, _ = self.move(x, y, direction, position)									# Check for every possible moves and update the map
						new_score = self.minimax(current_depth+1, target_depth, new_map, False)			# Use recursive function to build the tree 
						best_score = max(best_score, new_score)											# The AI is the maximizing player, it has to take the best score
				return best_score
			elif not my_turn:																			# Opponent's turn
				best_score = 1000																		# Set the score to the best possible (+infinite), 1000 is sufficient here
				for move in possibleMoves:
					x, y = move[0], move[1]	
					for direction in move[2]:
						new_map, _, _ = self.move(x, y, direction, position)									# Check for every possible moves and update the map
						new_score = self.minimax(current_depth+1, target_depth, new_map, True)			# Use recursive function to build the tree
						best_score = min(best_score, new_score)											# The opponent is the minmimazing player, it has to take the worst score
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
		
	def best_move_1(self, position, current_depth, target_depth):
		possibleMoves = self.availableMoves(position)
		count = 1
		if current_depth == target_depth or not possibleMoves:
			return self.getScore(position)
		else : 
			best_move = None 
			best_score = -1000
			for move in possibleMoves:
				x, y = move[0], move[1]
				for direction in move[2]: 
					#print("move : ", count, "/24 ", x, y, direction)		
					new_map, _, _ = self.move(x, y, direction, position)
					count += 1
					new_score = self.minimax(current_depth+1, target_depth, new_map, False)
					if new_score > best_score:
						best_move = x, y, direction
						best_score = new_score
			return best_move, best_score

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
				if len(position[x+value[0]][y+value[1]]) > 0 and len(position[x+value[0]][y+value[1]]) <= 5 :       # And if the final position is not on an empty place or full place
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

def update(x1, y1, x2, y2):
	map[x2][y2].append(map[x1][y1][0])
	del map[x1][y1][0]
	return map

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

running = True
my_turn = True
ai = AI(map, BLACKPAWN)
ai_bad = AI(map, REDPAWN)

while running:
	state = len(ai.availableMoves(map))
	if state != 0:
		if my_turn:
			print("BLACK TURN")
			ai.update(map)
			data = ai.run()
			data = ai.run()
			x1, y1, x2, y2 = unpack(data)
			update(x1, y1, x2, y2)
			ai.show_map(map)
			my_turn = False
		else:
			print("RED TURN")
			ai.update(map)
			ai_bad.run()
			data = ai.run()
			x1, y1, x2, y2 = unpack(data)
			update(x1, y1, x2, y2)
			ai.show_map(map)
			my_turn = True
		data = ai.run()

	else:
		print("GAME OVER ! FINAL SCORE : ", ai.getScore(map), " FOR BLACK and ", ai_bad.getScore(map), " FOR RED")
		running = False

#cProfile.run('ai.run()')															# Allow to see time run for every function (for performance)
class MiniMax():
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
			return best_move
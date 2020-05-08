import copy, time
from random import randint

TIMEOUT = 2
directions = {'RIGHT': [0, 1], 'LEFT': [0, -1], 'UP': [-1, 0], 'DOWN': [1, 0], 'UPRIGHT': [-1, 1], 'UPLEFT': [-1, -1],
              'DOWNRIGHT': [1, 1], 'DOWNLEFT': [1, -1]}

class AI():
    def __init__(self, position, pawn):
        self.timeout = time.time() + TIMEOUT
        self.pawn = pawn
        self.position = position
        self.pool = MapPool(self.position)
        self.pool.create(self.position)

    def run(self):	
		available_moves = self.availableMoves(self.map)
		random_pawn = randint(0, len(available_moves))
		random_direction = randint(0, len(available_moves[random_pawn][2])-1)
		x, y = available_moves[random_pawn][0], available_moves[random_pawn][1]
		direction = available_moves[random_pawn][2][random_direction]
		self.map, x2, y2 = self.move(x, y, direction, self.map)
		move = {"move": {"from": [x, y], "to": [x2, y2]}, "message": "I'm am the random AI !"}
		return move

    def availableMoves(self, position):
        available_moves = []
        available_pawns = self.availablePawns(position)
        for pawn in available_pawns:
            available_directions = self.checkDirections(pawn[0], pawn[1], position)
            if available_directions:
                available_moves.append(available_directions)
        return available_moves

    def availablePawns(self, position):
        available_pawn = []
        for x in range(len(position)):
            for y in range(len(position)):
                if 0 < len(position[x][y]) < 5:
                    available_pawn.append([x, y])
        return available_pawn

    def checkDirections(self, x, y, position):  # Check if we move a pawn in a certain direction, the final position is possible.
        availableDirections = []
        for key, value in directions.items():  # By checking first if were not out of bound.
            if 0 <= (x + value[0]) <= 8 and 0 <= (y + value[1]) <= 8: 
                if len(position[x + value[0]][y + value[1]]) > 0 and len(position[x + value[0]][y + value[1]]) + len(position[x][y]) <= 5:  # And if the final position is not on an empty place or full place
                    availableDirections.append(key)
        if len(availableDirections) != 0:
            return [x, y, availableDirections]
        else:
            return None

    def move(self, x1, y1, direction, position):  # Takes starting coordinate of the pawn and move it in the direction mentionned.
        for key, value in directions.items():
            if direction == key:
                x2 = x1 + value[0]  # Find the moving coordinates for the pawn.
                y2 = y1 + value[1]
        for pawn in position[x1][y1]:  # Move the pawn to the new coordinate.
            position[x2][y2].append(pawn)
        position[x1][y1] = []
        return position, x2, y2  # Remove previous location of the pawn.

    def getScore(self, positions):
        redScore = 0
        blackScore = 0
        for i in range(len(positions)):
            for j in range(len(positions)):
                if len(positions[i][j]) > 0:  # Check if there is a turret with minimum 1 pawn
                    a = len(positions[i][j]) - 1
                    if positions[i][j][a] == 1:  # Check if the last pawn is black
                        blackScore += 1
                    else:  # Or red
                        redScore += 1
        if self.pawn == 1:
            return blackScore - redScore  # Return black pawn score
        else:
            return redScore - blackScore  # Return red pawn score
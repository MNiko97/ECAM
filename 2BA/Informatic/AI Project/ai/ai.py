import copy, time
from random import randint
from .map_pool import MapPool

TIMEOUT = 2
directions = {'RIGHT': [0, 1], 'LEFT': [0, -1], 'UP': [-1, 0], 'DOWN': [1, 0], 'UPRIGHT': [-1, 1], 'UPLEFT': [-1, -1],
              'DOWNRIGHT': [1, 1], 'DOWNLEFT': [1, -1]}

class AI(MapPool):
    def __init__(self, position, pawn):
        self.timeout = time.time() + TIMEOUT
        self.pawn = pawn
        self.position = position
        self.pool = MapPool(self.position)
        self.pool.create(self.position)

    def run(self):
        for i in range(1, 10):
            print("depth :", i)
            if time.time() < self.timeout:
                res = self.best_move(self.position, 0, i, -1000, 1000)
                print("result :", res)
                x1, y1, x2, y2 = res
                move = {"move": {"from": [x1, y1], "to": [x2, y2]}, "message": "I'm the alpha beta AI !"}
            else:
                break
        print("My move :", move)
        return move

    def alpha_beta(self, position, current_depth, target_depth, alpha, beta, my_turn):
        if time.time() > self.timeout:
            return 0
        possibleMoves = self.availableMoves(position)
        if current_depth == target_depth or not possibleMoves:
            score = self.getScore(position)
            return score
        else:
            if my_turn:
                best_score = -1000
                for move in possibleMoves:
                    x, y, = move[0], move[1]
                    for direction in move[2]:
                        max_map = self.pool.borrow(position)
                        new_map, _, _ = self.move(x, y, direction, max_map)
                        best_score = max(best_score,
                                         self.alpha_beta(new_map, current_depth + 1, target_depth, alpha, beta, False))
                        self.pool.give_back(max_map)
                        alpha = max(alpha, best_score)
                        if alpha >= beta:
                            break
                    if alpha >= beta:
                        break
                return best_score
            elif not my_turn:
                best_score = 1000
                for move in possibleMoves:
                    x, y, = move[0], move[1]
                    for direction in move[2]:
                        min_map = self.pool.borrow(position)
                        new_map, _, _ = self.move(x, y, direction, min_map)
                        best_score = min(best_score,
                                         self.alpha_beta(new_map, current_depth + 1, target_depth, alpha, beta, True))
                        self.pool.give_back(min_map)
                        beta = min(beta, best_score)
                        if alpha >= beta:
                            break
                    if alpha >= beta:
                        break
                return best_score

    def best_move(self, position, current_depth, target_depth, alpha, beta):
        if time.time() > self.timeout:
            return 0
        possibleMoves = self.availableMoves(position)  # Store all the possible moves
        if current_depth == target_depth or not possibleMoves:
            return self.getScore(position)
        else:
            best_score = -1000
            for move in possibleMoves:
                x, y, = move[0], move[1]
                for direction in move[2]:
                    max_map = self.pool.borrow(position)
                    new_map, x2, y2 = self.move(x, y, direction, max_map)
                    new_score = self.alpha_beta(new_map, current_depth + 1, target_depth, alpha, beta, False)
                    self.pool.give_back(max_map)
                    if new_score > best_score:
                        best_move = x, y, x2, y2
                        best_score = new_score
            return best_move

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
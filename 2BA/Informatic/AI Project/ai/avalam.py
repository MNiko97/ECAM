import copy, cProfile, time, os
from random import randint
from map_pool import MapPool

map = [
    [[], [], [], [0], [1], [], [], [], []],
    [[], [], [], [1], [0], [1], [0], [1], []],
    [[], [], [1], [0], [1], [0], [1], [0], [1]],
    [[], [], [0], [1], [0], [1], [0], [1], [0]],
    [[], [0], [1], [0], [], [0], [1], [0], []],
    [[0], [1], [0], [1], [0], [1], [0], [], []],
    [[1], [0], [1], [0], [1], [0], [1], [], []],
    [[], [1], [0], [1], [0], [1], [], [], []],
    [[], [], [], [], [1], [0], [], [], []]
]

test1 = [
    [[1], [], [0]],
    [[], [0], []],
    [[1], [], []]
]

test2 = [
    [[], [0], []],
    [[], [0], []],
    [[1], [1], []]
]

test3 = [
    [[1], [0], [1]],
    [[0], [1], [0]],
    [[1], [0], [1]]
]

directions = {'RIGHT': [0, 1], 'LEFT': [0, -1], 'UP': [-1, 0], 'DOWN': [1, 0], 'UPRIGHT': [-1, 1], 'UPLEFT': [-1, -1],
              'DOWNRIGHT': [1, 1], 'DOWNLEFT': [1, -1]}

BLACKPAWN = 1
REDPAWN = 0
TIMEOUT = 2
SIZE = 8
ROOT = os.path.abspath(os.getcwd()) + "/2BA/Informatic/res/"


class AI(MapPool):
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
            if 0 <= (x + value[0]) <= SIZE and 0 <= (
                    y + value[1]) <= SIZE:  # ATTENTION : change 2 by 8 after finishing testing
                if len(position[x + value[0]][y + value[1]]) > 0 and len(position[x + value[0]][y + value[1]]) + len(
                        position[x][y]) < 5:  # And if the final position is not on an empty place or full place
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


class AItest:
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
            if 0 <= (x + value[0]) <= SIZE and 0 <= (
                    y + value[1]) <= SIZE:  # ATTENTION : change 2 by 8 after finishing testing
                if len(position[x + value[0]][y + value[1]]) > 0 and len(position[x + value[0]][y + value[1]]) + len(
                        position[x][y]) <= 5:  # And if the final position is not on an empty place or full place
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

    def checkcompo(self, turret, pawn):
        red = 0
        black = 0
        for i in range(len(turret)):
            if turret[i] == 0:
                red += 1
            else:
                black += 1
        if pawn == 'black':
            if black == 0:
                return 4.0
            return red/black
        else:
            if red == 0:
                return 4.00
            return black/red

    def getScore(self, positions):
        blackscore = 0
        redscore = 0
        for i in range(len(positions)):
            for j in range(len(positions)):
                turret = positions[i][j]
                if len(turret) > 0:  # Check if there is a turret with minimum 1 pawn
                    size = len(positions[i][j])
                    lastpawn = size - 1
                    if turret[lastpawn] == BLACKPAWN and not self.checkEnnemy(positions, i, j):
                        blackscore += 1
                    if turret[lastpawn] == REDPAWN and not self.checkEnnemy(positions, i, j):
                        redscore += 1
        if self.pawn == 1:
            return blackscore-redscore
        else:
            return redscore-blackscore

    def checkEnnemy(self, position, x, y):
        for key, value in directions.items():  # By checking first if were not out of bound.
            if 0 <= (x + value[0]) <= SIZE and 0 <= (y + value[1]) <= SIZE:
                if len(position[x + value[0]][y + value[1]]) > 0 and len(position[x + value[0]][y + value[1]]) + len(position[x][y]) <= 5:  # And if the final position is not on an empty place or full place
                    return True
        return False

    def oldScore(self, positions):
        blackturret = {'1': [0], '2': [0], '3': [0], '4': [0], '5': [0]}
        redturret = {'1': [0], '2': [0], '3': [0], '4': [0], '5': [0]}
        blackRatio = []
        redRatio = []
        for i in range(len(positions)):
            for j in range(len(positions)):
                if len(positions[i][j]) > 0:  # Check if there is a turret with minimum 1 pawn
                    size = len(positions[i][j])
                    lastpawn = size - 1
                    turret = positions[i][j]
                    if turret[lastpawn] == 1:                               # Check if the last pawn is BLACK
                        blackRatio.append(self.checkcompo(turret, "black"))
                        if size == 1:
                            blackturret['1'][0] += 1
                        if size == 2:
                            blackturret['2'][0] += 1
                        if size == 3:
                            blackturret['3'][0] += 1
                        if size == 4:
                            blackturret['4'][0] += 1
                        if size == 5:
                            blackturret['5'][0] += 1
                    else:                                                   # Or if the pawn is RED
                        redRatio.append(self.checkcompo(turret, "red"))
                        if size == 1:
                            redturret['1'][0] += 1
                        if size == 2:
                            redturret['2'][0] += 1
                        if size == 3:
                            redturret['3'][0] += 1
                        if size == 4:
                            redturret['4'][0] += 1
                        if size == 5:
                            redturret['5'][0] += 1
        blackScore = 0
        redScore = 0
        ratioB = 0
        ratioR = 0
        #print(blackturret)
        #print(redturret)
        for key, value in blackturret.items():
            blackScore += value[0]
            redScore += redturret.get(key)[0]
        for ratio in blackRatio:
            ratioB += ratio
        for ratio in redRatio:
            ratioR += ratio
        #print(blackRatio, redRatio)
        black = ratioB/len(blackRatio)
        red = ratioR/len(redRatio)
        if self.pawn == 1:
            return (blackScore/(redScore+blackScore))*black # Return black pawn score
        else:
            return (redScore/(redScore+blackScore))*red  # Return red pawn score


def update(x1, y1, x2, y2, position):
    while len(position[x1][y1]) > 0:
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


def game(board):
    running = True
    my_turn = False
    history = []
    while running:
        state_ai = AI(board, 1)
        state = len(state_ai.availableMoves(board))
        print("Available Move : ", state)
        if state != 0:
            if my_turn:
                print("BLACK TURN")
                ai = AItest(board, BLACKPAWN)
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
            print("GAME OVER ! FINAL SCORE : ", ai.getScore(board), " FOR BLACK and ", ai_bad.getScore(board),
                  " FOR RED")
            running = False


test4 = [
    [[1, 0], [0, 1, 1], [1]],
    [[0], [1], [0, 1, 0]],
    [[1], [0, 1, 1, 0, 1], [1, 0, 1, 1, 1]]
]

game(map)
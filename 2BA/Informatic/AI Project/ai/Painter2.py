import tkinter as tk
from src.avalam6 import AI #modifier ici, et retirer le call game() dans ai
import time

BLACKPAWN = 1
REDPAWN = 0

directions = {'RIGHT': [0, 1], 'LEFT': [0, -1], 'UP': [-1, 0], 'DOWN': [1, 0], 'UPRIGHT': [-1, 1], 'UPLEFT': [-1, -1],
              'DOWNRIGHT': [1, 1], 'DOWNLEFT': [1, -1]}

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

canvas = None
block_size = 80
choose1 = True
choose2 = False
my_turn = True
board = None
root = None

move1 = None
move2 = None

lastMove1 = None
lastMove2 = None

def init(boardmap):
    global canvas
    global root
    global board


    board = boardmap
    root = tk.Tk()

    canvas = tk.Canvas(master=root, width=len(board) * block_size * 2, height=len(board) * block_size)
    canvas.bind("<Button-1>", on_click)
    canvas.grid(row=0, column=0)
    draw_map(canvas, board)

    root.mainloop()

def run_game():
    global choose1
    global move1
    global move2
    global my_turn
    global lastMove1
    global lastMove2
    history = []
    draw_map(canvas, board)
    state_ai = AI(board, 1)
    state = len(state_ai.availableMoves(board))
    del state_ai
    if state != 0:
        x1, y1 = move1
        x2, y2 = move2
        lastMove1 = move1
        lastMove2 = move2
        move1 = None
        move2 = None
        update(x1, y1, x2, y2, board)
        history.append([x1, y1, x2, y2])
        my_turn = False
        draw_map(canvas, board)
        root.update_idletasks()
        print("RED TURN")
        ai_bad = AI(board, REDPAWN)
        data = ai_bad.run()
        x1, y1, x2, y2 = unpack(data)
        lastMove1 = x1, y1
        lastMove2 = x2, y2
        show_pc_move(x1, y1, x2, y2)
        update(x1, y1, x2, y2, board)
        del ai_bad
        history.append([x1, y1, x2, y2])
        my_turn = True
        draw_map(canvas, board)
    else:
        ai = AI(board, BLACKPAWN)
        ai_bad = AI(board, REDPAWN)
        print("GAME OVER ! FINAL SCORE : ", ai.getScore(board), " FOR BLACK and ", ai_bad.getScore(board),
              " FOR RED")

def show_pc_move(x1, y1, x2, y2):
    x, y = x1, y2
    canvas.create_rectangle((x * block_size, y * block_size, (x + 1) * block_size, (y + 1) * block_size),
                            outline='red')

    time.sleep(0.3)

    x, y = x2, y2
    canvas.create_rectangle((x * block_size, y * block_size, (x + 1) * block_size, (y + 1) * block_size),
                            outline='green')

    time.sleep(0.3)

def draw_map(canvas, board):
    for x in range(len(board)):
        for y in range(len(board)):
            canvas.create_rectangle((x * block_size, y * block_size, (x + 1) * block_size, (y + 1) * block_size),
                                    fill='white')
            offset = 0
            for pion in board[x][y]:
                mini_block_size=50
                color = None
                if pion == 1:
                    color = "black"
                else:
                    color = "yellow"
                canvas.create_rectangle((x * block_size + offset, y * block_size + offset, x * block_size + mini_block_size + offset, y * block_size + mini_block_size + offset),
                                        fill=color, outline="blue")
                offset += block_size/7

    if lastMove1:
        x, y = lastMove1
        canvas.create_rectangle((x * block_size, y * block_size, (x + 1) * block_size, (y + 1) * block_size),
                                outline='red')

    if lastMove2:
        x, y = lastMove2
        canvas.create_rectangle((x * block_size, y * block_size, (x + 1) * block_size, (y + 1) * block_size),
                                outline='green')



def on_click(event):
    global choose1
    global choose2
    global move1
    global move2
    x = int(event.x/block_size)
    y = int(event.y/block_size)
    if choose1:
        choose1 = False
        choose2 = True
        move1 = x, y
        canvas.create_rectangle((x * block_size, y * block_size, (x + 1) * block_size, (y + 1) * block_size),
                                fill='red')

    elif choose2:
        choose2 = False
        choose1 = True
        move2 = x, y
        canvas.create_rectangle((x * block_size, y * block_size, (x + 1) * block_size, (y + 1) * block_size),
                                fill='blue')
        run_game()

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

def update(x1, y1, x2, y2, position):
    while len(position[x1][y1]) > 0:
        position[x2][y2].append(position[x1][y1][0])
        del position[x1][y1][0]
    return position




init(map)
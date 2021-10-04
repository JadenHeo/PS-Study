### 08:17 시작
from collections import deque
N = int(input())
green, blue = [[0]*4 for _ in range(6)], [[0]*4 for _ in range(6)]
G, B = 0, 1
SCORE = 0
def print_board(color):
    if color == G:
        for row in range(6):
            for col in range(4):
                print(green[row][col], end=' ')
            print()
    else:
        for col in range(4):
            for row in range(6):
                print(blue[row][col], end=' ')
            print()
    print()

def put_block(color, t, col):
    board = green if color == G else blue
    if t == 1:
        now_row = 2
        while True:
            if now_row >= 6 or board[now_row][col] != 0:
                board[now_row-1][col] = 1
                break
            now_row += 1
    elif t == 2:
        now_row = 2
        while True:
            if now_row >= 6 or board[now_row][col] != 0 or board[now_row][col+1]:
                board[now_row-1][col], board[now_row-1][col+1] = 1, 1
                break
            now_row += 1
    else:
        now_row = 2
        while True:
            if now_row >= 6 or board[now_row][col] != 0:
                board[now_row-2][col], board[now_row-1][col] = 1, 1
                break
            now_row += 1

def delete_line(color):
    global SCORE, green, blue
    board = green if color == G else blue
    bingo = []
    for row in range(5, 1, -1):
        if sum(board[row]) == 4:
            bingo.append(row)
    SCORE += len(bingo)
    new_board = []
    for _ in range(len(bingo)):
        new_board.append([0,0,0,0])
    for row in range(6):
        if row not in bingo:
            new_board.append(board[row])
    if color == G:
        green = new_board
    else:
        blue = new_board

def delete_line2(color):
    board = green if color == G else blue
    cnt = 0
    for row in range(2):
        if sum(board[row]):
            cnt += 1
    for _ in range(cnt):
        board.pop()
        board.insert(0, [0, 0, 0, 0])

for _ in range(N):
    t, row, col = map(int, input().split())
    if t == 1:
        put_block(G, t, col)
        put_block(B, t, row)
    elif t == 2:
        put_block(G, t, col)
        put_block(B, 3, row)
    elif t == 3:
        put_block(G, t, col)
        put_block(B, 2, row)
    delete_line(G)
    delete_line(B)
    delete_line2(G)
    delete_line2(B)

    # print_board(G)
    # print_board(B)

print(SCORE)
SUM = 0
for row in range(2, 6):
    SUM += sum(green[row])
    SUM += sum(blue[row])
print(SUM)
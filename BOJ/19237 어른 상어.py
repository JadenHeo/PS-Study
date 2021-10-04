N, M, k = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))
sharks_dir = [0]
sharks_dir.extend(list(map(int, input().split())))
sharks_priority = [0]
for _ in range(M):
    p = [0]
    for i in range(4):
        p.append(tuple(map(int, input().split())))
    sharks_priority.append(p)
DIRECTION = [0, (-1, 0), (1, 0), (0, -1), (0, 1)]
ROW, COL = 0, 1
ARROW = [0, '↑', '↓', '←', '→']
SHARK, DIR, SMELL, REMAIN = 0, 1, 2, 3
for row in range(N):
    for col in range(N):
        if board[row][col] == 0:
            board[row][col] = [0, 0, 0, 0]
        else:
            shark = board[row][col]
            board[row][col] = [shark, sharks_dir[shark], shark, k]

def print_board(matrix):
    for row in matrix:
        for square in row:
            if square[SHARK]:
                print('SH'+str(square[SHARK])+ARROW[square[DIR]], square[SMELL], square[REMAIN], end=' '*4)
            else:
                print(square[SMELL], square[REMAIN], end=' '*9)
        print()
    print()

# print_board(board)

def move_shark(matrix):
    sharks_list = []
    for row in range(N):
        for col in range(N):
            if matrix[row][col][SHARK]:
                sharks_list.append((matrix[row][col][SHARK], matrix[row][col][DIR], row, col))
    # print(sharks_list)
    moved_sharks_list = []
    for shark in sharks_list:
        shark_num, now_dir, now_row, now_col = shark
        found = False
        for dir in sharks_priority[shark_num][now_dir]:
            next_row, next_col = now_row + DIRECTION[dir][ROW], now_col + DIRECTION[dir][COL]
            if 0 <= next_row < N and 0 <= next_col < N and matrix[next_row][next_col][SMELL] == 0:
                found = True
                break
        if not found:
            for dir in sharks_priority[shark_num][now_dir]:
                next_row, next_col = now_row + DIRECTION[dir][ROW], now_col + DIRECTION[dir][COL]
                if 0 <= next_row < N and 0 <= next_col < N and matrix[next_row][next_col][SMELL] == shark_num:
                    break
        moved_sharks_list.append((shark_num, dir, next_row, next_col))
        # print('SH'+str(shark_num)+ARROW[dir], next_row, next_col)
    
    for prev, shark in zip(sorted(sharks_list, reverse=True), sorted(moved_sharks_list, reverse=True)):
        _, _, prev_row, prev_col = prev
        shark_num, dir, row, col = shark
        matrix[prev_row][prev_col][SHARK], matrix[prev_row][prev_col][DIR] = 0, 0
        matrix[row][col] = [shark_num, dir, shark_num, k]
    
    # print_board(matrix)

    for row in range(N):
        for col in range(N):
            if not matrix[row][col][SHARK] and matrix[row][col][REMAIN] > 1:
                matrix[row][col][REMAIN] -= 1
            elif not matrix[row][col][SHARK] and matrix[row][col][REMAIN] == 1:
                matrix[row][col][SMELL], matrix[row][col][REMAIN] = 0, 0
    # print_board(matrix)

def check(matrix):
    cnt = 0
    for row in range(N):
        for col in range(N):
            if matrix[row][col][SHARK]:
                cnt += 1
    return cnt

i, cnt = 0, check(board)
while cnt > 1:
    i += 1
    if i > 1000:
        break
    # print('==========', i, '단계==========')
    move_shark(board)
    cnt = check(board)
if cnt == 1:
    print(i)
else:
    print(-1)
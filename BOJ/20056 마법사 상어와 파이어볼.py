N, M, K = map(int, input().split())
fireballs = []
for _ in range(M):
    fireballs.append(list(map(int, input().split())))

DIR = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

def balls_to_board(fireballs):
    board = [[[] for _ in range(N)] for _ in range(N)]
    for fireball in fireballs:
        r, c, m, s, d = fireball
        board[r][c].append((m, s, d))
    return board

def move(fireballs):
    moved_fireballs = []
    for fireball in fireballs:
        r, c, m, s, d = fireball
        moved_r, moved_c = (r + DIR[d][0] * s) % N, (c + DIR[d][1] * s) % N
        moved_fireballs.append((moved_r, moved_c, m, s, d))
    return moved_fireballs

def sum_and_split(board):
    for row in range(N):
        for col in range(N):
            if len(board[row][col]) >= 2:
                splited_balls = []
                sum_m, sum_s, prev_d= 0, 0, board[row][col][0][2] % 2
                odd_even = True
                for ball in board[row][col]:
                    m, s, d = ball
                    sum_m += m
                    sum_s += s
                    if d % 2 != prev_d:
                        odd_even = False
                new_m, new_s = sum_m // 5, sum_s // len(board[row][col])
                if new_m == 0:
                    board[row][col] = []
                    continue
                if odd_even:
                    for d in [0, 2, 4, 6]:
                        splited_balls.append((new_m, new_s, d))
                else:
                    for d in [1, 3, 5, 7]:
                        splited_balls.append((new_m, new_s, d))
                board[row][col] = splited_balls


for fireball in fireballs:
    fireball[0] -= 1
    fireball[1] -= 1
board = balls_to_board(fireballs)

for _ in range(K):
    board = balls_to_board(move(fireballs))
    sum_and_split(board)
    fireballs = []
    for row in range(N):
        for col in range(N):
            for ball in board[row][col]:
                m, s, d = ball
                fireballs.append((row, col, m, s, d))

total_mass = 0
for row in range(N):
    for col in range(N):
        if board[row][col]:
            for ball in board[row][col]:
                total_mass += ball[0]
print(total_mass)
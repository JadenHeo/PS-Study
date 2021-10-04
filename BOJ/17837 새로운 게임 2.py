ARROW = ['→', '←', '↑', '↓']
DIR = [(0, 1), (0, -1), (-1, 0), (1, 0)]
N, K = map(int, input().split())
board = []
for _ in range(N):
    board.append(tuple(map(int, input().split())))
horses = [[[] for _ in range(N)] for _ in range(N)]
horse_dict = {}
for idx in range(1, K+1):
    row, col, dir = map(int, input().split())
    horses[row-1][col-1] = [[idx, dir-1]]
    horse_dict[idx] = (row-1, col-1, 0, dir-1)

def print_board():
    print()
    for row in range(N):
        for col in range(N):
            if horses[row][col]:
                for horse in horses[row][col]:
                    print(str(horse[0])+ARROW[horse[1]], end='')
                print(end='\t')
            else:
                print(0, end='\t')
        print()

# print_board()

def check():
    max_height = 0
    for row in range(N):
        for col in range(N):
            if horses[row][col]:
                max_height = max(max_height, len(horses[row][col]))
    return max_height

TURN = 0
max_height = check()
while TURN < 1000 and max_height < 4:
    # print('==========TURN', TURN+1, '==========')
    for idx in range(1, K+1):
        # print_board()
        row, col, level, dir = horse_dict[idx]
        next_row, next_col = row + DIR[dir][0], col + DIR[dir][1]
        if not (0 <= next_row < N and 0 <= next_col < N) or board[next_row][next_col] == 2:
            if dir % 2 == 0:
                dir += 1
            else:
                dir -= 1
            horse_dict[idx] = (row, col, level, dir)
            horses[row][col][level][1] = dir
        next_row, next_col = row + DIR[dir][0], col + DIR[dir][1]
        if not (0 <= next_row < N and 0 <= next_col < N) or board[next_row][next_col] == 2:
            continue
        move = horses[row][col][level:]
        horses[row][col] = horses[row][col][:level]
        if board[next_row][next_col] == 0:
            for idx, d in move:
                _, _, prev_level, _ = horse_dict[idx]
                horse_dict[idx] = (next_row, next_col, prev_level - level + len(horses[next_row][next_col]), d)
            horses[next_row][next_col].extend(move)
        else:
            height = len(move)
            for idx, d in move:
                _, _, prev_level, _ = horse_dict[idx]
                horse_dict[idx] = (next_row, next_col, level + height - 1 - prev_level + len(horses[next_row][next_col]), d)
            horses[next_row][next_col].extend(move[::-1])
        if len(horses[next_row][next_col]) >= 4:
            break
    TURN += 1
    max_height = check()

# print_board()

if max_height >= 4:
    print(TURN)
else:
    print(-1)
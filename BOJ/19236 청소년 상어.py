from copy import deepcopy

DIRECTION = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]
board = []
for _ in range(4):
    infos = list(map(int, input().split()))
    fishes, directions = [], []
    for idx, info in enumerate(infos):
        if idx % 2 == 0:
            fishes.append(info)
        else:
            directions.append(info)
    line = []
    for fish, direction in zip(fishes, directions):
        line.append([fish, direction-1])
    board.append(line)

SHARK = 0
FISH, LOC, DIR = 0, 0, 1
fish_location = [False for _ in range(17)]
for row in range(4):
    for col in range(4):
        fish_location[board[row][col][FISH]] = [[row, col], board[row][col][DIR]]

def print_board(board):
    arrow = ['↑', '↖', '←', '↙', '↓', '↘', '→', '↗']
    for row in range(4):
        for col in range(4):
            temp = board[row][col]
            if not temp:
                p = 'Empty'
            elif temp[FISH] == 0:
                p = 'SHARK' + arrow[temp[DIR]]
            else:
                p = str(temp[FISH]) + arrow[temp[DIR]]
            print(p, end='\t')
        print()
    print()
            
def fish_move(board, fish_location):
    for idx in range(1, 17):
        if not fish_location[idx]:
            continue
        row, col = fish_location[idx][LOC]
        dir = fish_location[idx][DIR]
        rotation_cnt = 0
        _row, _col = row + DIRECTION[dir][0], col + DIRECTION[dir][1]
        while not (0 <= _row < 4 and 0 <= _col < 4 and (not board[_row][_col] or board[_row][_col][FISH] != SHARK)) and rotation_cnt < 8:
            dir = (dir + 1) % 8
            _row, _col = row + DIRECTION[dir][0], col + DIRECTION[dir][1]
            rotation_cnt += 1
        if 0 <= _row < 4 and 0 <= _col < 4 and (not board[_row][_col] or board[_row][_col][FISH] != SHARK):
            board[row][col][DIR] = dir
            temp = board[_row][_col]
            board[_row][_col] = board[row][col]
            board[row][col] = temp
            fish_location[idx] = [[_row, _col], dir]
            if temp:
                fish_location[temp[FISH]] = [[row, col], temp[DIR]]
    # print(fish_location)
    # print_board()
    return board, fish_location

def shark_move(target_fish, board, fish_location):
    target_row, target_col, target_dir = fish_location[target_fish][LOC][0], fish_location[target_fish][LOC][1], fish_location[target_fish][DIR]
    if fish_location[SHARK]:
        board[fish_location[SHARK][LOC][0]][fish_location[SHARK][LOC][1]] = False
    fish_location[SHARK] = [[target_row, target_col], target_dir]
    fish_location[target_fish] = False
    board[target_row][target_col] = [SHARK, target_dir]
    return board, fish_location

def fish_candidates(shark, board):
    row, col = shark[LOC]
    dir = shark[DIR]
    candidates = []
    _row, _col = row, col
    while 0 <= _row < 4 and 0 <= _col < 4:
        if board[_row][_col] and board[_row][_col][FISH] != SHARK:
            candidates.append(board[_row][_col][FISH])
        _row, _col = _row + DIRECTION[dir][0], _col + DIRECTION[dir][1]
    return candidates

SCORE = []
RECORD = []

def back_tracking(record, score, board, fish_location):
    # print(score, record)
    shark = fish_location[SHARK]
    if not fish_candidates(shark, board):
        SCORE.append(score)
        RECORD.append(record)
        # print(SCORE, RECORD)
        return 0
    for fish in fish_candidates(shark, board):
        copy_record, copy_score = record[:], score
        copy_board, copy_fish_location = deepcopy(board), deepcopy(fish_location)
        copy_board, copy_fish_location = shark_move(fish, copy_board, copy_fish_location)
        # print(copy_fish_location)
        # print_board(copy_board)
        copy_board, copy_fish_location = fish_move(copy_board, copy_fish_location)
        copy_record.append(fish)
        copy_score += fish

        back_tracking(copy_record, copy_score, copy_board, copy_fish_location)


# 처음 상어 진입
record, score = [board[0][0][FISH]], board[0][0][FISH]
board, fish_location = shark_move(board[0][0][FISH], board, fish_location)
board, fish_location = fish_move(board, fish_location)
back_tracking(record, score, board, fish_location)
print(sorted(SCORE, reverse=True)[0])
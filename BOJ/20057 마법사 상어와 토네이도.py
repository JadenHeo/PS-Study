N = int(input())
sand = []
for _ in range(N):
    sand.append(list(map(int, input().split())))
middle = ((N//2), (N//2))
ROTATION = [(0, 1), (1, 0), (0, -1), (-1, 0)]
r = 0
order = [0] * (N**2)
order[0] = (middle[0], middle[0], 2)
now, board = (0, 0), [[0] * N for _ in range(N)]
for idx in range(N**2-1, 0, -1):
    row, col = now
    order[idx] = (row, col, (r+2) % 4)
    board[row][col] = idx
    next_row, next_col = row+ROTATION[r][0], col+ROTATION[r][1]
    if 0 <= next_row < N and 0 <= next_col < N and board[next_row][next_col] == 0:
        now = (next_row, next_col)
    else:
        r = (r+1) % 4
        next_row, next_col = row+ROTATION[r][0], col+ROTATION[r][1]
        now = (next_row, next_col)

# print(order)

def tornado(row, col, r):
    s = sand[row][col]
    sand_move = []
    r1, r2, _r = (r+1) % 4, (r-1) % 4, (r+2) % 4
    # 7% move
    target_row, target_col = row + ROTATION[r1][0], col + ROTATION[r1][1]
    sand_move.append((target_row, target_col, (s * 7 // 100)))
    target_row, target_col = row + ROTATION[r2][0], col + ROTATION[r2][1]
    sand_move.append((target_row, target_col, (s * 7 // 100)))
    # 2% move
    target_row, target_col = row + 2 * ROTATION[r1][0], col + 2 * ROTATION[r1][1]
    sand_move.append((target_row, target_col, (s * 2 // 100)))
    target_row, target_col = row + 2 * ROTATION[r2][0], col + 2 * ROTATION[r2][1]
    sand_move.append((target_row, target_col, (s * 2 // 100)))
    # 1% move
    target_row, target_col = row + ROTATION[r1][0] + ROTATION[_r][0], col + ROTATION[r1][1] + ROTATION[_r][1]
    sand_move.append((target_row, target_col, (s * 1 // 100)))
    target_row, target_col = row + ROTATION[r2][0] + ROTATION[_r][0], col + ROTATION[r2][1] + ROTATION[_r][1]
    sand_move.append((target_row, target_col, (s * 1 // 100)))
    # 10% move
    target_row, target_col = row + ROTATION[r1][0] + ROTATION[r][0], col + ROTATION[r1][1] + ROTATION[r][1]
    sand_move.append((target_row, target_col, (s * 10 // 100)))
    target_row, target_col = row + ROTATION[r2][0] + ROTATION[r][0], col + ROTATION[r2][1] + ROTATION[r][1]
    sand_move.append((target_row, target_col, (s * 10 // 100)))
    # 5% move
    target_row, target_col = row + 2 * ROTATION[r][0], col + 2 * ROTATION[r][1]
    sand_move.append((target_row, target_col, (s * 5 // 100)))
    # alpha move
    alpha = s - 2 * ((s * 7 // 100) + (s * 2 // 100) + (s * 1 // 100) + (s * 10 // 100)) - (s * 5 // 100)
    target_row, target_col = row + ROTATION[r][0], col + ROTATION[r][1]
    sand_move.append((target_row, target_col, alpha))

    return sand_move

out = 0

for prev, next in zip(order[:-1], order[1:]):
    row, col, r = next[0], next[1], prev[2]
    for target_row, target_col, move in tornado(row, col, r):
        if 0 <= target_row < N and 0 <= target_col < N:
            sand[target_row][target_col] += move
        else:
            out += move

print(out)

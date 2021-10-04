from collections import deque

N, Q = map(int, input().split())
ice = []
for _ in range(2**N):
    ice.append(list(map(int, input().split())))
skills = list(map(int, input().split()))

SIZE = len(ice)
DIR = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def connected(row, col):
    c = []
    for d in DIR:
        _row, _col = row + d[0], col + d[1]
        if 0 <= _row < SIZE and 0 <= _col < SIZE:
            c.append((_row, _col))
    return c

def rotation(grid):
    row, col = len(grid), len(grid[0])
    answer = [[-1] * row for _ in range(col)]
    for r in range(row):
        for c in range(col):
            answer[c][r] = grid[row-r-1][c]
    return answer

for skill in skills:
    grid_size = 2**skill
    for row in range(0, SIZE, grid_size):
        for col in range(0, SIZE, grid_size):
            grid = []
            for line in ice[row:row+grid_size]:
                grid.append(line[col:col+grid_size])
            grid = rotation(grid)
            for d_row in range(grid_size):
                for d_col in range(grid_size):
                    ice[row+d_row][col+d_col] = grid[d_row][d_col]

    valid = [[True] * SIZE for _ in range(SIZE)]
    for row in range(SIZE):
        for col in range(SIZE):
            cnt = 0
            for con_row, con_col in connected(row, col):
                if ice[con_row][con_col] > 0:
                    cnt += 1
            if cnt < 3:
                valid[row][col] = False
    
    for row in range(SIZE):
        for col in range(SIZE):
            if not valid[row][col] and ice[row][col] > 0:
                ice[row][col] -= 1
    
ice_sum = 0
for row in range(SIZE):
    for col in range(SIZE):
        ice_sum += ice[row][col]

print(ice_sum)

max_size = 0
visited = [[False] * SIZE for _ in range(SIZE)]
for row in range(SIZE):
    for col in range(SIZE):
        iceberg = 0
        if not visited[row][col] and ice[row][col]:
            q = deque([(row, col)])
            while q:
                now_row, now_col = q.popleft()
                if not visited[now_row][now_col]:
                    visited[now_row][now_col] = True
                    iceberg += 1
                    for con_row, con_col in connected(now_row, now_col):
                        if not visited[con_row][con_col] and ice[con_row][con_col]:
                            q.append((con_row, con_col))
        max_size = max(max_size, iceberg)

print(max_size)
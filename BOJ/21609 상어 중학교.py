from collections import deque

N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))
SCORE = 0
DIR = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def rotation(matrix):
    row, col = len(matrix), len(matrix[0])
    answer = [[-1] * row for _ in range(col)]
    for r in range(row):
        for c in range(col):
            answer[c][r] = matrix[r][col-c-1]
    return answer

def gravity(matrix):
    row, col = len(matrix), len(matrix[0])
    for c in range(col):
        for r in range(row-2, -1, -1):
            if matrix[r][c] != None and matrix[r][c] >= 0:
                for i in range(r+1, row):
                    if matrix[i][c] != None:
                        break
                if matrix[i][c] == None:
                    matrix[i][c] = matrix[r][c]
                    matrix[r][c] = None
                elif i-1 != r:
                    matrix[i-1][c] = matrix[r][c]
                    matrix[r][c] = None
    return matrix

def connected(row, col):
    answer = []
    for d in DIR:
        _row, _col = row + d[0], col + d[1]
        if 0 <= _row < N and 0 <= _col < N:
            answer.append((_row, _col))
    return answer

def bfs(matrix):
    row, col = len(matrix), len(matrix[0])
    candidates = []
    visited = [[False] * col for _ in range(row)]
    for r in range(row):
        for c in range(col):
            if matrix[r][c] == None or matrix[r][c] <= 0:
                continue
            color = matrix[r][c]
            group = []
            rainbow_cnt = 0
            if not visited[r][c]:
                q = deque([(r, c)])
                while q:
                    now_r, now_c = q.popleft()
                    if not visited[now_r][now_c]:
                        visited[now_r][now_c] = True
                        group.append((now_r, now_c))
                        if matrix[now_r][now_c] == 0:
                            rainbow_cnt += 1
                        for con_r, con_c in connected(now_r, now_c):
                            if not visited[con_r][con_c] and (matrix[con_r][con_c] == 0 or matrix[con_r][con_c] == color):
                                q.append((con_r, con_c))
            if len(group) > 1:
                for _r in range(row):
                    for _c in range(col):
                        if matrix[_r][_c] == 0:
                            visited[_r][_c] = False
                candidates.append((group, rainbow_cnt, r, c))
    if candidates:
        remove_list = sorted(candidates, key=lambda x:(len(x[0]), x[1], x[2], x[3]), reverse=True)[0][0]
        for r, c in remove_list:
            matrix[r][c] = None
        return (matrix, len(remove_list) ** 2)
    return (matrix, 0)


while True:
    result = bfs(board)
    if result[1] == 0:
        break
    board = result[0]
    SCORE += result[1]
    board = gravity(board)
    board = gravity(rotation(board))

print(SCORE)
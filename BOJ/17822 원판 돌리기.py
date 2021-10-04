from collections import deque

DIR = [(-1, 0), (0, 1), (1, 0), (0, -1)]
N, M, T = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))
execute = []
for _ in range(T):
    execute.append(list(map(int, input().split())))

for rotate in execute:
    x, d, k = rotate
    k *= d * 2 - 1
    k = k % M
    for idx in range(x-1, N, x):
        board[idx] = board[idx][k:] + board[idx][:k]
    
    # print()
    # for b in board:
    #     print(b)

    visited = [[False] * M for _ in range(N)]
    is_block = False
    for row in range(N):
        for col in range(M):
            number = board[row][col]
            if number == 0:
                continue
            q = deque([(row, col)])
            block = []
            while q:
                r, c = q.popleft()
                if not visited[r][c] and board[r][c] == number:
                    visited[r][c] = True
                    block.append((r, c))
                    for dir in DIR:
                        _r, _c = r + dir[0], (c + dir[1]) % M
                        if 0 <= _r < N and 0 <= _c < M and not visited[_r][_c]:
                            q.append((_r, _c))
            if len(block) > 1:
                is_block = True
                for b in block:
                    r, c = b
                    board[r][c] = 0
    
    if not is_block:
        sum, cnt = 0, 0
        for row in range(N):
            for col in range(M):
                sum += board[row][col]
                if board[row][col] > 0:
                    cnt += 1
        if cnt == 0:
            break
        average = sum / cnt
        for row in range(N):
            for col in range(M):
                if board[row][col] > average:
                    board[row][col] -= 1
                elif board[row][col] < average and board[row][col] != 0:
                    board[row][col] += 1
    # print()
    # for b in board:
    #     print(b)

SUM = 0
for row in range(N):
    for col in range(M):
        SUM += board[row][col]
print(SUM)



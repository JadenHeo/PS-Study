from collections import deque

DIR = [(-1, 0), (0, 1), (0, -1), (1, 0)]

def input_to_idx(input):
    return int(input) - 1

def adj(v):
    nodes = []
    for dir in DIR:
        _i, _j = v[0] + dir[0], v[1] + dir[1]
        if 0 <= _i < N and 0 <= _j < N and board[_i][_j] != 1:
            nodes.append((_i, _j))
    return nodes

def bfs(start, end):
    visited = [[False] * N for _ in range(N)]
    dq = deque([(start, 0)])
    nearest = 100_000
    candidate = []
    while dq:
        now = dq.popleft()
        v, depth = now[0], now[1]
        if not end and board[v[0]][v[1]] == 2 and depth <= nearest and not visited[v[0]][v[1]]:
            nearest = depth
            candidate.append((v, depth))
        if v == end:
            return (v, depth)
        if not visited[v[0]][v[1]]:
            visited[v[0]][v[1]] = True
            # print((v, depth), end=' ')
            for e in adj(v):
                if not visited[e[0]][e[1]] and depth+1 <= nearest:
                    # print(nearest)
                    dq.append((e, depth+1))
    if candidate:
        # print(candidate)
        return sorted(candidate, key=lambda x:x[0])[0]
    return False

N, M, fuel = map(int, input().split())
visit = [[True] * N for _ in range(N)]
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))
start = tuple(map(input_to_idx, input().split()))
passangers = []
for _ in range(M):
    passangers.append(tuple(map(input_to_idx, input().split())))

for p in passangers:
    board[p[0]][p[1]] = 2
    visit[p[0]][p[1]], visit[p[2]][p[3]] = False, False

destination = {(p[0], p[1]) : (p[2], p[3]) for p in passangers}

now = start
pos = 0
cnt = M
while fuel >= 0 and cnt > 0:
    if pos == 0 or pos == 2:
        if bfs(now, None):
            now, used = bfs(now, None)
            if used > fuel:
                break
            fuel -= used
            board[now[0]][now[1]] = 0
            pos = 1
        else:
            break
    else:
        if bfs(now, destination[now]):
            now, used = bfs(now, destination[now])
            if used > fuel:
                break
            fuel += used
            cnt -= 1
            pos = 2
        else:
            break
    # print(now, fuel, pos)

if cnt == 0:
    print(fuel)
else:
    print(-1)
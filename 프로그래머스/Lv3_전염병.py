from collections import deque

DIRS = [(-1,0), (1, 0), (0, -1), (0, 1)]

def solution(m, n, infests, vaccinateds):
    not_infected = m * n - len(infests) - len(vaccinateds)
    new_infests = deque([(i-1, j-1, 0) for i, j in infests])
    visited = [[False for _ in range(n)] for _ in range(m)]
    for i, j in infests + vaccinateds:
        visited[i-1][j-1] = True
    while new_infests:
        i, j, day = new_infests.popleft()
        for di, dj in DIRS:
            next_i, next_j = i + di, j + dj
            if 0 <= next_i < m and 0 <= next_j < n:
                if not visited[next_i][next_j]:
                    new_infests.append((next_i, next_j, day + 1))
                    visited[next_i][next_j] = True
                    not_infected -= 1
    if not_infected == 0:
        return day
    else:
        return -1
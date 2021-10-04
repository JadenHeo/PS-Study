from collections import deque

DELTAS = [[1, 0], [0, 1], [-1, 0], [0, -1]]
ROW, COL, DISTANCE = 0, 1, 2

def is_valid(n, m, visited, location):
    return True if 0 <= location[ROW] < n and 0 <= location[COL] < m and not visited[location[ROW]][location[COL]] else False

def solution(maps):
    my_deque = deque([[0, 0, 1]])
    n, m = len(maps), len(maps[0])
    enemy = [n-1, m-1]
    visited = [[False if maps[row][col] else True for col in range(m)] for row in range(n)]
    while my_deque:
        start = my_deque.popleft()
        if start[:-1] == enemy:
            return start[DISTANCE]
        if not visited[start[ROW]][start[COL]]:
            visited[start[ROW]][start[COL]] = True
            for delta in DELTAS:
                arrive = [l + dl for l, dl in zip(start, delta)] + [start[DISTANCE] + 1]
                if is_valid(n, m, visited, arrive):
                    my_deque.append(arrive)
    return -1
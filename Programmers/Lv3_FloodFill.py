import sys
sys.setrecursionlimit(100_000)

DIRS = [[0, -1], [0, 1], [-1, 0], [1, 0]]

def dfs(start, image, visited):
    visited[start[0]][start[1]] = True
    surroundings = [(start[0] + dx, start[1] + dy) for dx, dy in DIRS]
    for row, col in surroundings:
        if 0 <= row < len(visited) and 0 <= col < len(visited[0]):
            if image[row][col] == image[start[0]][start[1]] and not visited[row][col]:
                dfs((row, col), image, visited)
        
def solution(n, m, image):
    answer = 0
    visited = [[False] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if not visited[i][j]:
                answer += 1
                dfs((i, j), image, visited)
    return answer
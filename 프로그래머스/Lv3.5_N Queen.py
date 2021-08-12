def is_valid(x, y, n, queen_positions):
    for i in range(x):
        if y == queen_positions[i] or y - queen_positions[i] == x - i or queen_positions[i] - y == x - i:
            return False
    return True

def dfs(x, n, queen_positions):
    cnt = 0
    if x == n:
        return 1
    for y in range(n):
        if is_valid(x, y, n, queen_positions):
            queen_positions[x] = y
            cnt += dfs(x+1, n, queen_positions)
    return cnt
            
def solution(n):
    queen_positions = [0 for _ in range(n)]
    return dfs(0, n, queen_positions)
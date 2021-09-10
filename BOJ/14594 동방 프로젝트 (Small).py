N = int(input())
M = int(input())
walls = [1 for _ in range(N+1)]
for _ in range(M):
    i, j = map(int, input().split())
    for k in range(i, j):
        walls[k] = 0
print(sum(walls)-1)
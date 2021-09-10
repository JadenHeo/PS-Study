from math import inf

n = int(input())
m = int(input())
V = [[inf] * (n+1) for _ in range(n+1)]

for _ in range(m):
    i, j, cost = map(int, input().split())
    V[i][j] = min(V[i][j], cost)

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i != j and i != k and j != k and V[i][j] > V[i][k]+V[k][j]:
                V[i][j] = V[i][k]+V[k][j]

for i in range(1, n+1):
    for j in range(1, n+1):
        if V[i][j] == inf:
            V[i][j] = 0
        print(V[i][j], end=' ')
    print()
from math import inf
n = int(input())
m = int(input())
V = [[inf] * (n+1) for _ in range(n+1)]
pi = [[0] * (n+1) for _ in range(n+1)]
for _ in range(m):
    i, j, cost = map(int, input().split())
    V[i][j] = min(V[i][j], cost)
    pi[i][j] = i

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i != j and i != k and j != k and V[i][j] > V[i][k]+V[k][j]:
                V[i][j] = V[i][k]+V[k][j]
                pi[i][j] = pi[k][j]

for i in range(1, n+1):
    for j in range(1, n+1):
        if V[i][j] == inf:
            V[i][j] = 0
        print(V[i][j], end=' ')
    print()
    
for i in range(1, n+1):
    for j in range(1, n+1):
        if not V[i][j]:
            print(0)
        elif pi[i][j] == i:
            print(2, i, j)
        else:
            path = [j]
            while pi[i][j] != i:
                path.append(pi[i][j])
                j = pi[i][j]
            path.append(i)
            path.reverse()
            print(len(path), end=' ')
            for p in path:
                print(p, end=' ')
            print()
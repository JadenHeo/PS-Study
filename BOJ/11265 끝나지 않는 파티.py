N, M = map(int, input().split())
V = []
for _ in range(N):
    v = list(map(int, input().split()))
    V.append(v)

for k in range(N):
    for i in range(N):
        for j in range(N):
            if i != j and i != k and j != k:
                V[i][j] = min(V[i][j], V[i][k]+V[k][j])

for _ in range(M):
    start, end, time = map(int, input().split())
    if V[start-1][end-1] <= time:
        print('Enjoy other party')
    else:
        print('Stay here')
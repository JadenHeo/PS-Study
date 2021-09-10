def solution(N, M, V):
    return 0


T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    V = []
    for _ in range(M):
        V.append(list(map(int, input().split())))
    print(N-1)
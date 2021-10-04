from itertools import combinations

N = int(input())
S = []
for _ in range(N):
    S.append(list(map(int, input().split())))

def stat(team):
    answer = 0
    for i, j in combinations(team, 2):
        answer += S[i][j] + S[j][i]
    return answer

result = 100_000
for case in combinations(range(N), N//2):
    start = list(case)
    link = list()
    for i in range(N):
        if i not in start:
            link.append(i)
    result = min(result, abs(stat(start) - stat(link)))

print(result)
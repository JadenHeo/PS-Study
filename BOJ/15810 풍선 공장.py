N, M = map(int, input().split())
A = list(map(int, input().split()))
fast, slow = min(A), max(A)
min_time = 0
max_time = M * slow
cnt = 0
while min_time < max_time:
    cnt = 0
    time = (min_time + max_time) // 2
    for a in A:
        cnt += time // a
    if cnt >= M:
        max_time = time
    else:
        min_time = time + 1
print(min_time)
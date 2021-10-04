from itertools import product

N = int(input())
day = list()
for _ in range(N):
    day.append(list(map(int, input().split())))

max_profit = 0
for case in product([0, 1], repeat=N):
    counsel = []
    for idx, d in enumerate(case):
        if d:
            counsel.append([day[idx],idx])
    counsel.append([[0, 0], N])
    # print(counsel)
    valid = True
    for c, next_c in zip(counsel, counsel[1:]):
        if c[1]+c[0][0] > next_c[1]:
            valid = False
    if valid:
        profit = 0
        for c in counsel:
            profit += c[0][1]
        # print(counsel)
        # print(profit)
        max_profit = max(max_profit, profit)
        
print(max_profit)
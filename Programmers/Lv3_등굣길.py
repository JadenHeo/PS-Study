def solution(m, n, puddles):
    locations = [[0] * (m+1) for _ in range(n+1)]
    locations[1][1] = 1
    puddles = set([(y, x) for x, y in puddles])
    for row in range(1, n+1):
        for col in range(1, m+1):
            if (row != 1 or col != 1) and (row, col) not in puddles:
                locations[row][col] = (locations[row-1][col] + locations[row][col-1]) % 1_000_000_007
    return locations[-1][-1]
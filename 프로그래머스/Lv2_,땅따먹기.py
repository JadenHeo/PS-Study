def solution(land):
    for row in range(1, len(land)):
        for col in range(4):
            land_without_same_col = land[row-1][:col] + land[row-1][col+1:]
            land[row][col] += max(land_without_same_col)
    return max(land[-1])
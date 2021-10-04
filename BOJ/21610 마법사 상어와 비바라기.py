DIR = [0, (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
DIAGONAL = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
N, M = map(int, input().split())
water = []
for _ in range(N):
    water.append(list(map(int, input().split())))
moves = []
for _ in range(M):
    moves.append(tuple(map(int, input().split())))
cloud = [[N-1, 0], [N-1, 1], [N-2, 0], [N-2, 1]]

def close(row, col):
    close_list = []
    for d in DIAGONAL:
        _row, _col = row + d[0], col + d[1]
        if 0 <= _row < N and 0 <= _col < N:
            close_list.append((_row, _col))
    return close_list

for move in moves:
    for i in range(len(cloud)):
        cloud[i][0] = (cloud[i][0] + move[1]*DIR[move[0]][0]) % N
        cloud[i][1] = (cloud[i][1] + move[1]*DIR[move[0]][1]) % N
    
    for c in cloud:
        row, col = c
        water[row][col] += 1
    
    for c in cloud:
        row, col = c
        cnt = 0
        for close_bucket in close(row, col):
            _row, _col = close_bucket
            if water[_row][_col]:
                cnt += 1
        water[row][col] += cnt
    
    used_cloud = set([tuple(c) for c in cloud])

    cloud = []

    for row in range(N):
        for col in range(N):
            if water[row][col] >= 2 and (row, col) not in used_cloud:
                cloud.append([row, col])
                water[row][col] -= 2

total_water = 0
for w in water:
    total_water += sum(w)
print(total_water)



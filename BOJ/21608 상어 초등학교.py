N = int(input())
prefer = dict()
students = []
for _ in range(N**2):
    temp = list(map(int, input().split()))
    students.append(temp[0])
    prefer[temp[0]] = set(temp[1:])

DIR = [(-1, 0), (0, -1), (0, 1), (1, 0)]
seat = [[0] * N for _ in range(N)]

def close(s):
    close_list = []
    for dir in DIR:
        i, j = s[0] + dir[0], s[1] + dir[1]
        if 0 <= i < N and 0 <= j < N:
            close_list.append((i, j))
    return close_list

def find_seat(student):
    candidates = []
    for row in range(N):
        for col in range(N):
            if seat[row][col] == 0:
                prefer_cnt = 0
                empty_cnt = 0
                for s in close((row, col)):
                    if seat[s[0]][s[1]] in prefer[student]:
                        prefer_cnt += 1
                    if seat[s[0]][s[1]] == 0:
                        empty_cnt += 1
                candidates.append((-prefer_cnt, -empty_cnt, row, col))
    return sorted(candidates)[0][2:]

for student in students:
    seat_info = find_seat(student)
    # print(student, seat_info)
    seat[seat_info[0]][seat_info[1]] = student

satisfy = 0
for row in range(N):
    for col in range(N):
        prefer_cnt = 0
        for s in close((row, col)):
            if seat[s[0]][s[1]] in prefer[seat[row][col]]:
                prefer_cnt += 1
        if prefer_cnt > 0:
            satisfy += 10**(prefer_cnt-1)

print(satisfy)
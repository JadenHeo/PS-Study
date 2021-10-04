from collections import deque

N, K = map(int, input().split())
SIZE = 2 * N
belt = list(map(int, input().split()))
is_empty = [True] * (2*N)

start, end = 0, N-1
step, zeros = 0, 0
robots = deque([])

while zeros < K:
    step += 1

    # print('step', step, '==============================')
    # print('초기단계')
    # temp = start
    # for _ in range(N):
    #     print((temp, belt[temp], is_empty[temp]), end=' ')
    #     temp = (temp+1) % SIZE
    # print()
    # temp = (temp+N-1) % SIZE
    # for _ in range(N):
    #     print((temp, belt[temp], is_empty[temp]), end=' ')
    #     temp = (temp-1) % SIZE
    # print()

    start, end = (start-1) % SIZE, (end-1) % SIZE
    arrived = False
    for idx in range(len(robots)):
        if robots[idx] == end:
            arrived = True
            is_empty[robots[idx]] = True
    if arrived:
        robots.popleft()

    # print('1단계 이후 - 벨트 이동 완료')
    # temp = start
    # for _ in range(N):
    #     print((temp, belt[temp], is_empty[temp]), end=' ')
    #     temp = (temp+1) % SIZE
    # print()
    # temp = (temp+N-1) % SIZE
    # for _ in range(N):
    #     print((temp, belt[temp], is_empty[temp]), end=' ')
    #     temp = (temp-1) % SIZE
    # print()

    arrived = False
    for idx in range(len(robots)):
        if is_empty[(robots[idx]+1) % SIZE] and belt[(robots[idx]+1) % SIZE]:
            is_empty[robots[idx]] = True
            robots[idx] = (robots[idx]+1) % SIZE
            if robots[idx] != end:
                is_empty[robots[idx]] = False
            else:
                arrived = True
            belt[robots[idx]] -= 1
            if not belt[robots[idx]]:
                zeros += 1
    if arrived:
        robots.popleft()
    
    # print('2단계 이후 - 로봇 이동 완료')
    # temp = start
    # for _ in range(N):
    #     print((temp, belt[temp], is_empty[temp]), end=' ')
    #     temp = (temp+1) % SIZE
    # print()
    # temp = (temp+N-1) % SIZE
    # for _ in range(N):
    #     print((temp, belt[temp], is_empty[temp]), end=' ')
    #     temp = (temp-1) % SIZE
    # print()

    if belt[start]:
        robots.append(start)
        is_empty[start] = False
        belt[start] -= 1
        if not belt[start]:
            zeros += 1
    
    # print('3단계 이후 - 올리는 위치에 적재')
    # temp = start
    # for _ in range(N):
    #     print((temp, belt[temp], is_empty[temp]), end=' ')
    #     temp = (temp+1) % SIZE
    # print()
    # temp = (temp+N-1) % SIZE
    # for _ in range(N):
    #     print((temp, belt[temp], is_empty[temp]), end=' ')
    #     temp = (temp-1) % SIZE
    # print()

    # print(robots)
    # print(zeros)

print(step)
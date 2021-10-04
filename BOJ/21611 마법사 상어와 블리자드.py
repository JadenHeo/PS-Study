N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))
skills = []
for _ in range(M):
    skills.append(tuple(map(int, input().split())))

DIR = [-1, (-1, 0), (1, 0), (0, -1), (0, 1)]
ROTATION = [(0, 1), (1, 0), (0, -1), (-1, 0)]
shark = ((N//2), (N//2))
start = (0, 0)
idx_board = [[0] * N for _ in range(N)]
idx_to_pos = [0] * (N**2)
r = 0
for idx in range(N**2-1, 0, -1):
    idx_to_pos[idx] = start
    idx_board[start[0]][start[1]] = idx
    next_pos = start[0] + ROTATION[r][0], start[1] + ROTATION[r][1]
    if not (0 <= next_pos[0] < N and 0 <= next_pos[1] < N and idx_board[next_pos[0]][next_pos[1]] == 0):
        r = (r+1) % 4
        next_pos = start[0] + ROTATION[r][0], start[1] + ROTATION[r][1]
    start = next_pos

answer = 0

for skill in skills:
    d, s = skill
    destroy = (shark[0] + DIR[d][0], shark[1] + DIR[d][1])
    for _ in range(s):
        board[destroy[0]][destroy[1]] = 0
        destroy = (destroy[0] + DIR[d][0], destroy[1] + DIR[d][1])
    
    # for b in board:
    #     print(b)
    # print()

    total_balls = N**2
    for b in board:
        total_balls -= b.count(0)
    # print(total_balls)

    ball_pos = 1
    for pos in idx_to_pos[1:]:
        target = idx_to_pos[ball_pos]
        if ball_pos > total_balls:
            board[target[0]][target[1]] = 0
            ball_pos += 1
            continue
        if board[pos[0]][pos[1]] == 0:
            continue
        board[target[0]][target[1]] = board[pos[0]][pos[1]]
        # print(ball_pos, pos, target, board[target[0]][target[1]])
        ball_pos += 1
        
    # for b in board:
    #     print(b)
    # print()

    prev_total_balls = total_balls
    while True:
        prev, stack = 0, []
        for ball_pos in range(1, total_balls+2):
            if not stack:
                prev = board[idx_to_pos[ball_pos][0]][idx_to_pos[ball_pos][1]]
                stack.append((idx_to_pos[ball_pos][0], idx_to_pos[ball_pos][1]))
            elif board[idx_to_pos[ball_pos][0]][idx_to_pos[ball_pos][1]] == prev:
                stack.append((idx_to_pos[ball_pos][0], idx_to_pos[ball_pos][1]))
            else:
                if len(stack) >= 4:
                    for pos in stack:
                        answer += board[pos[0]][pos[1]]
                        board[pos[0]][pos[1]] = 0
                    total_balls -= len(stack)
                prev = board[idx_to_pos[ball_pos][0]][idx_to_pos[ball_pos][1]]
                stack = [(idx_to_pos[ball_pos][0], idx_to_pos[ball_pos][1])]

        # for b in board:
        #     print(b)
        # print()

        ball_pos = 1
        for pos in idx_to_pos[1:]:
            target = idx_to_pos[ball_pos]
            if ball_pos > total_balls:
                board[target[0]][target[1]] = 0
                ball_pos += 1
                continue
            if board[pos[0]][pos[1]] == 0:
                continue
            board[target[0]][target[1]] = board[pos[0]][pos[1]]
            # print(ball_pos, pos, target, board[target[0]][target[1]])
            ball_pos += 1
        
        # for b in board:
        #     print(b)

        if total_balls == prev_total_balls:
            break
        prev_total_balls = total_balls
    
    prev, stack, balls = 0, [], []
    for ball_pos in range(1, total_balls+2):
        if not stack:
            prev = board[idx_to_pos[ball_pos][0]][idx_to_pos[ball_pos][1]]
            stack.append((idx_to_pos[ball_pos][0], idx_to_pos[ball_pos][1]))
        elif board[idx_to_pos[ball_pos][0]][idx_to_pos[ball_pos][1]] == prev:
            stack.append((idx_to_pos[ball_pos][0], idx_to_pos[ball_pos][1]))
        else:
            ball_number = board[stack[0][0]][stack[0][1]]
            balls.append(len(stack))
            balls.append(ball_number)
            prev = board[idx_to_pos[ball_pos][0]][idx_to_pos[ball_pos][1]]
            stack = [(idx_to_pos[ball_pos][0], idx_to_pos[ball_pos][1])]
    total_balls = min(len(balls), N**2-1)
    for ball_pos in range(1, total_balls+1):
        board[idx_to_pos[ball_pos][0]][idx_to_pos[ball_pos][1]] = balls[ball_pos-1]
    
    # for b in board:
    #         print(b)
    # print()

print(answer)
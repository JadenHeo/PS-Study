from itertools import product

blueline = {10:130, 130:160, 160:190, 190:250, 20:220, 220:240, 240:250, 30:280, 280:270, 270:260, 260:250, 250:300, 300:350, 350:40, 40:42}
FINISH = 42
BLUE = 1
SCORE = 0
numbers = list(map(int, input().split()))
cnt = 0
for case in product((0, 1, 2, 3), repeat=10):
    cnt += 1
    horse_pos = [0] * 4
    score = 0
    for turn in range(10):
        horse, dice = case[turn], numbers[turn]
        if horse_pos[horse] == -1:
            break
        if horse_pos[horse] in [10, 20, 30] or horse_pos[horse] > 42:
            next_pos = horse_pos[horse]
            for _ in range(dice):
                if next_pos == 42:
                    break
                next_pos = blueline[next_pos]
        else:
            next_pos = horse_pos[horse] + 2 * dice
        if next_pos in horse_pos:
            break
        if next_pos < 42:
            score += next_pos
        elif 42 <= next_pos < 100:
            horse_pos[horse] = -1
            continue
        elif next_pos > 100:
            score += next_pos // 10
        horse_pos[horse] = next_pos
    SCORE = max(SCORE, score)
print(SCORE)


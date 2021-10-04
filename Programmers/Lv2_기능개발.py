import math
from collections import deque

def solution(progresses, speeds):
    answer = []
    finish_dates = deque([math.ceil((100 - progress) / speed) for progress, speed in zip(progresses, speeds)])
    date = 0
    while finish_dates:
        count = 0
        if finish_dates[0] == date:
            while finish_dates and finish_dates[0] <= date:
                finish_dates.popleft()
                count += 1
            answer.append(count)
        date += 1
    return answer
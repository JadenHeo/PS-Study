import heapq

PRIORITY = 0
TIME = 1
INDEX = 2

def solution(reqs):
    answer = []
    waiting_reqs = []
    heapq.heapify(waiting_reqs)
    now_time = 0
    time_stamp = 0
    req_index = 0
    now_working = []
    while now_working or waiting_reqs or req_index < len(reqs):
        if now_time % 3 == 0 and req_index < len(reqs):
            heapq.heappush(waiting_reqs, [-reqs[req_index][PRIORITY], reqs[req_index][TIME], req_index])
            req_index += 1
        if not now_working and waiting_reqs:
            now_working = heapq.heappop(waiting_reqs)
            answer.append(now_working[INDEX] + 1)
            time_stamp = now_time + now_working[TIME]
        if now_time == time_stamp:
            if waiting_reqs:
                now_working = heapq.heappop(waiting_reqs)
                answer.append(now_working[INDEX] + 1)
                time_stamp = now_time + now_working[TIME]
            else:
                now_working = []
        now_time += 1
    return answer
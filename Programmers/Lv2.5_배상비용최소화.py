import heapq

def solution(N, works):
    if N >= sum(works):
        return 0
    works = [(-work, work) for work in works]
    heapq.heapify(works)
    
    for _ in range(N):
        work_max = heapq.heappop(works)[1] - 1
        heapq.heappush(works, (-work_max, work_max))
    return sum([work[0]**2 for work in works])
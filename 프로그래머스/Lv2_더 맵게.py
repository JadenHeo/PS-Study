import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    while len(scoville) > 1:
        answer += 1
        food1 = heapq.heappop(scoville)
        food2 = heapq.heappop(scoville)
        blended = food1 + 2 * food2
        heapq.heappush(scoville, blended)
        if scoville[0] >= K:
            return answer
    return -1
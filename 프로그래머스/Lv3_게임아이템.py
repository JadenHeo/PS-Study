import heapq

ATTACK = 0
DAMAGE = 1
INDEX = 2

def solution(healths, items):
    answer = []
    heap = []
    heapq.heapify(healths)
    items_with_index = [(items[i][DAMAGE], items[i][ATTACK], i + 1) for i in range(len(items))]
    heapq.heapify(items_with_index)
    while healths:
        health = heapq.heappop(healths)
        while items_with_index:
            item = items_with_index[0]
            if health - item[0] < 100:
                break
            heapq.heappop(items_with_index)
            heapq.heappush(heap, (-item[DAMAGE], item[INDEX]))
        if heap:
            answer.append(heapq.heappop(heap)[1])
    return sorted(answer)
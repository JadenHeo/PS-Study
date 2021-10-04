from collections import deque

def bfs(start, computers, visited):
    q = deque([start])
    while q:
        cursor = q.popleft()
        if not visited[cursor]:
            visited[cursor] = True
            #print("cursor :", cursor)
            for next in range(len(computers[cursor])):
                if next == cursor or computers[cursor][next] == 0:
                    continue
                elif not visited[next]:
                    q.append(next)
                    #print(q)
        
def solution(n, computers):
    answer = 0
    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            bfs(i, computers, visited)
            answer += 1
            #print(answer)
            
    return answer
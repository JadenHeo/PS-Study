from collections import deque

def solution(n, signs):
    answer = [[0] * n for _ in range(n)]
    edges = {}
    for station in range(n):
        edges[station] = [i for i in range(n) if signs[station][i]]
    for station in range(n):
        stations = deque([station])
        reachable_stations = set()
        while stations:
            now = stations.popleft()
            for next_station in edges[now]:
                if next_station not in reachable_stations:
                    reachable_stations.add(next_station)
                    stations.append(next_station)
                    answer[station][next_station] = 1
    return answer
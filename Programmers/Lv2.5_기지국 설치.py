import math

def get_darkzone(stations, darkzone_idx, n, w):
    left_station = stations[darkzone_idx-1] if darkzone_idx > 0 else 0
    right_station = stations[darkzone_idx] if darkzone_idx < len(stations) else n + 1
    if darkzone_idx == 0 or darkzone_idx == len(stations):
        return right_station - left_station - w - 1
    else:
        return right_station - left_station - 2 * w - 1

def required_station_number(darkzone, cover):
    return math.ceil(darkzone / cover)

def solution(n, stations, w):
    answer = 0
    cover = 2 * w + 1
    for darkzone_idx in range(len(stations)+1):
        darkzone = get_darkzone(stations, darkzone_idx, n, w)
        if darkzone > 0:
            answer += required_station_number(darkzone, cover)
    return answer
import math

def solution_greedy(l, v):
    v = sorted(v)
    max_dif = 2 * max(v[0] - 0, l - v[-1])
    for prev_light, next_light in zip(v, v[1:]):
        if next_light - prev_light > max_dif:
            max_dif = next_light - prev_light
    return math.ceil(max_dif / 2)

def possible(mid, left_edge, right_edge, distances):
    if mid < left_edge or mid < right_edge:
        return False
    for distance in distances:
        if mid * 2 < distance:
            return False
    return True

def solution(l, v):
    v = sorted(v)
    lower_bound, upper_bound = 1, l
    left_edge, right_edge = v[0] - 0, l - v[-1]
    distances = [now - prev for now, prev in zip(v[1:], v[:-1])]   
    while lower_bound <= upper_bound:
        mid = (lower_bound + upper_bound) // 2
        if possible(mid, left_edge, right_edge, distances):
            upper_bound = mid - 1
        else:
            lower_bound = mid + 1
    return upper_bound + 1
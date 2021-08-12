def solution(max_weight, specs, names):
    answer = 1
    specs = {name : int(weight) for name, weight in specs}
    now_weight = 0
    for name in names:
        if now_weight + specs[name] <= max_weight:
            now_weight += specs[name]
        else:
            answer += 1
            now_weight = specs[name]
    return answer
def is_valid(skills_order, filtered):
    return skills_order.startswith(''.join(filtered))

def solution(skills_order, candidates):
    answer = 0
    for candidate in candidates:
        filtered = filter(lambda skill: skill in skills_order, candidate)
        if is_valid(skills_order, filtered):
            answer += 1
    return answer
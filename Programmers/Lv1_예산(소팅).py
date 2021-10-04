def solution(d, budget):
    used = 0
    for department, cost in enumerate(sorted(d)):
        used += cost
        if used > budget:
            return department
    return len(d)
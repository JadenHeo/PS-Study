from collections import defaultdict

def solution(skills_order, skill_tree):
    skills_order = defaultdict(int, {skill : idx for idx, skill in enumerate(skills_order)})
    skill_count = 1
    for skill in skill_tree:
        if skills_order[skill] > skill_count:
            return False
        elif skills_order[skill] == skill_count:
            skill_count += 1
    return True
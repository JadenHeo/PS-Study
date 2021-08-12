from functools import cmp_to_key

def cmp(a, b):
    case1 = int(a + b)
    case2 = int(b + a)
    return case2 - case1

def solution(numbers):
    if not sum(numbers):
        return '0'
    numbers = list(map(str, numbers))
    numbers = sorted(numbers, key=cmp_to_key(cmp))
    return ''.join(numbers)
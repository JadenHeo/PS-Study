from itertools import product

def solution(monster, S1, S2, S3):
    total = S1 * S2 * S3
    count = 0
    monster = set(monster)
    for s1, s2, s3 in product(range(1, S1+1), range(1, S2+1), range(1, S3+1)):
        if s1 + s2 + s3 + 1 not in monster:
            count += 1
    return int(count / total * 1000)
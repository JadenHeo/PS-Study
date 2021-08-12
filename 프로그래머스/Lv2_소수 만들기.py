from itertools import combinations

def prime_nums(n):
    is_prime = [True] * (n+1)
    is_prime[0], is_prime[1] = False, False
    for divisor in range(2, n+1):
        if not is_prime[divisor]:
            continue
        for multiple in range(divisor ** 2, n+1, divisor):
            is_prime[multiple] = False
    return [prime_num for prime_num in range(2, n+1) if is_prime[prime_num]]
        
def solution(nums):
    MAXIMUM_NUMS = 3000
    answer = 0
    prime_nums_set = set(prime_nums(MAXIMUM_NUMS))
    sumlist = combinations(nums, 3)
    for s in sumlist:
        if sum(s) in prime_nums_set:
            answer += 1
    return answer
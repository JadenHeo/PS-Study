from itertools import combinations

def solution(m, weights):
    candy_combinations = []
    for number_of_candies in range(1, len(weights)+1):
        candy_combinations += combinations(weights, number_of_candies)
    return len([0 for candies in candy_combinations if sum(candies) == m])
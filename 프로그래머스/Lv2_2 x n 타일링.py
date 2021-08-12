import sys
sys.setrecursionlimit(100000)

my_dic = {1:1, 2:2}
def solution_recursion(n):
    if n in my_dic:
        return my_dic[n]
    my_dic[n] = (solution_recursion(n-1) + solution_recursion(n-2)) % 1_000_000_007
    return my_dic[n]

def solution(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    now, prev = 2, 1
    for _ in range(3, n+1):
        answer = (now + prev) % 1_000_000_007 
        prev = now
        now = answer
    return answer
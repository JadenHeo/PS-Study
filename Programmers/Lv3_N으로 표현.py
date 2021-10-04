my_dic = {}

def recursion(N, num):
    if num == 1:
        my_dic[1] = set([N])
        return set([N])
    if num in my_dic:
        return my_dic[num]
    num_list = set([N * int('1'*num)])
    for i in range(1, num // 2 + 1):
        for a in recursion(N, i):
            for b in recursion(N, num-i):
                num_list.add(a + b)
                num_list.add(a - b)
                num_list.add(b - a)
                num_list.add(a * b)
                if a != 0:
                    num_list.add(b // a)
                if b != 0:
                    num_list.add(a // b)
    my_dic[num] = num_list
    return num_list

def solution(N, number):
    for answer in range(1, 9):
        if number in recursion(N, answer):
            return answer
    return -1
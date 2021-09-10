from collections import deque

T = int(input())
for _ in range(T):
    func = input()
    num = input()
    num_list = input()[1:-1]
    if num_list:
        num_list = deque(map(int, num_list.split(',')))
    reverse = False
    error = False
    for f in func:
        if f == 'R':
            reverse = not reverse
        elif num_list:
            if not reverse:
                num_list.popleft()
            else:
                num_list.pop()
        else:
            error = True
    
    if error:
        print('error')
    elif reverse:
        print('[', end='')
        for i in range(len(num_list)):
            print(num_list[len(num_list)-1-i], end='')
            if i != len(num_list) - 1:
                print(',', end='')
        print(']')
    else:
        print('[', end='')
        for i in range(len(num_list)):
            print(num_list[i], end='')
            if i != len(num_list) - 1:
                print(',', end='')
        print(']')
def solution(s):
    stack = []
    for alphabet in s:
        if not stack:
            stack.append(alphabet)
        elif alphabet == stack[-1]:
            stack.pop()
        else:
            stack.append(alphabet)
    return 0 if stack else 1
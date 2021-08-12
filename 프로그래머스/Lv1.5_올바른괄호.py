def solution(parenthses):
    answer = True
    stack = []
    for parenthesis in parenthses:
        if not stack:
            stack.append(parenthesis)
        elif stack[-1] == '(' and parenthesis == ')':
            stack.pop()
        else:
            stack.append(parenthesis)
    if stack:
        answer = False

    return answer
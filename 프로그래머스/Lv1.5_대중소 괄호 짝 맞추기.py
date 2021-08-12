def is_pair(parenthesis1, parenthesis2):
    pair = {'(' : ')', '{' : '}', '[' : ']'}
    if pair.get(parenthesis1) == parenthesis2:
        return True
    return False

def solution(parentheses):
    stack = []
    for parenthesis in parentheses:
        if not stack:
            stack.append(parenthesis)
        elif is_pair(stack[-1], parenthesis):
            stack.pop()
        else:
            stack.append(parenthesis)
    if stack:
        return False
    return True
from collections import Counter
def perms(xs):
    def helper(prefix, ws):
        if all(v==0 for v in ws.values()):
            yield prefix
        for w in ws:
            if ws[w] > 0:
                yield from helper((*prefix, w), {**ws, w:ws[w]-1})
    yield from helper((), Counter(xs))

def op(a, b, operand):
    if operand == '+':
        return a + b
    elif operand == '-':
        return a - b
    elif operand == '*':
        return a * b
    elif a < 0:
        return -(-a // b)
    else:
        return a // b

N = int(input())
numbers = list(map(int, input().split()))
plus, minus, multiply, division = map(int, input().split())
operands = '+'*plus + '-'*minus + '*'*multiply + '/'*division

cases = []
for p in perms(operands):
  cases.append(''.join(p))

min_result, max_result = 1_000_000_000, -1_000_000_000

for case in cases:
    temp = numbers[0]
    for b, operand in zip(numbers[1:], case):
        temp = op(temp ,b, operand)
    min_result = min(min_result, temp)
    max_result = max(max_result, temp)

print(max_result)
print(min_result)


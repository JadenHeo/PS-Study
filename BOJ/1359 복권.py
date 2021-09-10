def combi(x, y):
    if x < y:
        return 0
    a, b = 1, 1
    for i in range(y):
        a *= (x-i)
        b *= (i+1)
    return a // b
N, M, K = map(int, input().split())
s = 0
for i in range(K, M+1):
    s += combi(M, i) * combi(N-M, M-i)
print(s / combi(N, M))
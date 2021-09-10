from math import inf

n = int(input())
V = [[inf]*26 for _ in range(26)]

for _ in range(n):
    s = input()
    i, j = ord(s[0])-97, ord(s[-1])-97
    V[i][j] = 1
    # print(i, j)
    
for k in range(26):
    for i in range(26):
        for j in range(26):
            if i != j and i != k and j != k:
                V[i][j] = min(V[i][j], V[i][k]+V[k][j])
                
m = int(input())
for _ in range(m):
    s = input()
    i, j = ord(s[0])-97, ord(s[-1])-97
    if V[i][j] != inf:
        print('T')
    else:
        print('F')
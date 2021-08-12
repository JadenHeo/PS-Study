import math

def solution(brown, red):
    b = brown / 2 + 2
    c = brown + red
    return [(b + math.sqrt(b**2 - 4*c)) / 2, (b - math.sqrt(b**2 - 4*c)) / 2]
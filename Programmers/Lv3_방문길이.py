def solution(dirs):
    now = (0, 0)
    X, Y = 0, 1
    routes = set()
    DELTAS = {'U' : (0, 1), 'D' : (0, -1), 'R' : (1, 0), 'L' : (-1, 0)}
    for d in dirs:
        x, y = now[X] + DELTAS[d][X], now[Y] + DELTAS[d][Y]
        if x < -5 or x > 5 or y < -5 or y > 5:
            continue
        routes.add((now, (x, y)))
        routes.add(((x, y), now))
        now = (x, y)
    return len(routes) / 2
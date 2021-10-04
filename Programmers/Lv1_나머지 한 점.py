import collections

def solution(v):
    x, y, counted_coordinate = 0, 1, 0
    x_counter = collections.Counter([coordinate[x] for coordinate in v])
    y_counter = collections.Counter([coordinate[y] for coordinate in v])
    return [x_counter.most_common()[-1][counted_coordinate], y_counter.most_common()[-1][counted_coordinate]]
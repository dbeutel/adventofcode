import ast
from itertools import product


def run(rocks, until, threshold):
    x, y = 500, 0
    while until(y, rocks):
        for dx in [0, -1, 1]:
            if (x + dx, y + 1) not in rocks and threshold(y):
                x, y = x + dx, y + 1
                break
        else:
            rocks = rocks | {(x, y)}
            x, y = 500, 0
    return rocks


rocks = set()
maxy = -1
with open("input14.txt") as fobj:
    for line in fobj:
        corners = [*map(ast.literal_eval, line.split(" -> "))]
        for c in zip(corners, corners[1:]):
            maxy = max(maxy, c[0][1], c[1][1])
            rocks |= {*product(*map(lambda p: range(min(p), max(p) + 1), zip(*c)))}

nrocks = len(rocks)
maxy = max(map(lambda i: i[1], rocks))
print(len(run(rocks, lambda y, _: y <= maxy, lambda y: True)) - nrocks)
print(len(run(rocks, lambda _, r: (500, 0) not in r, lambda y: y < maxy + 1)) - nrocks)

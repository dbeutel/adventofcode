import ast
from itertools import pairwise, product


def run(rocks, until, threshold):
    x, y = 500, 0
    while until(y, rocks):
        for dx in [0, -1, 1]:
            if (x + dx, y + 1) not in rocks and threshold(y):
                x, y = x + dx, y + 1
                break
        else:
            rocks.add((x, y))
            x, y = 500, 0
    return rocks


rocks = set()
with open("input14.txt") as fobj:
    for line in fobj:
        for c in pairwise(map(ast.literal_eval, line.split(" -> "))):
            rocks |= {*product(*map(lambda p: range(min(p), max(p) + 1), zip(*c)))}

nrocks = len(rocks)
maxy = max(map(lambda i: i[1], rocks))
print(len(run(rocks, lambda y, _: y <= maxy, lambda y: True)) - nrocks)
print(len(run(rocks, lambda _, r: (500, 0) not in r, lambda y: y <= maxy)) - nrocks)

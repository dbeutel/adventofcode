import itertools
import math


def ggt(a, b):
    if a == 0:
        return abs(b)
    if b == 0:
        return abs(a)
    a, b = b, a % b
    while b != 0:
        a, b = b, a % b
    return abs(a)


def angle(x, y):
    """Measured clockwise from (0, -1)"""
    return math.atan2(x, -y) % (2 * math.pi)


asteroids = set()
with open("input10.txt", "r") as f:
    for y, line in enumerate(f.readlines()):
        asteroids = asteroids.union(
            [(x, y) for x, c in enumerate(line.strip()) if c == "#"]
        )


res = {}
for a, b in itertools.combinations(asteroids, 2):
    mx = b[0] - a[0]
    my = b[1] - a[1]
    divisor = ggt(mx, my)
    mx, my = mx // divisor, my // divisor
    test = (a[0] + mx, a[1] + my)
    insight = True
    while test != b:
        if test in asteroids:
            insight = False
            break
        test = (test[0] + mx, test[1] + my)
    if insight:
        res.setdefault(a, []).append(b)
        res.setdefault(b, []).append(a)

station = max(res, key=lambda k: len(res[k]))
print(len(res[station]))

angles = [angle(x - station[0], y - station[1]) for x, y in res[station]]
angle200 = sorted(angles)[199]
twohundredth = res[station][angles.index(angle200)]
print(twohundredth[0] * 100 + twohundredth[1])

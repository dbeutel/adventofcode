import functools
import itertools
import re

import numpy as np


def gcd(a, b, *c):
    if c == ():
        if a == 0:
            return abs(b)
        if b == 0:
            return abs(a)
        a, b = b, a % b
        while b != 0:
            a, b = b, a % b
        return abs(a)
    return gcd(a, gcd(b, *c))


def lcm(a, b, *c):
    if c == ():
        if a == b == 0:
            return 0
        return abs(a * b) // gcd(a, b)
    return lcm(a, lcm(b, *c))


def update_velocity(pa, va, pb, vb):
    if pa > pb:
        return va - 1, vb + 1
    if pa < pb:
        return va + 1, vb - 1
    return va, vb


def step(pos, vel):
    # update velocities
    for (pa, va), (pb, vb) in itertools.combinations(zip(pos, vel), 2):
        for i in range(len(pa)):
            va[i], vb[i] = update_velocity(pa[i], va[i], pb[i], vb[i])
    # update positions
    pos += vel
    return pos, vel


def run(pos, vel):
    pos = pos.copy()
    vel = vel.copy()
    yield pos, vel
    while True:
        pos, vel = step(pos, vel)
        yield pos, vel


def runsingle(pos, vel):
    pos = pos.copy()
    vel = vel.copy()
    yield pos, vel
    while True:
        for i, j in itertools.combinations(range(len(pos)), 2):
            vel[i], vel[j] = update_velocity(pos[i], vel[i], pos[j], vel[j])
        pos = [p + v for p, v in zip(pos, vel)]
        yield pos, vel


pos = []
vel = []
with open("input12.txt", "r") as f:
    for line in f.readlines():
        pos.append([int(i) for i in re.findall("-?\d+", line)])
        vel.append([0, 0, 0])
pos = np.array(pos)
vel = np.array(vel)
posnew, velnew = next(x for i, x in enumerate(iter(run(pos, vel))) if i == 10)
print(np.sum(np.sum(np.abs(posnew), axis=1) * np.sum(np.abs(velnew), axis=1)))

pos_t = map(list, zip(*pos))
vel_t = map(list, zip(*vel))
res = [0, 0, 0]
for i, (singlepos, singlevel) in enumerate(zip(pos_t, vel_t)):
    g = iter(runsingle(singlepos, singlevel))
    next(g)
    j = 1
    while True:
        p, v = next(g)
        if p == singlepos and v == singlevel:
            res[i] = j
            break
        j += 1

print(lcm(*res))

import re


def parsereq(line):
    x = [*map(int, re.findall("[0-9]+", line))]
    return [[x[1], 0, 0, 0], [x[2], 0, 0, 0], [x[3], x[4], 0, 0], [x[5], 0, x[6], 0]]


def divup(x, y):
    if x == y == 0:
        return 0
    return x // y + (x % y > 0)


def schedule(idx, time, res, bots, req, maxbots):
    if bots[max(idx - 1, 0)] == 0 or (maxbots[idx] > 0 and bots[idx] >= maxbots[idx]):
        return time + 1
    return max(0, *map(lambda x: divup(x[0] - x[1], x[2]), zip(req, res, bots))) + 1


def build(idx, wait, res, bots, spend):
    return (
        [*map(lambda x: x[0] + x[1] * wait - x[2], zip(res, bots, spend))],
        [b + (i == idx) for i, b in enumerate(bots)],
    )


def run(reqs, time=32, res=None, bots=None, maxbots=None, best=0):
    bots = [1, 0, 0, 0] if bots is None else bots
    res = [0] * 4 if res is None else res
    maxbots = [*map(max, zip(*reqs))] if maxbots is None else maxbots
    if res[3] + time * bots[3] + time * (time - 1) // 2 < best:
        return best
    best = max(best, res[3] + time * bots[3])
    if time <= 0:
        return best
    for i, req in enumerate(reqs):
        if (wait := schedule(i, time, res, bots, req, maxbots)) < time:
            tmp = build(i, wait, res, bots, req)
            best = max(best, run(reqs, time - wait, *tmp, maxbots, best))
    return best


bps = [*map(parsereq, open("input19.txt"))]
print(sum(map(lambda i: (i[0] + 1) * run(i[1], 24), enumerate(bps))))
print(run(bps[0]) * run(bps[1]) * run(bps[2]))

def adjacent(a, start=True):
    """
    All neighbours of a position
    """
    *xs, x = a
    if not xs:
        res = {(x - 1,), (x,), (x + 1,)}
        if start:
            res.discard(a)
        return res
    res = set()
    for s in adjacent(xs, False):
        res.add(s + (x - 1,))
        res.add(s + (x,))
        res.add(s + (x + 1,))
    if start:
        res.discard(a)
    return res


def cycle(active):
    neighbours = {}
    for a in active:
        for n in adjacent(a):
            neighbours[n] = neighbours.get(n, 0) + 1
    res = set()
    for k, v in neighbours.items():
        if k in active:
            if v in (2, 3):
                res.add(k)
        else:
            if v == 3:
                res.add(k)
    return res


input = set()
with open("input17.txt", "r") as f:
    for x, line in enumerate(f.readlines()):
        for y, c in enumerate(line.strip()):
            if c == "#":
                input.add((x, y, 0))

active = input
for _ in range(6):
    active = cycle(active)
print(len(active))

active = {i + (0,) for i in input}
for _ in range(6):
    active = cycle(active)
print(len(active))

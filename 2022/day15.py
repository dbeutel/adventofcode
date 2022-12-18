import re

with open("input15.txt") as fobj:
    pos = [[*map(int, re.findall("-?[0-9]+", line))] for line in fobj]


def search(pos, y):
    # Relatively simple but slow for part 1
    res = set()
    beacons = set()
    for sx, sy, bx, by in pos:
        if by == y:
            beacons.add(bx)
        mdist = abs(sx - bx) + abs(sy - by) - abs(sy - y)
        res.update(range(-mdist + sx, mdist + sx + 1))
    return res - beacons


def to_uv(x, y):
    return x + y, y - x


def to_xy(u, v, r=0):
    u += 0 if (u + v) % 2 == 0 else r
    return (u - v) // 2, (u + v) // 2


def divide_and_conquer(pos, size=4_000_000, area=None):
    # Not so simple but fast
    u, v, du, dv = (0, -size, 2 * size + 1, 2 * size + 1) if area is None else area
    if du <= 0 or dv <= 0 or ((u + v) % 2 == 1 and du <= 1 and dv <= 1):
        return
    ymin, ymax = to_xy(u, v, 1)[1], to_xy(u + du - 1, v + dv - 1, 1)[1]
    xmin, xmax = to_xy(u, v + dv - 1, 1)[0], to_xy(u + du - 1, v, -1)[0]
    if ymin > size or ymax < 0 or xmin > size or xmax < 0:
        return
    if pos == []:
        x, y = to_xy(u, v)
        return x * size + y
    sx, sy, bx, by = pos[0]
    d = abs(sx - bx) + abs(sy - by)
    pu, pv = to_uv(sx, sy - d)
    qu, qv = pu + 2 * d + 1, pv + 2 * d + 1
    for area in [
        (u, v, min(du, qu - u), min(dv, pv - v)),
        (max(u, qu), v, min(du, du - (qu - u)), min(dv, qv - v)),
        (max(u, pu), max(v, qv), min(du, du - (pu - u)), min(dv, dv - (qv - v))),
        (u, max(v, pv), min(du, pu - u), min(dv, dv - (pv - v))),
    ]:
        if (res := divide_and_conquer(pos[1:], size, area)) is not None:
            return res
    return


print(len(search(pos, 2_000_000)))
print(divide_and_conquer(pos, 4_000_000))

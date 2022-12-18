def surface(cubes):
    s = set()
    for x, y, z in cubes:
        x, y, z = 2 * x, 2 * y, 2 * z
        for d in [-1, 1]:
            s.symmetric_difference_update({(x + d, y, z), (x, y + d, z), (x, y, z + d)})
    return len(s)


def steam(lava, maxval):
    steam = set()
    check = {(-1, -1, -1)}
    while check:
        x, y, z = cube = check.pop()
        if cube in steam or cube in lava or -2 in cube or maxval + 2 in cube:
            continue
        steam.add(cube)
        for d in [1, -1]:
            check |= {(x + d, y, z), (x, y + d, z), (x, y, z + d)}
    return steam


with open("input18.txt") as fobj:
    lava = {(*map(int, line.split(",")),) for line in fobj}
print(surface(lava))
maxval = max(map(max, lava))
print(surface(steam(lava, maxval)) - 6 * (maxval + 3) ** 2)

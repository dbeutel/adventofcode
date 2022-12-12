grid = {}
with open("input12.txt") as fobj:
    for i, line in enumerate(fobj):
        for j, c in enumerate(line.strip()):
            if c == "S":
                check = {j - i * 1j}
                grid[j - i * 1j] = 1
            elif c == "E":
                goal = j - i * 1j
                grid[j - i * 1j] = 26
            else:
                grid[j - i * 1j] = ord(c) - 96


def pathlengths(grid, check):
    dists = {pos: 0 for pos in check}
    while check:
        pos = check.pop()
        dist = dists[pos]
        for i in range(4):
            nextpos = pos + 1j**i
            try:
                nextval = grid[nextpos]
            except KeyError:
                continue
            if nextval <= grid[pos] + 1 and dists.get(nextpos, dist + 2) > dist + 1:
                dists[nextpos] = dist + 1
                check.add(nextpos)
    return dists


print(pathlengths(grid, check)[goal])
check = {pos for pos, val in grid.items() if val == 1}
print(pathlengths(grid, check)[goal])

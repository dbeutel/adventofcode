import bisect

# Commented lines are for the backwards search, which visits fewer nodes for the typical
# input from Advent of Code, but the heuristics makes it quite slow in part 2.


def heuristics(z, goal):
    return min(abs((z - g).real) + abs((z - g).imag) for g in goal)


def pathlength(grid, check, goal):
    dists = {pos: 0 for pos in check}
    visited = set()
    while check:
        pos = check.pop(0)
        dist = dists.pop(pos)
        if pos in goal:
            return dist
        visited.add(pos)
        for i in range(4):
            npos = pos + 1j**i
            if (
                npos not in visited
                and grid.get(npos, grid[pos] + 2) <= grid[pos] + 1
                # and grid.get(npos, grid[pos] - 2) >= grid[pos] - 1
                and dists.get(npos, dist + 2) > dist + 1
            ):
                if npos in check:
                    check.remove(npos)
                dists[npos] = dist + 1
                bisect.insort(check, npos, key=lambda x: dists[x] + heuristics(x, goal))


grid = {}
with open("input12.txt") as fobj:
    for row, line in enumerate(fobj):
        for col, char in enumerate(line.strip()):
            if char == "S":
                start = col - row * 1j
                grid[col - row * 1j] = 1
            elif char == "E":
                end = col - row * 1j
                grid[col - row * 1j] = 26
            else:
                grid[col - row * 1j] = ord(char) - 96


print(pathlength(grid, [start], (end,)))
# print(pathlength(grid, [end], (start,)))
print(pathlength(grid, [pos for pos, val in grid.items() if val == 1], (end,)))
# print(pathlength(grid, [end], tuple(pos for pos, val in grid.items() if val == 1)))

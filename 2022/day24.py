def run(blizzards, valid, nr, nc, goal):
    n = 0
    while goal not in valid:
        n += 1
        valid = {
            (r + dr, c + dc)
            for r, c in valid
            for dr, dc in [*DIRS.values()] + [(0, 0)]
            if (0 <= r + dr < nr and 0 <= c + dc < nc)
            or (r + dr, c + dc) == (-1, 0)
            or (r + dr, c + dc) == (nr, nc - 1)
        }
        nblizzards = {}
        for (r, c), blizzard in blizzards.items():
            for dr, dc in blizzard:
                nblizzards.setdefault(((r + dr) % nr, (c + dc) % nc), []).append(
                    (dr, dc)
                )
        blizzards = nblizzards
        valid -= set(blizzards)
    return n, blizzards


DIRS = {"<": (0, -1), ">": (0, 1), "^": (-1, 0), "v": (1, 0)}
blizzards = {}
with open("input24.txt") as fobj:
    next(fobj)
    for row, line in enumerate(fobj):
        if line.startswith("##"):
            nr = row
            nc = len(line) - 3
            break
        for col, char in enumerate(line[1:-2]):
            if char in DIRS:
                blizzards[(row, col)] = [DIRS[char]]

acc, blizzards = run(blizzards, {(-1, 0)}, nr, nc, (nr, nc - 1))
print(acc)
n, blizzards = run(blizzards, {(nr, nc - 1)}, nr, nc, (-1, 0))
acc += n
n, blizzards = run(blizzards, {(-1, 0)}, nr, nc, (nr, nc - 1))
print(acc + n)

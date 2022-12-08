with open("input08.txt") as fobj:
    forest = [list(map(int, line.strip())) for line in fobj]


def visible(grid, pos, direction, maxheight=9, update=True):
    minheight = -1
    res = set()
    i, j = pos[0] + direction[0], pos[1] + direction[1]
    while -1 not in (i, j) and len(grid) not in (i, j):
        height = grid[i][j]
        if height > minheight:
            res.add((i, j))
            minheight = height if update else minheight
        if height >= maxheight:
            break
        i, j = i + direction[0], j + direction[1]
    return res


res = set()
length = len(forest)
for i, _ in enumerate(forest):
    res.update(visible(forest, (-1, i), (1, 0)))
    res.update(visible(forest, (length, i), (-1, 0)))
    res.update(visible(forest, (i, -1), (0, 1)))
    res.update(visible(forest, (i, length), (0, -1)))
print(len(res))

maxscore = -1
for i, line in enumerate(forest):
    for j, maxheight in enumerate(line):
        score = 1
        for direction in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            score *= len(visible(forest, (i, j), direction, maxheight, False))
        maxscore = max(maxscore, score)
print(maxscore)

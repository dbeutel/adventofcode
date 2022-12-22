import re


def step(pos, facing, rows, cols):
    r, c = pos
    if facing in (0, 2):
        c += (-1) ** (facing // 2)
        c = (c - rows[r][0]) % rows[r][1] + rows[r][0]
    else:
        r += (-1) ** ((facing - 1) // 2)
        r = (r - cols[c][0]) % cols[c][1] + cols[c][0]
    return (r, c), facing


def stepcube(pos, facing):
    r, c = pos
    if facing in (0, 2):
        c += (-1) ** (facing // 2)
    else:
        r += (-1) ** ((facing - 1) // 2)
    if r == -1 and 50 <= c < 100:
        r, c, facing = 100 + c, 0, 0
    elif r == -1 and 100 <= c < 150:
        r, c, facing = 199, c - 100, facing
    elif r == 50 and 100 <= c < 150:
        r, c, facing = c - 50, 99, 2
    elif r == 99 and 0 <= c < 50:
        r, c, facing = c + 50, 50, 0
    elif r == 150 and 50 <= c < 100:
        r, c, facing = c + 100, 49, 2
    elif r == 200 and 0 <= c < 50:
        r, c, facing = 0, c + 100, facing
    elif c == -1 and 100 <= r < 150:
        r, c, facing = 149 - r, 50, 0
    elif c == -1 and 150 <= r < 200:
        r, c, facing = 0, r - 100, 1
    elif c == 49 and 0 <= r < 50:
        r, c, facing = 149 - r, 0, 0
    elif c == 49 and 50 <= r < 100:
        r, c, facing = 100, r - 50, 1
    elif c == 50 and 150 <= r < 200:
        r, c, facing = 149, r - 100, 3
    elif c == 100 and 50 <= r < 100:
        r, c, facing = 49, r + 50, 3
    elif c == 100 and 100 <= r < 150:
        r, c, facing = 149 - r, 149, 2
    elif c == 150 and 0 <= r < 50:
        r, c, facing = 149 - r, 99, 2
    return (r, c), facing


rows = []
cols = []
walls = set()
with open("input22.txt") as fobj:
    for r, line in enumerate(fobj):
        line = line[:-1]
        if line == "":
            break
        cols = cols + [None] * (len(line) - len(cols))
        start = len(line) - len(line.lstrip())
        stop = len(line.rstrip())
        rows.append((start, stop - start))
        for c in range(start, stop):
            cols[c] = (r, 1) if (col := cols[c]) is None else (col[0], col[1] + 1)
            if line[c] == "#":
                walls.add((r, c))
    commands = re.findall("[0-9]+|L|R", next(fobj))


def run(commands, func):
    pos = (0, rows[0][0])
    facing = 0
    for command in commands:
        if command == "R":
            facing = (facing + 1) % 4
        elif command == "L":
            facing = (facing - 1) % 4
        else:
            for _ in range(int(command)):
                npos, nfacing = func(pos, facing)
                if npos in walls:
                    break
                pos, facing = npos, nfacing
    return (pos[0] + 1) * 1000 + (pos[1] + 1) * 4 + facing


print(run(commands, lambda p, f: step(p, f, rows, cols)))
print(run(commands, stepcube))

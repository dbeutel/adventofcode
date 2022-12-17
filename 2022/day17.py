def check(lines, x, y, shape):
    for yy, row in enumerate(shape):
        if ({-1, 7} | lines.get(y + yy, set())) & {x + xx for xx in row}:
            return False
    return True


commands = [1 if c == ">" else -1 for c in open("input17.txt").read().strip()]
ncom = len(commands)
shapes = [
    [{0, 1, 2, 3}],
    [{1}, {0, 1, 2}, {1}],
    [{0, 1, 2}, {2}, {2}],
    [{0}, {0}, {0}, {0}],
    [{0, 1}, {0, 1}],
]

NRUNS = 1_000_000_000_000
icom = 0
tops = [0]
lines = {}
cache = {}
for i in range(NRUNS):
    top = tops[i]
    if i == 2022:
        print(top)
    ishape = i % 5
    if (c := cache.get((ishape, icom), (0,))) != (0,) and i - c[0] == c[1]:
        rep, gap = (NRUNS - c[0]) // c[1], (NRUNS - c[0]) % c[1]
        print(rep * (tops[i] - tops[c[0]]) + tops[c[0] + gap])
        break
    else:
        cache[(ishape, icom)] = i, i - c[0]
    shape = shapes[ishape]
    x, y = 2, top + 4
    while True:
        d = commands[icom]
        icom = (icom + 1) % ncom
        if check(lines, x + d, y, shape):
            x += d
        if check(lines, x, y - 1, shape) and y > 1:
            y -= 1
        else:
            for yy, row in enumerate(shape):
                lines.setdefault(y + yy, set()).update({x + xx for xx in row})
            tops.append(max(lines))
            break

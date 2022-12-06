from intcode import Intcode


def run(code, white):
    painted = set()
    x = y = dx = 0
    dy = 1
    ret = 1
    while ret != 0:
        code.input = 1 if (x, y) in white else 0
        ret = code.run()
        out = code.flush()
        while len(out) > 1:
            color, dir, *out = out
            if color:
                white.add((x, y))
            else:
                white.discard((x, y))
            painted.add((x, y))
            if dir:
                dx, dy = dy, -dx
            else:
                dx, dy = -dy, dx
            x, y = x + dx, y + dy
    return len(painted)


with open("input11.txt", "r") as f:
    tape = [int(i) for i in f.read().split(",")]

print(run(Intcode(tape), set()))

white = {(0, 0)}
run(Intcode(tape), white)

xmax = ymax = -999
xmin = ymin = 999
for x, y in white:
    xmin = min(xmin, x)
    ymin = min(ymin, y)
    xmax = max(xmax, x)
    ymax = max(ymax, y)

picture = [[" "] * (xmax - xmin + 1) for _ in range(ymax - ymin + 1)]
for x, y in white:
    picture[y - ymin][x - xmin] = "#"

for line in picture[::-1]:
    print("".join(line))

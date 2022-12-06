import functools

from intcode import Intcode


def move(x, y, dir):
    if dir == 1:
        return x, y + 1
    elif dir == 2:
        return x, y - 1
    elif dir == 3:
        return x - 1, y
    elif dir == 4:
        return x + 1, y


def opposite(x):
    if x == 1:
        return 2
    elif x == 2:
        return 1
    elif x == 3:
        return 4
    elif x == 4:
        return 3
    # return None intentional


possibilities = [(1, 3, 4), (2, 3, 4), (1, 2, 3), (1, 2, 4)]


class Step:
    def __init__(self, pos, dir, prev, oxygen=False):
        self.prev = prev
        self.x, self.y = pos
        self.dir = dir
        self.oxygen = oxygen

    def findnext(self, code):
        self.cont = []
        if self.dir is None:
            possible = (1, 2, 3, 4)
        else:
            possible = possibilities[self.dir - 1]
        for d in possible:
            code.input = d
            code.run()
            res = code.flush()[0]
            if res in (1, 2):
                a, b = move(self.x, self.y, d)
                s = Step((a, b), d, self, res == 2)
                s.findnext(code)
                self.cont.append(s)
                code.input = opposite(d)
                code.run()
                code.flush()

    def layout(self, dct):
        if self.oxygen:
            dct[(self.x, self.y)] = "x"
        elif self.prev is None:
            dct[(self.x, self.y)] = "o"
        else:
            dct[(self.x, self.y)] = "."
        for d in range(1, 5):
            if d != opposite(self.dir):
                a, b = move(self.x, self.y, d)
                dct[(a, b)] = "#"
        for s in self.cont:
            s.layout(dct)

    def changeroot(self, prev=None):
        prevprev, self.prev = self.prev, prev
        if prev is not None:
            self.cont.remove(prev)
        if prevprev is not None:
            self.cont.append(prevprev)
            prevprev.changeroot(self)


def findoxygen(step):
    n = 0
    backtrace = False
    while not step.oxygen:
        if backtrace:
            nextstep = step.prev
            i = nextstep.cont.index(step)
            if i == len(nextstep.cont) - 1:  # continue backtracking
                n -= 1
            else:  # Swith to next branch
                backtrace = False
                nextstep = nextstep.cont[i + 1]
        else:
            if step.cont:  # continue
                n += 1
                nextstep = step.cont[0]
            else:  # dead end
                n -= 1
                backtrace = True
                nextstep = step.prev
        step = nextstep
    return n, step


def maxdepth(step):
    n = maxd = 0
    backtrace = False
    while True:
        if backtrace:
            if step.prev is None:
                break
            nextstep = step.prev
            i = nextstep.cont.index(step)
            if i == len(nextstep.cont) - 1:  # continue backtracking
                n -= 1
            else:  # Swith to next branch
                backtrace = False
                nextstep = nextstep.cont[i + 1]
        else:
            if step.cont:  # continue
                n += 1
                maxd = max(maxd, n)
                nextstep = step.cont[0]
            else:  # dead end
                n -= 1
                backtrace = True
                nextstep = step.prev
        step = nextstep
    return maxd


with open("input15.txt", "r") as f:
    tape = [int(i) for i in f.read().split(",")]


code = Intcode(tape)
root = Step((0, 0), None, None)
root.findnext(code)

labyrinth = {}
root.layout(labyrinth)
xmin = xmax = ymin = ymax = 0
for x, y in labyrinth:
    xmin, xmax = min(xmin, x), max(xmax, x)
    ymin, ymax = min(ymin, y), max(ymax, y)


picture = [[" "] * (xmax - xmin + 1) for _ in range(ymax - ymin + 1)]
for (x, y), c in labyrinth.items():
    picture[y - ymin][x - xmin] = c

for line in picture[::-1]:
    print("".join(line))

distance, o2 = findoxygen(root)
print(distance)
o2.changeroot()
print(maxdepth(o2))

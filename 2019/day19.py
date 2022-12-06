import itertools

from intcode import Intcode

with open("input19.txt", "r") as f:
    tape = [int(i) for i in f.read().split(",")]

total = 0
for y, x in itertools.product(range(50), repeat=2):
    c = Intcode(tape, [x, y])
    c.run()
    res = c.flush()[0]
    if res == 1:
        total += 1
        print("#", end="")
    else:
        print(".", end="")
    if x == 49:
        print()
print(total)


def checkspace(a):
    firstx = 0
    for y in range(99, a):
        for x in range(firstx, a):
            c = Intcode(tape, [x, y])
            c.run()
            res = c.flush()[0]
            if res:
                firstx = x
                c = Intcode(tape, [x + 99, y - 99])
                c.run()
                if c.flush()[0]:
                    return x * 10000 + (y - 99)
                break


print(checkspace(10000))

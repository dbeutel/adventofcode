from intcode import Intcode

with open("input23.txt", "r") as f:
    tape = [int(i) for i in f.read().split(",")]


def run(tape):
    nat = [0, 0]
    lasty = firsty = None
    cs = [Intcode(tape, i) for i in range(50)]
    i = 0
    idle = 0
    # A happy merry go round scheduler
    while True:
        if not cs[i].input:
            idle += 1
            cs[i].input = -1
        else:
            idle = 0
        cs[i].run()
        out = cs[i].flush()
        while len(out) > 2:
            d, x, y, *out = out
            if d == 255:
                firsty = y if firsty is None else firsty
                nat = [x, y]
            else:
                cs[d].input = [x, y]
        if idle > 50:  # just to be safe it's really idle :)
            if y == lasty:
                return firsty, lasty
            lasty = y
            cs[0].input = nat
            i = 0
        else:
            i = (i + 1) % 50


res = run(tape)
print(res[0])
print(res[1])

def step(d):
    return (max(min(d.real, 1), -1) + 1j * max(min(d.imag, 1), -1)) * int(abs(d) >= 2)


def update(s):
    rope[0] += s
    for i, (x, y) in enumerate(zip(rope, rope[1:])):
        rope[i + 1] = y + step(x - y)
    return rope[-1]


with open("input09.txt", "r") as fobj:
    steps = [i for line in fobj for i in [1j ** "RULD".index(line[0])] * int(line[2:])]

for n in (2, 10):
    rope = [0] * n
    print(len(set(map(update, steps))))

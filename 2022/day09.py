def step(d):
    return (max(min(d.real, 1), -1) + 1j * max(min(d.imag, 1), -1)) * int(abs(d) >= 2)


def update(s):
    rope[0] += s
    rope[1:] = map(lambda x: x[1] + step(x[0] - x[1]), zip(rope, rope[1:]))
    return rope[-1]


with open("input09.txt", "r") as fobj:
    steps = [i for line in fobj for i in [1j ** "RULD".index(line[0])] * int(line[2:])]

for n in (2, 10):
    rope = [0] * n
    print(len(set(map(update, steps))))

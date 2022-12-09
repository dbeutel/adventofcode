directions = {"U": (0, 1), "R": (1, 0), "D": (0, -1), "L": (-1, 0)}


def sign(x):
    if x > 0:
        return 1
    if x < 0:
        return -1
    return 0


def step(head, tail):
    x = head[0] - tail[0]
    y = head[1] - tail[1]
    if x in (-1, 0, 1) and y in (-1, 0, 1):
        return 0, 0
    return sign(x), sign(y)


def simulation(n, fobj):
    rope = [(0, 0) for _ in range(n)]
    visited = {rope[-1]}
    for line in fobj:
        key, steps = line.split()
        for _ in range(int(steps)):
            rope[0] = tuple(map(sum, zip(rope[0], directions[key])))
            for i in range(1, len(rope)):
                rope[i] = tuple(map(sum, zip(rope[i], step(rope[i - 1], rope[i]))))
            visited.add(rope[-1])
    print(len(visited))


for n in (2, 10):
    with open("input09.txt", "r") as fobj:
        simulation(n, fobj)

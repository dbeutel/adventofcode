def step(elves, n):
    proposed = {}
    dirs = [1j, -1j, -1, 1]
    for elf in elves:
        if not (
            {
                elf + 1,
                elf + 1 + 1j,
                elf + 1j,
                elf - 1 + 1j,
                elf - 1,
                elf - 1 - 1j,
                elf - 1j,
                elf + 1 - 1j,
            }
            & elves
        ):
            continue
        for i in range(4):
            d = dirs[(i + n) % 4]
            if not ({elf + d, elf + d + 1j * d, elf + d - 1j * d} & elves):
                proposed.setdefault(elf + d, []).append(elf)
                break
    if not proposed:
        return False
    for key, val in proposed.items():
        if len(val) != 1:
            continue
        elves.remove(val.pop())
        elves.add(key)
    return True


elves = set()
with open("input23.txt") as fobj:
    for my, line in enumerate(fobj):
        for x, c in enumerate(line.strip()):
            if c == "#":
                elves.add(x - 1j * my)

n = 0
while step(elves, n):
    if n == 9:
        lo = [*map(lambda i: i.real, elves)]
        la = [*map(lambda i: i.imag, elves)]
        print(int((max(la) - min(la) + 1) * (max(la) - min(la) + 1) - len(elves)))
    n += 1
print(n + 1)

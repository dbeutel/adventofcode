cuporder = [int(i) for i in '716892543']
# cuporder = [int(i) for i in '389125467']

def parsecups(cuporder, maxvalue):
    cups = [0] + list(range(2, maxvalue + 1)) + [1]
    if not cuporder:
        return 1, cups
    cups[-1] = prev = cuporder[0]
    for i in cuporder[1:]:
        cups[prev] = i
        prev = i
    cups[prev] = len(cuporder) + 1 if len(cuporder) < maxvalue else cuporder[0]
    return cuporder[0], cups


def undocupsparse(cups, start):
    res = [start]
    i = cups[start]
    while i != start:
        res.append(i)
        i = cups[i]
    return res


def step(cups, current, wrap):
    pick1 = cups[current]
    pick2 = cups[pick1]
    pick3 = cups[pick2]
    dest = (current - 2) % wrap + 1
    while dest in (pick1, pick2, pick3):
        dest = (dest - 2) % wrap + 1
    cups[current] = cups[pick3]
    cups[pick3] = cups[dest]
    cups[dest] = pick1


current, cups = parsecups(cuporder, 9)
for _ in range(100):
    step(cups, current, 9)
    current = cups[current]

print(''.join([str(i) for i in undocupsparse(cups, 1)[1:]]))

current, cups = parsecups(cuporder, 1_000_000)
for _ in range(10_000_000):
    step(cups, current, 1_000_000)
    current = cups[current]

print(cups[1] * cups[cups[1]])

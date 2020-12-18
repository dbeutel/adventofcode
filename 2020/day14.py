import functools
import re


def apply1(mask, val):
    return (val & int(mask.replace('X', '1'), 2)) | int(mask.replace('X', '0'), 2)


def apply2(mask, val):
    val = val | int(mask.replace('X', '1'), 2) # Sets all X's
    posx = [35 - i for i, c in enumerate(mask) if c == 'X'][::-1]
    res = []
    for x in range(2 ** len(posx)):
        newval = val
        for i, pos in enumerate(posx):
            if not (x & (1 << i)):
                newval = newval & ~(1 << pos) # Unset position
        res.append(newval)
    return res


with open('input14.txt', 'r') as f:
    lines = f.readlines()

p = re.compile('((mem)\[([0-9]*)\]|mask) = ([X0-9]*)')

memory = {}
mask = 'X' * 36
for line in lines:
    a = p.search(line)
    if a.group(1) == 'mask':
        mask = a.group(4)
    elif a.group(2) == 'mem':
        memory[int(a.group(3))] = apply1(mask, int(a.group(4)))
print(functools.reduce(lambda x, y: x + y, memory.values()))

memory = {}
mask = '0' * 36
for line in lines:
    a = p.search(line)
    if a.group(1) == 'mask':
        mask = a.group(4)
    elif a.group(2) == 'mem':
        for addr in apply2(mask, int(a.group(3))):
            memory[addr] = int(a.group(4))
print(functools.reduce(lambda x, y: x + y, memory.values()))

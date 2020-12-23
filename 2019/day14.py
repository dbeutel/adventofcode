import math
reactions = {}

def namequantity(line):
    a, b = line.strip().split(' ')
    return b, int(a)


def getleftovers(d, key, m):
    if key in d:
        if d[key] <= m:
            return m - d.pop(key)
        else:
            d[key] -= m
            return 0
    return m


with open('input14.txt', 'r') as f:
    for line in f.readlines():
        educts, product = line.split(' => ')
        p, n = namequantity(product)
        dct = {}
        for i in educts.split(','):
            q, m = namequantity(i)
            dct[q] = m
        reactions[p] = (n, dct)


def howmuchore(requires):
    leftovers = {}
    ore = 0
    while requires:
        p, m = requires.popitem()
        m = getleftovers(leftovers, p, m)
        if m == 0:
            continue
        n, educts = reactions[p]
        factor = (m - 1) // n + 1
        if factor * n != m:
            leftovers[p] = factor * n - m
        for e, i in educts.items():
            if e == 'ORE':
                ore += factor * i
                continue
            requires[e] = requires.setdefault(e, 0) + factor * i
    return ore

print(howmuchore({'FUEL': 1}))

# Really dumb search algorithm:
maxore = 1e12
fuel = 1
n = -1
test = howmuchore({'FUEL': fuel})
while test < maxore:
    n += 1
    fuel *= 10
    test = howmuchore({'FUEL': fuel})


sub = fuel / 10
for _ in range(n, -1, -1):
    for _ in range(11):
        if howmuchore({'FUEL': fuel}) < maxore:
            break
        fuel -= sub
    fuel += sub
    sub /= 10

print(int(fuel) - 1)

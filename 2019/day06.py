orbits = {}
with open('input06.txt', 'r') as f:
    for line in f.readlines():
        a, b = line.strip().split(')')
        orbits.setdefault(a, set()).add(b)

def countorbits(orbits, key, cache=None):
    if cache is None:
        cache = {}
    if key in cache:
        return cache(key)
    indirect = 0
    current = orbits.get(key, set())
    for i in current:
        indirect += sum(countorbits(orbits, i, cache))
    direct = len(current)
    cache[key] = (direct, indirect)
    return direct, indirect

cache = {}
countorbits(orbits, 'COM', cache)
print(sum([sum(i) for i in cache.values()]))

def find(goal, orbits, key):
    if key == goal:
        return [goal]
    for i in orbits.get(key, set()):
        found = find(goal, orbits, i)
        if found:
            found.append(key)
            return found
    return []

you = find('YOU', orbits, 'COM')
san = find('SAN', orbits, 'COM')
while you[-1] == san[-1]:
    y = you.pop()
    s = san.pop()

print(len(you) + len(san) - 2)

prio = 0
with open("input03.txt", "r") as fobj:
    for line in fobj:
        line = line.strip()
        item = (set(line[: len(line) // 2]) & set(line[len(line) // 2 :])).pop()
        prio += ord(item) - (38 if item.isupper() else 96)
print(prio)

prio = 0
with open("input03.txt", "r") as fobj:
    for line in fobj:
        item = (set(line.strip()) & set(next(fobj)) & set(next(fobj))).pop()
        prio += ord(item) - (38 if item.isupper() else 96)
print(prio)

prio = 0
with open("input03.txt", "r") as fobj:
    for line in fobj:
        line = line.strip()
        item = next(iter(set(line[: len(line) // 2]) & set(line[len(line) // 2 :])))
        prio += ord(item) - (38 if item.isupper() else 96)
print(prio)

prio = 0
with open("input03.txt", "r") as fobj:
    for line in fobj:
        item = next(iter(set(line.strip()) & set(next(fobj)) & set(next(fobj))))
        prio += ord(item) - (38 if item.isupper() else 96)
print(prio)

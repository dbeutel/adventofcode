with open('input10.txt', 'r') as f:
    adapters = sorted([int(line) for line in f.readlines()])
    adapters = [0] + adapters + [adapters[-1] + 3]

diffs = [x - y for x, y in zip(adapters[1:], adapters[:-1])]
print(diffs.count(1) * diffs.count(3))

paths = [1] * len(adapters)
for i, a in enumerate(adapters[2:]):
    paths[i + 2] = paths[i + 1]
    for j in range(min(i + 1, 2)):
        if a - adapters[i - j] <= 3:
            paths[i + 2] += paths[i - j]
print(paths[-1])

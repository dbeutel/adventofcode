def disk_usage(filesystem, res=None):
    res = [] if res is None else res
    size = 0
    for val in filesystem.values():
        if isinstance(val, int):
            size += val
        else:
            disk_usage(val, res=res)
            size += res[-1]
    res.append(size)
    return res


root = {}
cwd = [root]

with open("input07.txt", "r") as fobj:
    for line in fobj:
        line = line.strip()
        if line == "$ cd ..":
            cwd.pop()
        elif line == "$ cd /":
            cwd = [root]
        elif line.startswith("$ cd "):
            cwd.append(cwd[-1].setdefault(line[5:], {}))
        elif line.startswith("dir "):
            cwd[-1].setdefault(line[4:], {})
        elif line != "$ ls":
            size, name = line.split()
            cwd[-1][name] = int(size)

du = disk_usage(root)
print(sum(i for i in du if i < 100_000))
threshold = du[-1] - 40_000_000
print(min(i for i in du if i > threshold))

def du(dirs, res):
    res.append(sum(v if isinstance(v, int) else du(v, res)[-1] for v in dirs.values()))
    return res


cwd = [root := {}]

with open("input07.txt", "r") as fobj:
    for line in fobj:
        line = line.strip()
        if line == "$ cd ..":
            cwd.pop()
        elif line == "$ cd /":
            cwd = [root]
        elif line.startswith("$ cd "):
            cwd.append(cwd[-1].setdefault(line[5:], {}))
        elif not line.startswith("dir ") and line != "$ ls":
            size, name = line.split()
            cwd[-1][name] = int(size)

res = du(root, [])
print(sum(i for i in res if i < 100_000))
print(min(i for i in res if i > res[-1] - 40_000_000))

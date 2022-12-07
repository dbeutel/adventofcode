def consume(itr):
    try:
        command = next(itr).strip()
    except StopIteration:
        return
    if not command.startswith("$"):
        return
    output = []
    while True:
        try:
            line = next(itr).strip()
        except StopIteration:
            yield command, output
            return
        if line.startswith("$"):
            yield command, output
            command = line
            output = []
        else:
            output.append(line)


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
    for command, output in consume(fobj):
        if command == "$ cd ..":
            cwd.pop()
        elif command == "$ cd /":
            cwd = [root]
        elif command.startswith("$ cd "):
            cwd.append(cwd[-1].setdefault(command[5:], {}))
        else:
            for line in output:
                if line.startswith("dir "):
                    cwd[-1].setdefault(line[4:], {})
                else:
                    size, name = line.split()
                    cwd[-1][name] = int(size)

du = disk_usage(root)
print(sum(i for i in du if i < 100_000))
threshold = du[-1] - 40_000_000
print(min(i for i in du if i > threshold))

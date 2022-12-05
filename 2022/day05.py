import copy
import re

regex = re.compile(r"^move ([0-9]+) from ([0-9]+) to ([0-9]+)$")
stacks = {}

with open("input05.txt", "r") as fobj:
    for line in fobj:
        if line.strip().startswith("["):
            for i, crate in enumerate(line[1::4]):
                if crate != " ":
                    stacks.setdefault(i, []).insert(0, crate)
        elif line == "\n":
            break
        else:
            stacks = {int(key): stacks[i] for i, key in enumerate(line[1::4])}

    stacks_9001 = copy.deepcopy(stacks)
    for line in fobj:
        repeat, origin, dest = map(int, regex.match(line).groups())
        for _ in range(repeat):
            stacks[dest].append(stacks[origin].pop())
        stacks_9001[dest].extend(stacks_9001[origin][-repeat:])
        del stacks_9001[origin][-repeat:]

print("".join(stack[-1] for stack in stacks.values()))
print("".join(stack[-1] for stack in stacks_9001.values()))

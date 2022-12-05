import copy
import re

regex = re.compile(r"^move ([0-9]+) from ([0-9]+) to ([0-9]+)$")
stacks = [[] for _ in range(9)]

with open("input05.txt", "r") as fobj:
    for line in fobj:
        if line == " 1   2   3   4   5   6   7   8   9 \n":
            break
        items = line[1::4]
        for item, stack in zip(items, stacks):
            if item != " ":
                stack.insert(0, item)

    stacks_9001 = copy.deepcopy(stacks)
    next(fobj)
    for line in fobj:
        repeat, origin, dest = (int(i) for i in regex.match(line).groups())
        for _ in range(repeat):
            stacks[dest - 1].append(stacks[origin - 1].pop())
        stacks_9001[dest - 1].extend(stacks_9001[origin - 1][-repeat:])
        del stacks_9001[origin - 1][-repeat:]

print("".join(stack[-1] for stack in stacks))
print("".join(stack[-1] for stack in stacks_9001))

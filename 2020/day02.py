import re

with open("input02.txt", "r") as f:
    lines = f.readlines()

p = re.compile("([0-9]*)-([0-9]*) ([a-z]): ([a-z]*)")
valid = [0, 0]
for line in lines:
    a = p.search(line)
    start = int(a.group(1))
    stop = int(a.group(2))
    q = re.compile(a.group(3))
    if start <= len(re.findall(q, a.group(4))) <= stop:
        valid[0] += 1
    if bool(a.group(4)[start - 1] == a.group(3)) is not bool(
        a.group(4)[stop - 1] == a.group(3)
    ):
        valid[1] += 1
print(valid[0])
print(valid[1])

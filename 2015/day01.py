with open("input01.txt", "r") as f:
    line = f.read()

floor = 0
first = True
for i, c in enumerate(line):
    if c == "(":
        floor += 1
    if c == ")":
        floor -= 1
    if first and floor == -1:
        first = False
        print(f"Part 2: {i + 1}")
print(f"Part 1: {floor}")

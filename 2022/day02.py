values = {j: i % 3 for i, j in enumerate("ABCXYZ")}

with open("input02.txt", "r") as fobj:
    guide = [[values[i] for i in line.strip().split()] for line in fobj]

print(sum(j + 1 + ((j - i + 1) % 3) * 3 for i, j in guide))
print(sum(j * 3 + (i + j - 1) % 3 + 1 for i, j in guide))

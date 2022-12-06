with open("input01.txt", "r") as f:
    lines = [int(line) for line in f.readlines()]

a = []
b = []
nline = len(lines)
for i in range(nline):
    for j in range(i, nline):
        if lines[i] + lines[j] == 2020:
            a.append(lines[i] * lines[j])
        for k in range(j, nline):
            if lines[i] + lines[j] + lines[k] == 2020:
                b.append(lines[i] * lines[j] * lines[k])

print(a[0])
print(b[0])

with open("input06.txt") as fobj:
    line = fobj.read().strip()

def marker(length, line):
    for i in range(length, len(line)):
        if len(set(line[i - length: i])) == length:
            return i
    return -1

print(marker(4, line))
print(marker(14, line))

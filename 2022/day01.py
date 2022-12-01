with open("input01.txt") as fobj:
    food = sorted(
        sum(int(line) for line in elf.split("\n") if line != "")
        for elf in fobj.read().split("\n\n")
    )

print(food[-1])
print(sum(food[-3:]))

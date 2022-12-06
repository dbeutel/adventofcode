with open("input01.txt", "r") as f:
    masses = [int(i) for i in f.readlines()]

print(sum([m // 3 - 2 for m in masses]))

total = 0
for m in masses:
    fuel = m // 3 - 2
    while fuel > 0:
        total += fuel
        fuel = fuel // 3 - 2
print(total)

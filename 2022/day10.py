with open("input10.txt", "r") as fobj:
    reg = [1]
    for line in fobj:
        reg.append(reg[-1])
        if line != "noop\n":
            reg.append(reg[-1] + int(line.split()[1]))
print(sum((c * 40 + 20) * r for c, r in enumerate(reg[19::40])))

screen = "".join("#" if r - 1 <= c % 40 <= r + 1 else " " for c, r in enumerate(reg))
for i in range(6):
    print(screen[i * 40 : (i + 1) * 40])

with open("input04.txt", "r") as fobj:
    pairs = [
        [
            set(range(*(int(j) + i for i, j in enumerate(elf.split("-")))))
            for elf in line.strip().split(",")
        ]
        for line in fobj
    ]

print(sum(1 for a, b in pairs if (a <= b or b <= a)))
print(sum(1 for a, b in pairs if a & b))

prio = lambda item: ord(item) - (38 if item.isupper() else 96)

with open("input03.txt", "r") as fobj:
    print(
        sum(
            prio((set(line[: len(line) // 2]) & set(line[len(line) // 2 :])).pop())
            for line in fobj
        )
    )

with open("input03.txt", "r") as fobj:
    print(
        sum(
            prio((set(line.strip()) & set(next(fobj)) & set(next(fobj))).pop())
            for line in fobj
        )
    )

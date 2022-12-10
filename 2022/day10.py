from itertools import accumulate
from textwrap import fill

with open("input10.txt") as fobj:
    reg = list(
        accumulate(
            map(int, fobj.read().replace("noop", "0").replace("addx", "0").split()),
            initial=1,
        )
    )
print(sum((c * 40 + 20) * r for c, r in enumerate(reg[19::40])))
print(fill("".join("#" if abs(c % 40 - r) < 2 else " " for c, r in enumerate(reg)), 40))

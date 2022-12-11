import copy
import re
from functools import partial, reduce
from operator import add, mul

OPS = {"*": mul, "+": add}


def fullop(a, op, b, x):
    return OPS[op](x if a == "old" else int(a), x if b == "old" else int(b))


def test(mod, a, b, x):
    return a if x % mod == 0 else b


def play(monkeys, nrounds, worry):
    for _ in range(nrounds):
        for monkey in monkeys.values():
            while monkey["items"]:
                item = worry(monkey["op"](monkey["items"].pop(0)))
                monkey["activity"] += 1
                monkeys[test(*monkey["test"], item)]["items"].append(item)


regex = re.compile(
    r"Monkey ([0-9]+):\n"
    r"  Starting items: ([0-9]+(?:, [0-9]+)*)\n"
    r"  Operation: new = (old|[0-9]+) (\+|\*) (old|[0-9]+)\n"
    r"  Test: divisible by ([0-9]+)\n"
    r"    If true: throw to monkey ([0-9]+)\n"
    r"    If false: throw to monkey ([0-9]+)\n"
)
with open("input11.txt") as fobj:
    monkeys = {}
    for match in regex.findall(fobj.read()):
        monkeys[int(match[0])] = {
            "items": list(map(int, match[1].split(","))),
            "op": partial(fullop, *match[2:5]),
            "test": list(map(int, match[5:])),
            "activity": 0,
        }

mnkys = copy.deepcopy(monkeys)  # Superior variable naming...
play(monkeys, 20, lambda x: x // 3)
print(reduce(mul, sorted([m["activity"] for m in monkeys.values()])[-2:]))
play(mnkys, 10_000, lambda x: x % reduce(mul, [m["test"][0] for m in mnkys.values()]))
print(reduce(mul, sorted([m["activity"] for m in mnkys.values()])[-2:]))

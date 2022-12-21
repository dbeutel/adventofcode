from operator import add, floordiv, mul, sub


def getval(dct, key, noupdate):
    if isinstance(val := dct[key], int):
        return val
    res = val[1](getval(dct, val[0], noupdate), getval(dct, val[2], noupdate))
    if key not in noupdate:
        dct[key] = res
    return res


def getnoupdate(dct, key, res=None):
    res = set() if res is None else res
    if key in res:
        return res
    res.add(key)
    for k, v in dct.items():
        if not isinstance(v, int) and k not in res:
            if v[0] == key:
                getnoupdate(monkeys, k, res)
            if v[2] == key:
                getnoupdate(monkeys, k, res)
    return res


def getunknown(dct, key, val, unkowns):
    if isinstance(dct[key], int):
        return val
    a, op, b = dct[key]
    if a in unkowns and b in unkowns:
        raise ValueError(f"two unknows encountered at {key} = {val}")
    if a in unkowns:
        if op == add:
            return getunknown(dct, a, val - dct[b], unkowns)
        if op == sub:
            return getunknown(dct, a, val + dct[b], unkowns)
        if op == mul:
            return getunknown(dct, a, val // dct[b], unkowns)
        if op == floordiv:
            return getunknown(dct, a, val * dct[b], unkowns)
    if b in unkowns:
        if op == add:
            return getunknown(dct, b, val - dct[a], unkowns)
        if op == sub:
            return getunknown(dct, b, dct[a] - val, unkowns)
        if op == mul:
            return getunknown(dct, b, val // dct[a], unkowns)
        if op == floordiv:
            return getunknown(dct, b, dct[a] // val, unkowns)
    raise ValueError(f"no unknown at {key} = {val}")


OPS = {"+": add, "*": mul, "-": sub, "/": floordiv}
monkeys = {}
with open("input21.txt") as fobj:
    for line in fobj:
        name, yells = line.split(":")
        if yells.strip().isdigit():
            monkeys[name] = int(yells)
        else:
            a, op, b = yells.split()
            monkeys[name] = a, OPS[op], b

nup = getnoupdate(monkeys, "humn")
print(getval(monkeys, "root", nup))
a, _, b = monkeys["root"]
monkeys["root"] = a, sub, b
print(getunknown(monkeys, "root", 0, nup)[2])

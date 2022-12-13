from ast import literal_eval
from functools import cmp_to_key
from itertools import zip_longest


def cmp(a, b):
    for x, y in zip_longest(a, b):
        if None in (x, y):
            return 1 - 2 * int(x is None)
        if isinstance(x, int) and isinstance(y, int):
            if x != y:
                return 1 if x > y else -1
        elif (val := cmp(*([i] if isinstance(i, int) else i for i in (x, y)))) != 0:
            return val
    return 0


sig = list(map(literal_eval, open("input13.txt").read().split()))
print(sum(i + 1 for i, (a, b) in enumerate(zip(sig[::2], sig[1::2])) if cmp(a, b) < 0))
sig = sorted(sig + [[[2]], [[6]]], key=cmp_to_key(cmp))
print((sig.index([[2]]) + 1) * (sig.index([[6]]) + 1))

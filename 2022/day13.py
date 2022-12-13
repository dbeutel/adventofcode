from itertools import zip_longest


def compare(a, b):
    for x, y in zip_longest(a, b):
        if None in (x, y):
            return x is None
        if isinstance(x, int) and isinstance(y, int):
            if x > y:
                return False
            if x < y:
                return True
        else:
            x = [x] if isinstance(x, int) else x
            y = [y] if isinstance(y, int) else y
            if (comp := compare(x, y)) is not None:
                return comp
    return None


def quicksort(x):
    if len(x) <= 1:
        return x
    pivot = x[0]
    before = []
    after = []
    for i in x[1:]:
        if compare(i, pivot):
            before.append(i)
        else:
            after.append(i)
    return quicksort(before) + [pivot] + quicksort(after)


sig = [eval(i) for i in open("input13.txt").read().split()]  # too tempting to use eval
print(sum(i + 1 for i, (a, b) in enumerate(zip(sig[::2], sig[1::2])) if compare(a, b)))
sig.extend([[[2]], [[6]]])
sig = quicksort(sig)
print((sig.index([[2]]) + 1) * (sig.index([[6]]) + 1))

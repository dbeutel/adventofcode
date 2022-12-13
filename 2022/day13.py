def cmp(a, b):
    a, b = ab = [[i] if isinstance(i, int) else i for i in (a, b)]
    if all(isinstance(i, int) for i in a + b):
        return (a > b) - (a < b)
    return x if (x := cmp(*(i[0] if len(i) else i for i in ab))) else cmp(a[1:], b[1:])


s = list(map(__import__("ast").literal_eval, open("input13.txt").read().split()))
print(sum(i + 1 for i, (a, b) in enumerate(zip(s[::2], s[1::2])) if cmp(a, b) < 0))
print((sum(cmp(i, [[2]]) < 0 for i in s) + 1) * (sum(cmp(i, [[6]]) < 0 for i in s) + 2))

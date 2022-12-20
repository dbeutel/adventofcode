def decode(n, vs):
    ixs = list(range(nvs := len(vs)))
    for i in range(n * nvs):
        ixs.pop(ii := ixs.index(i % nvs))
        ixs.insert((ii + vs[i % nvs]) % (nvs - 1), i % nvs)
    return sum(vs[ixs[(ixs.index(vs.index(0)) + i * 1000) % nvs]] for i in range(1, 4))


print(decode(1, vs := [*map(int, open("input20.txt"))]))
print(decode(10, [v * 811_589_153 for v in vs]))

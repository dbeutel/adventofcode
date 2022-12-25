def dec(s):
    return sum(
        ("=-012".index(c) - 2) * 5**p for p, c in enumerate(reversed(s.strip()))
    )


def snafu(d):
    if d == 0:
        return "0"
    s = ""
    while d != 0:
        s = "=-012"[(d + 2) % 5] + s
        d = (d + 2) // 5
    return s


print(snafu(sum(map(dec, open("input25.txt")))))

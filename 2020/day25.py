import itertools

keys = [0, 0]
with open("input25.txt", "r") as f:
    for i, line in enumerate(f.readlines()):
        keys[i] = int(line)

# Example
# keys = [5764801, 17807724]


def transform(n, subject, times):
    for _ in range(times):
        n = (n * subject) % 20201227
    return n


i = 0
value = 1
while value != keys[0]:
    i += 1
    value = transform(value, 7, 1)

print(transform(1, keys[1], i))

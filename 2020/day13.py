import functools


with open('input13.txt', 'r') as f:
    lines = f.readlines()

earliest = int(lines[0])
ids = [int(x) for x in lines[1].split(',') if x != 'x']

waitingtime = [((earliest - 1) // id + 1) * id - earliest for id in ids]
next, idx = min((val, idx) for (idx, val) in enumerate(waitingtime))
print(next * ids[idx])

# This is kind of a trick solution, not a real one.
# There are two large ids. Every other id can be grouped to one of the large ones to
# which it only has a relative offset that corresponds to itself.
# So an educated guess later we only need to find the right combination of those to
# groups.
offsets = [t for t, x in enumerate(lines[1].split(',')) if x != 'x']

maxidx = nextmaxidx = 0
for i, (id, offset) in enumerate(zip(ids, offsets)):
    if id > ids[maxidx]:
        maxidx, nextmaxidx = i, maxidx
    elif id > ids[nextmaxidx]:
        nextmaxidx = i

a = ids[maxidx]
b = ids[nextmaxidx]
for id, offset in zip(ids, offsets):
    if abs(offset - offsets[maxidx]) == id:
        a *= id
    if abs(offset - offsets[nextmaxidx]) == id:
        b *= id

i = j = 0
while True:
    if a * i - b * j > offsets[maxidx] - offsets[nextmaxidx]:
        j += 1
    elif a * i - b * j < offsets[maxidx] - offsets[nextmaxidx]:
        i += 1
    else:
        print(a * i - offsets[maxidx])
        break

# Second, real solution using the chinese remainder theorem (also faster)
def exteuclid(a, b):
    if b == 0:
        return a, 1, 0
    d, s, t = exteuclid(b, a % b)
    return d, t, s - a // b * t


def chremth(as_, ms):
    M = functools.reduce(lambda x, y: x * y, ms)
    return sum([a * M // m * exteuclid(m, M // m)[2] for a, m in zip(as_, ms)]) % M


print(chremth([-o for o in offsets], ids))

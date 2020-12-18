def move(c, x, y):
    if c == '<':
        x -= 1
    elif c == '>':
        x += 1
    elif c == '^':
        y += 1
    elif c == 'v':
        y -= 1
    return x, y

with open('input03.txt', 'r') as f:
    input = f.read().strip()

s = {(0, 0)}
x = y = 0
for c in input:
    x, y = move(c, x, y)
    s.add((x, y))
print(len(s))

s = {(0, 0)}
x = y = 0 # Santa
a = b = 0 # Robo-Santa
for i, c in enumerate(input):
    if i % 2 == 0:
        x, y = move(c, x, y)
        s.add((x, y))
    else:
        a, b = move(c, a, b)
        s.add((a,b))
print(len(s))

import re

p = re.compile('ne|se|sw|nw|e|w')

with open('input24.txt', 'r') as f:
    tiles = [p.findall(line) for line in f.readlines()]

# print(tiles)
direction = {'ne': (1, 0), 'nw': (0, 1), 'sw': (-1, 0), 'se': (0, -1), 'e': (1, -1), 'w': (-1, 1)}
def move(x, y, dir):
    dx, dy = direction[dir]
    return x + dx, y + dy

black = set()
for tile in tiles:
    pos = (0, 0)
    for dir in tile:
        pos = move(*pos, dir)
    if pos in black:
        black.remove(pos)
    else:
        black.add(pos)
print(len(black))


def nextday(black):
    neighbours = {b: 0 for b in black}
    for tile in black:
        for dir in direction:
            pos = move(*tile, dir)
            neighbours[pos] = neighbours.setdefault(pos, 0) + 1
    for k, v in neighbours.items():
        if k in black:
            if v == 0 or v > 2:
                black.remove(k)
        else:
            if v == 2:
                black.add(k)
    return black

for _ in range(100):
    nextday(black)

print(len(black))

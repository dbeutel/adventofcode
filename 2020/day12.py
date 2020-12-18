actions = []
with open('input12.txt', 'r') as f:
    for line in f.readlines():
        actions.append((line[0], int(line[1:])))

def move(a, b, pos):
    if a == 'N':
        pos[0] = pos[0] + b
    if a == 'S':
        pos[0] = pos[0] - b
    elif a == 'E':
        pos[1] = pos[1] + b
    elif a == 'W':
        pos[1] = pos[1] - b
    return pos


dirdct = {0: 'N', 90: 'E', 180: 'S', 270: 'W'}

dir = 90
pos = [0, 0]
for a, b in actions:
    if a in ('N', 'S', 'E', 'W'):
        move(a, b, pos)
    elif a == 'L':
        dir = (dir - b) % 360
    elif a == 'R':
        dir = (dir + b) % 360
    elif a == 'F':
        move(dirdct[dir], b, pos)
print(abs(pos[0]) + abs(pos[1]))

pos = [0, 0]
pos_way = [1, 10]
for a, b in actions:
    if a in ('N', 'S', 'E', 'W'):
        move(a, b, pos_way)
    elif a == 'L':
        for _ in range(b // 90):
            pos_way = [pos_way[1], -pos_way[0]]
    elif a == 'R':
        for _ in range(b // 90):
            pos_way = [-pos_way[1], pos_way[0]]
    elif a == 'F':
        pos = [x + b * y for x, y in zip(pos, pos_way)]
print(abs(pos[0]) + abs(pos[1]))

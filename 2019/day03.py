with open("input03.txt", "r") as f:
    wire = f.readlines()


def move(pos, dir):
    if dir == "R":
        return pos[0] + 1, pos[1]
    if dir == "L":
        return pos[0] - 1, pos[1]
    if dir == "U":
        return pos[0], pos[1] + 1
    if dir == "D":
        return pos[0], pos[1] - 1


candidates = {}

pos = (0, 0)
steps = 0
for c in wire[0].split(","):
    dir = c[0]
    length = int(c[1:])
    while length > 0:
        length -= 1
        steps += 1
        pos = move(pos, dir)
        if pos not in candidates:
            candidates[pos] = steps

nearest = 999_999
shortest = 999_999
pos = (0, 0)  #
steps = 0
for c in wire[1].split(","):
    dir = c[0]
    length = int(c[1:])
    while length > 0:
        # print(dir, ' ', length)
        length -= 1
        steps += 1
        pos = move(pos, dir)
        if pos in candidates:
            manhattan = abs(pos[0]) + abs(pos[1])
            nearest = manhattan if manhattan < nearest else nearest
            totalsteps = steps + candidates[pos]
            shortest = totalsteps if totalsteps < shortest else shortest

print(nearest)
print(shortest)

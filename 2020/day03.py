import math

with open('input03.txt', 'r') as f:
    lines = f.readlines()

slopes_right = [1, 3, 5, 7, 1]
slopes_down = [1, 1, 1, 1, 2]
hits = [0, 0, 0, 0, 0]

linelen = len(lines[0]) - 1
for slope_idx, (slope_right, slope_down) in enumerate(zip(slopes_right, slopes_down)):
    pos = 0
    for i, line in enumerate(lines):
        if not i % slope_down == 0:
            continue
        if line[pos] == '#':
            hits[slope_idx] += 1
        pos = (pos + slope_right) % linelen

print(hits[1])
print(math.prod(hits))

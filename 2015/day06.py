import re

import numpy as np


p = re.compile('(turn on|toggle|turn off) ([0-9]*),([0-9]*) through ([0-9]*),([0-9]*)')
grid = np.full((1000, 1000), False)
grid2 = np.zeros((1000, 1000), np.int)

with open('input06.txt', 'r') as f:
    for line in f.readlines():
        a = p.search(line)
        x0, y0, x1, y1 = [int(i) for i in a.groups()[1:5]]
        if a.group(1) == 'turn on':
            grid[x0:x1 + 1, y0:y1 + 1] = True
            grid2[x0:x1 + 1, y0:y1 + 1] += 1
        elif a.group(1) == 'turn off':
            grid[x0:x1 + 1, y0:y1 + 1] = False
            grid2[x0:x1 + 1, y0:y1 + 1] = np.maximum(0, grid2[x0:x1 + 1, y0:y1 + 1] - 1)
        elif a.group(1) == 'toggle':
            grid[x0:x1 + 1, y0:y1 + 1] = np.invert(grid[x0:x1 + 1, y0:y1 + 1])
            grid2[x0:x1 + 1, y0:y1 + 1] += 2
print(np.sum(grid))
print(np.sum(grid2))

import numpy as np
import scipy.signal as sg

with open("input11.txt", "r") as f:
    grid = np.array(
        [
            [int(x) for x in line.strip("\n").replace(".", "2").replace("L", "0")]
            for line in f.readlines()
        ]
    )
    grid = np.ma.masked_array(grid, mask=grid == 2)

adjacent = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])


def apply_rules(grid):
    neighbours = sg.convolve2d(grid.filled(0), adjacent, mode="same")
    newgrid = grid.copy()
    for i, j in np.ndindex(grid.shape):
        if grid[i, j] == np.ma.masked:
            continue
        if grid[i, j] == 0 and neighbours[i, j] == 0:
            newgrid[i, j] = 1
        if grid[i, j] == 1 and neighbours[i, j] >= 4:
            newgrid[i, j] = 0
    return newgrid


def apply_rules_2(grid):
    newgrid = grid.copy()
    for x, y in np.ndindex(grid.shape):
        if grid[x, y] == np.ma.masked:
            continue
        n = 0
        for dx, dy in [
            (1, 0),
            (1, 1),
            (0, 1),
            (-1, 1),
            (-1, 0),
            (-1, -1),
            (0, -1),
            (1, -1),
        ]:
            ix, iy = x + dx, y + dy
            while 0 <= ix < grid.shape[0] and 0 <= iy < grid.shape[1]:
                if grid[ix, iy] == 1:
                    n += 1
                if grid[ix, iy] is not np.ma.masked:
                    break
                ix, iy = ix + dx, iy + dy
        if grid[x, y] == 0 and n == 0:
            newgrid[x, y] = 1
        elif grid[x, y] == 1 and n >= 5:
            newgrid[x, y] = 0
    return newgrid


origgrid = grid.copy()
newgrid = apply_rules(grid)
while not np.array_equal(grid, newgrid):
    grid = newgrid
    newgrid = apply_rules(grid)
print(newgrid.sum())

grid = origgrid
newgrid = apply_rules_2(grid)
while not np.array_equal(grid, newgrid):
    grid = newgrid
    newgrid = apply_rules_2(grid)
print(newgrid.sum())

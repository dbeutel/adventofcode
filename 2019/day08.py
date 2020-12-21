import numpy as np

with open('input08.txt', 'r') as f:
    data = np.array([int(i) for i in f.read().strip()])

data = data.reshape((-1, 6, 25))

fewestzeros = 999_999
for layer in data:
    nzeros = np.sum(layer == 0)
    if nzeros < fewestzeros:
        fewestzeros = nzeros
        res = np.sum(layer == 1) * np.sum(layer == 2)

print(res)

pic = data[0]
for layer in data[1:]:
    pic[pic == 2] = layer[pic == 2]

for line in pic:
    print(''.join(['#' if i == 1 else ' ' for i in line]))

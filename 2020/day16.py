import re

with open('input16.txt', 'r') as f:
    lines = f.readlines()

part = 0
fields = {}
tickets = []
p = re.compile('([a-z ]*): ([0-9-]*) or ([0-9-]*)')
maximum = -1
minimum = 1000
for line in lines:
    if line == '\n':
        continue
    if line == 'your ticket:\n':
        part = 1
        continue
    if line == 'nearby tickets:\n':
        part = 2
        continue
    if part == 0:
        a = p.search(line)
        xmin, xmax = [int(i) for i in a.group(2).split('-')]
        ymin, ymax = [int(i) for i in a.group(3).split('-')]
        if maximum < ymax:
            maximum = ymax
        if minimum > xmin:
            minimum = xmin
        fields[a.group(1)] = [(xmin, xmax), (ymin, ymax)]
    if part == 1:
        myticket = [int(i) for i in line.split(',')]
    if part == 2:
        tickets.append([int(i) for i in line.split(',')])

ninvalid = 0
validtickets = []
for ticket in tickets:
    valid = True
    for val in ticket:
        if val < minimum or maximum < val:
            ninvalid += val
            valid = False
    if valid:
        validtickets.append(ticket)
print(ninvalid)

# For each field find possible columns
fieldvalues = list(zip(*validtickets))
pos = []
for field in fields:
    tmp = set()
    ra, rb = fields[field]
    for j, vals in enumerate(fieldvalues):
        if all([ra[0] <= val <= ra[1] or rb[0] <= val <= rb[1] for val in vals]):
            tmp.add(j)
    pos.append(tmp)

# Eliminate possible colums, that are necessarily taken by other fields
remove = set()
i = 0
while i < len(pos):
    if len(pos[i]) > 1:
        pos[i] = pos[i].difference(remove)
    if len(pos[i]) == 1 and next(iter(pos[i])) not in remove:
        remove.add(next(iter(pos[i])))
        i = -1
    i += 1

res = 1
for i, key in enumerate(fields):
    if key[0:9] == 'departure':
        res *= myticket[next(iter(pos[i]))]
print(res)

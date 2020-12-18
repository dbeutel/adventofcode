with open('input05.txt', 'r') as f:
    lines = f.readlines()

maxid = 0
ids = []
for line in lines:
    line = line.replace('B', '1').replace('R', '1').replace('F', '0').replace('L', '0')
    id = int(line, 2)
    ids.append(id)
    if id > maxid:
        maxid = id

ids.sort()
lastid = ids[0]
for id in ids[1:]:
    if not id == lastid + 1:
        break
    lastid = id

print(maxid)
print(lastid + 1)

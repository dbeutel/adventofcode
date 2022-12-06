monster = [
    (18, 0),
    (0, 1),
    (5, 1),
    (6, 1),
    (11, 1),
    (12, 1),
    (17, 1),
    (18, 1),
    (19, 1),
    (1, 2),
    (4, 2),
    (7, 2),
    (10, 2),
    (13, 2),
    (16, 2),
]


class Tile:
    def __init__(self, id, picture):
        self.id = id
        self.picture = picture
        self.corners = Tile.getcorners(picture)
        self.corners_flipped = Tile.flipcorners(self.corners, len(picture[0]))

    @staticmethod
    def getcorners(picture):
        c = [-1] * 4
        c[0] = int(picture[0].replace("#", "1").replace(".", "0"), 2)
        c[2] = int(picture[-1][::-1].replace("#", "1").replace(".", "0"), 2)
        c[1] = int(
            ("".join([i[-1] for i in picture])).replace("#", "1").replace(".", "0"), 2
        )
        c[3] = int(
            ("".join([i[0] for i in picture[::-1]]))
            .replace("#", "1")
            .replace(".", "0"),
            2,
        )
        return c

    @staticmethod
    def flipcorners(corners, x):
        c = [int(str(f"{i:0{x}b}")[::-1], 2) for i in corners]
        c[1], c[3] = c[3], c[1]
        return c

    def rotate(self):
        ymax = len(self.picture)  # Old picture
        xmax = len(self.picture[0])  # Old picture
        rawpicture = [[" "] * ymax for _ in range(xmax)]
        for y in range(ymax):
            for x in range(xmax):
                rawpicture[x][ymax - 1 - y] = self.picture[y][x]
        self.picture = ["".join(line) for line in rawpicture]
        self.corners.insert(0, self.corners.pop())
        self.corners_flipped.append(self.corners_flipped.pop(0))

    def flip(self):
        self.picture = ["".join(list(line)[::-1]) for line in self.picture]
        self.corners, self.corners_flipped = self.corners_flipped, self.corners

    def align(self, side, val):
        if val in self.corners_flipped and val not in self.corners:
            self.flip()
        if val in self.corners:
            while self.corners[side] != val:
                self.rotate()
            return True
        return False

    def print(self):
        for line in self.picture:
            print(line)

    def findmonster(self, nrot=0, nflip=0):
        total = []
        for y in range(len(self.picture) - 2):
            for x in range(len(self.picture[0]) - 19):
                found = True
                for dx, dy in monster:
                    if self.picture[y + dy][x + dx] != "#":
                        found = False
                        break
                if found:
                    total.append((x, y))
        if not total:
            if nrot < 3:
                self.rotate()
                return self.findmonster(nrot + 1, nflip)
            elif nflip < 1:
                self.flip()
                return self.findmonster(0, 1)
        return total


picture = []
id = -9999
tile = []
with open("input20.txt", "r") as f:
    for line in f.readlines():
        if line.startswith("Tile"):
            id = int(line[5:9])
        elif line == "\n":
            tile.append(Tile(id, picture))
            picture = []
        else:
            picture.append(line.strip())
    if picture:
        tile.append(Tile(id, picture))


def arrange_line(tile, start=None):
    if start is None:
        start = tile.pop()
    line = [start]
    changed = True
    while changed:
        changed = False
        for t in tile:
            if t.align(3, line[-1].corners_flipped[3]):
                tile.remove(t)
                line.append(t)
                changed = True
            elif t.align(1, line[0].corners_flipped[1]):
                tile.remove(t)
                line.insert(0, t)
                changed = True
    return line


def arrange(tile):
    res = [arrange_line(tile)]
    changed = True
    while tile:
        t = tile.pop(0)
        if t.align(0, res[-1][0].corners_flipped[2]):
            res.append(arrange_line(tile, t))
        elif t.align(2, res[0][0].corners_flipped[0]):
            res.insert(0, arrange_line(tile, t))
        else:
            tile.append(t)
    return res


res = arrange(tile)
print(res[0][0].id * res[-1][0].id * res[0][-1].id * res[-1][-1].id)

picture = []
for line in res:
    for i in range(1, len(line[0].picture) - 1):
        picture.append("".join([t.picture[i][1:-1] for t in line]))

image = Tile(id, picture)
nmonster = len(image.findmonster())
print(sum([i.count("#") for i in image.picture]) - nmonster * len(monster))

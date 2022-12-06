from time import sleep

from intcode import Intcode


def sign(x):
    if x == 0:
        return 0
    elif x > 0:
        return 1
    return -1


decode = [" ", "#", "=", "-", "o"]


class Screen:
    def __init__(self, size=(37, 26)):
        x, y = size
        self.screen = screen = [[0] * x for _ in range(y)]
        self.score = 0
        self.ballx = -1
        self.paddlex = -1

    def update(self, res):
        while len(res) > 2:
            x, y, tileid, *res = res
            if x == -1 and y == 0:
                self.score = tileid
            else:
                self.screen[y][x] = tileid
                if tileid == 4:
                    self.ballx = x
                elif tileid == 3:
                    self.paddlex = x
        return self.screen

    def print(self):
        for line in self.screen:
            print("".join([decode[i] for i in line]))
        print(f"Score: {self.score}")


with open("input13.txt", "r") as f:
    tape = [int(i) for i in f.read().split(",")]

c = Intcode(tape)
c.run()

total = 0
screen = Screen()
for line in screen.update(c.flush()):
    total += sum([i == 2 for i in line])
print(total)


tape[0] = 2
video = input("Video (Y/n)? ").lower().strip() in ("", "y")
c = Intcode(tape)
ret = c.run()
screen = Screen()
while ret != 0:
    screen.update(c.flush())
    if video:
        screen.print()
        sleep(0.025)
    c.input = sign(screen.ballx - screen.paddlex)
    ret = c.run()
screen.update(c.flush())
if video:
    screen.print()
else:
    print(screen.score)

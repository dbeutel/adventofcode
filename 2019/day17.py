from time import sleep
import os

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

from intcode import Intcode

with open('input17.txt', 'r') as f:
    tape = [int(i) for i in f.read().split(',')]

code = Intcode(tape)
code.run()
view = ''.join([chr(i) for i in code.flush()])
# print(view)

def decode(i):
    if i == '.':
        return 0
    if i == '#':
        return 1
    if i == '^':
        return 2
    if i == '>':
        return 3
    if i == 'v':
        return 4
    if i == '<':
        return 5

grid = []
for line in view.strip().split('\n'):
    grid.append([decode(i) for i in line.strip()])

sumalign = 0
for y in range(1, len(grid) - 1):
    for x in range(1, len(grid[y]) - 1):
        if grid[y][x] and grid[y + 1][x] and grid[y - 1][x] and grid[y][x + 1] and grid[y][x - 1]:
            sumalign += x * y
print(sumalign)

tape[0] = 2
code = Intcode(tape)
code.input = [ord(i) for i in 'A,A,B,C,B,C,B,C,B,A\nR,10,L,12,R,6\nR,6,R,10,R,12,R,6\nR,10,L,12,L,12\nn\n']
code.run()
res = code.flush()[-1]
print(res)

x = input('Start interactive (Y/n)? ').lower().strip()
while x == '' or x == 'y':
    code = Intcode(tape)
    ret = code.run(True)
    c = ''
    first = True
    while ret != 0:
        if ret == 2:
            c, prev = chr(code.flush()[0]), c
            if c == prev == '\n':
                if first:
                    first = False
                else:
                    sleep(0.1)
                    clear()
            if ord(c) != res:
                print(c, end='')
        if ret == 1:
            y = input('')
            code.input = [ord(i) for i in y]
            code.input = ord('\n')
        ret = code.run(True)
    print(f'Collected dust: {ord(c)}')
    x = input('Restart (Y/n)? ').lower().strip()

if x != 'n':
    print('Unrecognized option')

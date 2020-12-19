from time import sleep

from intcode import Intcode

with open('input25.txt', 'r') as f:
    tape = [int(i) for i in f.read().split(',')]

code = Intcode(tape, [ord(i) for i in """south
take fuel cell
north
north
west
south
take planetoid
west
take antenna
east
east
take mutex
south
south
east
north
"""])
code.run()
print(''.join([chr(i) for i in code.flush()]))

x = input('Start interactive (Y/n)? ').lower().strip()
while x == '' or x == 'y':
    code = Intcode(tape)
    ret = code.run(True)
    while ret != 0:
        if ret == 2:
            print(chr(code.flush()[0]), end='')
        if ret == 1:
            y = input('')
            code.input = [ord(i) for i in y]
            code.input = ord('\n')
        ret = code.run(True)
    x = input('Restart (Y/n)? ').lower().strip()

if x != 'n':
    print('Unrecognized option')

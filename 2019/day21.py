from time import sleep

from intcode import Intcode

with open('input21.txt', 'r') as f:
    tape = [int(i) for i in f.read().split(',')]

c = Intcode(tape, [ord(i) for i in'NOT C J\nAND D J\nNOT A T\nOR T J\nWALK\n'])
c.run()
print(c.flush()[-1])


c = Intcode(tape, [ord(i) for i in'NOT B T\nNOT C J\nOR T J\nAND D J\nAND H J\nNOT A T\nOR T J\nRUN\n'])
c.run()
print(c.flush()[-1])


x = input('Start interactive (Y/n)? ').lower().strip()
while x == '' or x == 'y':
    code = Intcode(tape)
    ret = code.run(True)
    while ret != 0:
        if ret == 2:
            c = code.flush()[0]
            if c < 128:
                print(chr(c), end='')
        if ret == 1:
            y = input('')
            code.input = [ord(i) for i in y]
            code.input = ord('\n')
        ret = code.run(True)
    print(f'Collected dust: {c}')
    x = input('Restart (Y/n)? ').lower().strip()

if x != 'n':
    print('Unrecognized option')

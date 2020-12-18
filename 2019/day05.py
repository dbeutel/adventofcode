with open('input05.txt', 'r') as f:
    tape = [int(i) for i in f.read().split(',')]

def getmodes(x, n):
    res = []
    for _ in range(n):
        res.append(x % 10)
        x //= 10
    return res

def getparam(mode, val, tape):
    if mode == 0:
        return tape[val]
    elif mode == 1:
        return val

def run(tape, input):
    pc = 0
    output = []
    while True:
        opcode = tape[pc] % 100
        modes = tape[pc] // 100
        if opcode == 1:
            a, b = [
                    getparam(mode, val, tape)
                    for mode, val in zip(getmodes(modes, 2), tape[pc + 1 : pc + 3])
            ]
            tape[tape[pc + 3]] = a + b
            pc += 4
        elif opcode == 2:
            a, b = [
                    getparam(mode, val, tape)
                    for mode, val in zip(getmodes(modes, 2), tape[pc + 1 : pc + 3])
            ]
            tape[tape[pc + 3]] = a * b
            pc += 4
        elif opcode == 3:
            tape[tape[pc + 1]] = input
            pc += 2
        elif opcode == 4:
            output.append(getparam(getmodes(modes, 1)[0], tape[pc + 1], tape))
            pc += 2
        elif opcode == 5:
            a, b = [
                    getparam(mode, val, tape)
                    for mode, val in zip(getmodes(modes, 2), tape[pc + 1 : pc + 3])
            ]
            pc = b if a else (pc + 3)
        elif opcode == 6:
            a, b = [
                    getparam(mode, val, tape)
                    for mode, val in zip(getmodes(modes, 2), tape[pc + 1 : pc + 3])
            ]
            pc = b if not a else (pc + 3)
        elif opcode == 7:
            a, b = [
                    getparam(mode, val, tape)
                    for mode, val in zip(getmodes(modes, 2), tape[pc + 1 : pc + 3])
            ]
            tape[tape[pc + 3]] = int(a < b)
            pc += 4
        elif opcode == 8:
            a, b = [
                    getparam(mode, val, tape)
                    for mode, val in zip(getmodes(modes, 2), tape[pc + 1 : pc + 3])
            ]
            tape[tape[pc + 3]] = int(a == b)
            pc += 4
        elif opcode == 99:
            break
    return output

print(run(tape.copy(), 1)[-1])
print(run(tape, 5)[-1])

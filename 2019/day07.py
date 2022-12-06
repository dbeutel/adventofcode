import itertools

with open("input07.txt", "r") as f:
    tape = [int(i) for i in f.read().split(",")]


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


def run(tape, input, pc=0):
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
            if not input:
                return (1, pc, output)
            tape[tape[pc + 1]] = input.pop()
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
            return (0, pc, output)


maximum = -999
for setting in itertools.permutations(range(5)):
    output = [0]
    for phase in setting:
        input = output + [phase]
        _, _, output = run(tape.copy(), input)
    maximum = max(maximum, output[0])
print(maximum)


maximum = -999
for setting in itertools.permutations(range(5, 10)):
    tapes = [tape.copy() for _ in range(5)]  # set up each tape
    inputs = [[x] for x in setting]  # prepare first inputs
    inputs[0] = [0] + inputs[0]  # cont.
    pcs = [0] * 5
    res = [1] * 5
    i = 0
    while any(res):
        res[i], pcs[i], out = run(tapes[i], inputs[i], pcs[i])
        i = (i + 1) % 5
        inputs[i] = out[::-1] + inputs[i]
    maximum = max(maximum, out[0])
print(maximum)

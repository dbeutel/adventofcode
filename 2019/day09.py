def _getmodes(x):
    while True:
        yield x % 10
        x //= 10


def _get(tape, pos):
    if pos >= len(tape):
        return 0
    return tape[pos]


def _read(tape, pos, mode=0, relbase=0):
    if mode == 0:
        return _get(tape, _get(tape, pos))
    elif mode == 1:
        return _get(tape, pos)
    elif mode == 2:
        return _get(tape, relbase + _get(tape, pos))


def _write(tape, pos, val, mode=0, relbase=0):
    if mode == 0:
        finalpos = _get(tape, pos)
    elif mode == 2:
        finalpos = relbase + _get(tape, pos)
    while len(tape) - 1 < finalpos:
        tape.append(0)
    tape[finalpos] = val


def intcode(tape, input, pc=0, relbase=0):
    output = []
    while True:
        opcode = tape[pc] % 100
        modes = tape[pc] // 100
        if opcode == 1:  # add
            g = iter(_getmodes(modes))
            a, b = [_read(tape, pos, next(g), relbase) for pos in range(pc + 1, pc + 3)]
            _write(tape, pc + 3, a + b, next(g), relbase)
            pc += 4
        elif opcode == 2:  # mul
            g = iter(_getmodes(modes))
            a, b = [_read(tape, pos, next(g), relbase) for pos in range(pc + 1, pc + 3)]
            _write(tape, pc + 3, a * b, next(g), relbase)
            pc += 4
        elif opcode == 3:  # get input
            if not input:
                return (1, output, pc, relbase)
            _write(tape, pc + 1, input.pop(), next(iter(_getmodes(modes))), relbase)
            pc += 2
        elif opcode == 4:  # output
            output.append(_read(tape, pc + 1, next(iter(_getmodes(modes))), relbase))
            pc += 2
        elif opcode == 5:  # jump if not zero
            g = iter(_getmodes(modes))
            a, b = [_read(tape, pos, next(g), relbase) for pos in range(pc + 1, pc + 3)]
            pc = b if a else (pc + 3)
        elif opcode == 6:  # jump if zero
            g = iter(_getmodes(modes))
            a, b = [_read(tape, pos, next(g), relbase) for pos in range(pc + 1, pc + 3)]
            pc = b if not a else (pc + 3)
        elif opcode == 7:  # less than
            g = iter(_getmodes(modes))
            a, b = [_read(tape, pos, next(g), relbase) for pos in range(pc + 1, pc + 3)]
            _write(tape, pc + 3, int(a < b), next(g), relbase)
            pc += 4
        elif opcode == 8:  # equal
            g = iter(_getmodes(modes))
            a, b = [_read(tape, pos, next(g), relbase) for pos in range(pc + 1, pc + 3)]
            _write(tape, pc + 3, int(a == b), next(g), relbase)
            pc += 4
        elif opcode == 9:  # relbase
            relbase += _read(tape, pc + 1, next(iter(_getmodes(modes))), relbase)
            pc += 2
        elif opcode == 99:  # halt
            return (0, output, pc, relbase)


if __name__ == "__main__":
    with open("input09.txt", "r") as f:
        tape = [int(i) for i in f.read().split(",")]

    print(intcode(tape.copy(), [1])[1][0])
    print(intcode(tape, [2])[1][0])

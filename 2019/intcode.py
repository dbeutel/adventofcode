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


class Intcode:
    def __init__(self, tape, input=None):
        self.tape = tape.copy()
        self.pc = 0
        self.relbase = 0
        if input is None:
            input = []
        if isinstance(input, list):
            self._input = input
        else:
            self._input = [input]
        self.output = []
        self.halt = False

    @property
    def input(self):
        return self._input

    @input.setter
    def input(self, x):
        if isinstance(x, list):
            self._input.extend(x)
        else:
            self._input.append(x)

    def flush(self):
        out = self.output.copy()
        self.output.clear()
        return out

    def run(self, stopatoutput=False):
        if self.halt:
            return 0
        while True:
            opcode = self.tape[self.pc] % 100
            modes = self.tape[self.pc] // 100
            if opcode == 1:  # add
                g = iter(_getmodes(modes))
                a, b = [
                    _read(self.tape, pos, next(g), self.relbase)
                    for pos in range(self.pc + 1, self.pc + 3)
                ]
                _write(self.tape, self.pc + 3, a + b, next(g), self.relbase)
                self.pc += 4
            elif opcode == 2:  # mul
                g = iter(_getmodes(modes))
                a, b = [
                    _read(self.tape, pos, next(g), self.relbase)
                    for pos in range(self.pc + 1, self.pc + 3)
                ]
                _write(self.tape, self.pc + 3, a * b, next(g), self.relbase)
                self.pc += 4
            elif opcode == 3:  # get input
                if not self._input:
                    return 1
                val = self._input[0]
                self._input.remove(val)
                _write(
                    self.tape,
                    self.pc + 1,
                    val,
                    next(iter(_getmodes(modes))),
                    self.relbase,
                )
                self.pc += 2
            elif opcode == 4:  # output
                self.output.append(
                    _read(
                        self.tape,
                        self.pc + 1,
                        next(iter(_getmodes(modes))),
                        self.relbase,
                    )
                )
                self.pc += 2
                if stopatoutput:
                    return 2
            elif opcode == 5:  # jump if not zero
                g = iter(_getmodes(modes))
                a, b = [
                    _read(self.tape, pos, next(g), self.relbase)
                    for pos in range(self.pc + 1, self.pc + 3)
                ]
                self.pc = b if a else (self.pc + 3)
            elif opcode == 6:  # jump if zero
                g = iter(_getmodes(modes))
                a, b = [
                    _read(self.tape, pos, next(g), self.relbase)
                    for pos in range(self.pc + 1, self.pc + 3)
                ]
                self.pc = b if not a else (self.pc + 3)
            elif opcode == 7:  # less than
                g = iter(_getmodes(modes))
                a, b = [
                    _read(self.tape, pos, next(g), self.relbase)
                    for pos in range(self.pc + 1, self.pc + 3)
                ]
                _write(self.tape, self.pc + 3, int(a < b), next(g), self.relbase)
                self.pc += 4
            elif opcode == 8:  # equal
                g = iter(_getmodes(modes))
                a, b = [
                    _read(self.tape, pos, next(g), self.relbase)
                    for pos in range(self.pc + 1, self.pc + 3)
                ]
                _write(self.tape, self.pc + 3, int(a == b), next(g), self.relbase)
                self.pc += 4
            elif opcode == 9:  # relbase
                self.relbase += _read(
                    self.tape, self.pc + 1, next(iter(_getmodes(modes))), self.relbase
                )
                self.pc += 2
            elif opcode == 99:  # halt
                return 0

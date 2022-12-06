with open("input02.txt", "r") as f:
    origtape = [int(i) for i in f.read().split(",")]


def run(tape):
    pc = 0
    while True:
        if tape[pc] == 1:
            a, b, d = tape[pc + 1 : pc + 4]
            tape[d] = tape[a] + tape[b]
        elif tape[pc] == 2:
            a, b, d = tape[pc + 1 : pc + 4]
            tape[d] = tape[a] * tape[b]
        elif tape[pc] == 99:
            break
        pc += 4
    return tape[0]


tape = origtape.copy()
tape[1] = 12
tape[2] = 2
print(run(tape))

for x in range(10_000):
    tape = origtape.copy()
    tape[1] = x // 100
    tape[2] = x % 100
    if run(tape) == 19690720:
        print(x)
        break

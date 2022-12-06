import copy

ops = []
with open("input08.txt", "r") as f:
    for line in f.readlines():
        op, arg = line.split()
        ops.append((op, int(arg)))


def run(ops):
    visited = [False] * len(ops)
    pc = 0
    acc = 0
    ret = 3  # loop
    while not visited[pc]:
        op, arg = ops[pc]
        visited[pc] = True
        if op == "jmp":
            pc += arg
        elif op == "nop":
            pc += 1
        elif op == "acc":
            acc += arg
            pc += 1
        else:
            ret = 2  # illegal instruction
            break
        if visited[-1]:
            ret = 0  # legal terminate
            break
        if pc >= len(ops) or pc < 0:
            ret = 1  # illegal terminate
            break
    return ret, acc


# Part 1
ret, acc = run(ops)
print(acc)

# Part 2
for i, (op, arg) in enumerate(ops):
    newops = copy.copy(ops)
    if op == "acc":
        continue
    elif op == "jmp":
        newops[i] = ("nop", arg)
    elif op == "nop":
        newops[i] = ("jmp", arg)
    ret, acc = run(newops)
    if ret == 0:
        print(acc)

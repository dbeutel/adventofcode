with open('input18.txt', 'r') as f:
    lines = f.readlines()

def bracket(line, part2=False):
    n = 1
    tmp = []
    while n > 0:
        a, *line = line
        if a == '(':
            n += 1
        if a == ')':
            n -= 1
        tmp.append(a)
    return evaluate(tmp[:-1], part2=part2), line

def nextoperand(line, part2=False):
    a, *line = line
    if a == '(':
        return bracket(line, part2=part2)
    elif a.isdigit():
        return int(a), line


def evaluate(line, res=None, part2=False):
    if not line:
        return res
    if res is None:
        x, line = nextoperand(line)
        return evaluate(line, x, part2)
    a, *line = line
    if a == '*':
        if part2:
            return res * evaluate(line, part2=part2)
        else:
            x, line = nextoperand(line)
            return evaluate(line, res * x, part2=part2)
    if a == '+':
        x, line = nextoperand(line)
        return evaluate(line, res + x, part2=part2)

print(sum([evaluate(list(''.join(line.split()))) for line in lines]))
print(sum([evaluate(list(''.join(line.split())), part2=True) for line in lines]))

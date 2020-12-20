import re
mode = 0
message = []
rawrule = {}
with open('input19.txt', 'r') as f:
    for line in f.readlines():
        if line == '\n':
            mode += 1
        if mode == 0:
            k, v = line.split(':')
            rawrule[int(k)] = v.strip()
        elif mode == 1:
            message.append(line.strip())

def makere(rule, line):
    return ''.join([rule[int(i)] for i in line.split(' ')])

rule = {}
while len(rule) < len(rawrule):
    for k, r in rawrule.items():
        if k in rule:
            continue
        x = r.find('|')
        if r.startswith('"'):
            rule[k] = r[1]
        elif x == -1 and all([(int(i) in rule) for i in r.split(' ')]):
            rule[k] = makere(rule, r)
        elif x != -1 and all([(int(i) in rule) for i in r.replace('| ', '').split(' ')]):
            rule[k] = '(?:' + '|'.join([makere(rule, y.strip()) for y in r.split('|')]) + ')'


p = re.compile('^' + rule[0] + '$')
matchzero = 0
for i in message:
    if p.match(i):
        matchzero += 1

print(matchzero)

p = re.compile('^((' + rule[42] + ')+)((' + rule[31] + ')+)$')
matchzero = 0
for i in message:
    x = p.search(i)
    if x and len(x.group(1)) // len(x.group(2)) > len(x.group(3)) // len(x.group(4)):
        matchzero += 1
print(matchzero)

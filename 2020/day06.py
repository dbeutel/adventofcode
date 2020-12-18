import re

with open('input06.txt', 'r') as f:
    lines = f.readlines()

def nyes(text):
    anyone = everyone = 0
    for c in 'abcdefghijklmnopqrstuvwxyz':
        p = re.compile(c)
        if p.search(text):
            anyone += 1
            check_every = True
            for line in text.split('\n'):
                if line == '':
                    continue
                if not p.search(line):
                    check_every = False
                    break
            if check_every:
                everyone += 1
    return anyone, everyone

anyone = everyone = 0
current = ''
for line in lines:
    if line == '\n':
        a, b = nyes(current)
        anyone += a
        everyone += b
        current = ''
    else:
        current = current + line


a, b = nyes(current)
anyone += a
everyone += b
print(anyone)
print(everyone)

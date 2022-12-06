import re

p = re.compile("(?=.*[aeiou].*[aeiou].*[aeiou])(?=.*([a-z])\\1)(?!.*(ab|cd|pq|xy))")
q = re.compile("(?=.*([a-z][a-z]).*\\1)(?=.*([a-z]).\\2)")

nice = nice2 = 0
with open("input05.txt", "r") as f:
    for line in f.readlines():
        if p.match(line):
            nice += 1
        if q.match(line):
            nice2 += 1
print(nice)
print(nice2)

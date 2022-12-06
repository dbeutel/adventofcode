with open("input02.txt", "r") as f:
    input = [sorted([int(i) for i in line.split("x")]) for line in f.readlines()]


paper = ribbon = 0
for i, j, k in input:
    paper += 3 * i * j + 2 * k * (i + j)
    ribbon += 2 * (i + j) + i * j * k
print(paper)
print(ribbon)

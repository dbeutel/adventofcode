import itertools

input = []
with open('input09.txt', 'r') as f:
    for line in f.readlines():
        input.append(int(line))

def part1(input, pre=25):
    for i, x in enumerate(input[pre:]):
        if all([x != y + z for y, z in itertools.product(input[i:i + pre], repeat=2)]):
            return x
    return None


def part2(input, goal):
    low = high = 0
    val = 0
    while high < len(input):
        if val < goal:
            val += input[high]
            high += 1
        elif val > goal:
            val -= input[low]
            low += 1
        if val == goal:
            return min(input[low:high]) + max(input[low:high])
    return None


a = part1(input)
print(a)
print(part2(input, a))

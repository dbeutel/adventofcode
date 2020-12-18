input = [5, 1, 9, 18, 13, 8, 0]

memory = {i: turn + 1 for turn, i in enumerate(input)}
a = len(input)
for turn in range(len(input) + 1, 30000001):
    num = turn - 1 - a
    a = memory.get(num, turn)
    memory[num] = turn
    if turn == 2020:
        print(num)
print(num)

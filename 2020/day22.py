player1 = []
player2 = []

with open('input22.txt', 'r') as f:
    for line in f.readlines():
        if line.strip() == 'Player 1:':
            addto = player1
        elif line.strip() == 'Player 2:':
            addto = player2
        elif line.strip():
            addto.append(int(line))

def score(deck):
    return sum([(i + 1) * x for i, x in enumerate(deck[::-1])])



def combat(player1, player2):
    while player1 and player2:
        a, b = player1.pop(0), player2.pop(0)
        if a > b:
            player1.append(a)
            player1.append(b)
        else:
            player2.append(b)
            player2.append(a)

    return score(player1), score(player2)

print(max(combat(player1.copy(), player2.copy())))

def deckvalue(deck, acc=0):
    if deck:
        a = deck.pop(0)
        acc = acc * 100 + a
        return deckvalue(deck, acc)
    return acc

def recursivecombat(player1, player2):
    existing1 = set()
    existing2 = set()
    while player1 and player2:
        val1, val2 = deckvalue(player1.copy()), deckvalue(player2.copy())
        if val1 in existing1 and val2 in existing2:
            return score(player1), 0
        else:
            existing1.add(val1)
            existing2.add(val2)
        a, b = player1.pop(0), player2.pop(0)
        winner = a > b
        if len(player1) >= a and len(player2) >= b:
            x, y = recursivecombat(player1[:a], player2[:b])
            winner = x > y
        if winner:
            player1.append(a)
            player1.append(b)
        else:
            player2.append(b)
            player2.append(a)

    return score(player1), score(player2)

print(max(recursivecombat(player1.copy(), player2.copy())))

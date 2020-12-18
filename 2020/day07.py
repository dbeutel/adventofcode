import re


with open('input07.txt', 'r') as f:
    lines = f.readlines()

class Bag:
    def __init__(self, name, contains=None):
        self.name = name
        if contains is None:
            self.contains = []
        else:
            self.contains = contains
        self._shiny_gold = None
        self._bags_contained = None
    @property
    def contains_shiny_gold(self):
        if self._shiny_gold is not None:
            return self._shiny_gold
        if self.name == 'shiny gold':
            self._shiny_gold = True
            return True
        if self.contains == []:
            self._shiny_gold = False
            return False
        for bag, _ in self.contains:
            if bag.contains_shiny_gold:
                self._shiny_gold = True
                return True
        self._shiny_gold = False
        return False
    @property
    def total_bags_contained(self):
        if self._bags_contained is not None:
            return self._bags_contained
        total = 0
        for bag, amount in self.contains:
            total += amount * (bag.total_bags_contained + 1)
        self._bags_contained = total
        return total

p = re.compile('([0-9]+) ([a-z ]+) bag')

bags = {}
for line in lines:
    name, _ = line.split(' bags contain ')
    bags[name] = Bag(name)

for line in lines:
    name, inside = line.split(' bags contain ')
    contains = []
    for a, b in p.findall(inside):
        contains.append((bags[b], int(a)))
    bags[name].contains = contains

res = -1 # subtract the shiny gold bag itself
for bag in bags.values():
    res += bag.contains_shiny_gold

print(res)
print(bags['shiny gold'].total_bags_contained)

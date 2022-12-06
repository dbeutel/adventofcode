import functools

ingredients = []
allergens = []
allings = set()
with open("input21.txt", "r") as f:
    for line in f.readlines():
        i, a = line.replace(")", "").split("(contains ")
        ings = set([x.strip() for x in i.strip().split(" ")])
        ingredients.append(ings)
        allings = allings.union(ings)
        allergens.append(set([x.strip() for x in a.strip().split(",")]))

candidates = {}
for ings, allgs in zip(ingredients, allergens):
    for a in allgs:
        candidates[a] = candidates.setdefault(a, allings).intersection(ings)

bijective = set()
lastlen = lastlastlen = -1
while lastlastlen != len(bijective):
    lastlen, lastlastlen = len(bijective), lastlen
    for k, v in candidates.items():
        if len(v) == 1:
            bijective.add(next(iter(v)))
        else:
            candidates[k] = v.difference(bijective)

noallergen = allings.difference(bijective)

total = 0
for ings in ingredients:
    total += sum([i in noallergen for i in ings])
print(total)

allergenssorted = sorted(candidates)
print(",".join([next(iter(candidates[i])) for i in allergenssorted]))

def nvalid(intrvl, pos, prevdigit=-1, doubled=False, atmin=True, atmax=True):
    start = max((intrvl[0] // (10**pos)) % 10, prevdigit) if atmin else prevdigit
    stop = (intrvl[1] // (10**pos)) % 10 if atmax else 9
    if pos == 0:
        if doubled:
            return stop - start + 1
        elif prevdigit in range(start, stop + 1):
            return 1
        return 0
    total = 0
    for i in range(start, stop + 1):
        nowdoubled = doubled or prevdigit == i
        nowatmin = atmin and i == start
        nowatmax = atmax and i == stop
        total += nvalid(intrvl, pos - 1, i, nowdoubled, nowatmin, nowatmax)
    return total


def nvalid2(intrvl, pos, prevdigit=-1, doubled=0, atmin=True, atmax=True):
    # doubled = 0 -> single digit
    # doubled = 1 -> vulnerable double (the only valid double is at the end)
    # doubled = 2 -> overshooted (triple...)
    # doubled = 3 -> safe double
    start = max((intrvl[0] // (10**pos)) % 10, prevdigit) if atmin else prevdigit
    stop = (intrvl[1] // (10**pos)) % 10 if atmax else 9
    if pos == 0:
        if doubled in (1, 3):
            if doubled == 1 and prevdigit in range(start, stop + 1):
                return stop - start
            return stop - start + 1
        elif doubled == 0 and prevdigit in range(start, stop + 1):
            return 1
        return 0
    total = 0
    for i in range(start, stop + 1):
        if doubled in (0, 1, 2):
            if prevdigit == i:
                nowdoubled = min(doubled + 1, 2)
            elif doubled == 1:
                nowdoubled = 3
            else:
                nowdoubled = 0
        else:
            nowdoubled = doubled
        nowatmin = atmin and i == start
        nowatmax = atmax and i == stop
        total += nvalid2(intrvl, pos - 1, i, nowdoubled, nowatmin, nowatmax)
    return total


intrvl = (246515, 739105)
print(nvalid(intrvl, len(str(intrvl[1])) - 1))
print(nvalid2(intrvl, len(str(intrvl[1])) - 1))

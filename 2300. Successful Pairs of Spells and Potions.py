def successfulPairs(spells, potions, success):
    out = []
    potions.sort()

    for i in range(len(spells)):
        out.append(len(potions) - find_valid(spells[i], potions, success))
    return out


def find_valid(spell, potions, success):
    start = 0
    end = len(potions)-1
    while end >= start:
        mid = (end + start) // 2
        if spell * potions[mid] >= success:
            end = mid-1
        else:
            start = mid + 1
    return start


spells = [15, 8, 19]
potions = [38, 36, 23]
success = 328
print(successfulPairs(spells, potions, success))

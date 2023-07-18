# easier to use dict than sliding window
def minimum_card(cards):
    passed = {}
    min_len = float('inf')

    for i, n in enumerate(cards):
        if n in passed:
            min_len = min(min_len,i - passed[n] + 1)
        passed[n] = i

    if min_len == float('inf'):
        return -1
    return min_len


cards = [70, 37, 70, 1]
print(minimum_card(cards))

# since each price is being multiplied by the current date, we want to start by choosing the smaller values
# that way, once we get to the bigger, ones, the multiplier will be bigger and we gain more

from heapq import heappop, heappush


def maxSpending(values: list[list[int]]) -> int:
    values = list(map(lambda x: x[::-1], values))

    n, m = len(values), len(values[0])
    available = []
    for i in range(m):
        heappush(available, (values[i][0], i, 0))

    total = 0
    for day in range(1, n * m + 1):
        cost, i, j = heappop(available)
        total += cost * day
        if j != m - 1:
            heappush(available, (values[i][j + 1], i, j + 1))

    return total


print(maxSpending(values=[[8, 5, 2], [6, 4, 1], [9, 7, 3]]))

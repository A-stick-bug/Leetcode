# https://leetcode.com/problems/eat-pizzas
# Greedy + sorting

def maxWeight(pizzas: list[int]) -> int:
    n = len(pizzas)

    # remove smaller half
    pizzas.sort()
    larger = pizzas[n // 2:]

    days = n // 4
    odd = days // 2
    even = days - odd

    # always pair largest + smaller on even days
    larger.reverse()
    total = sum(larger[:even])

    larger = larger[even:]
    for _ in range(even):
        larger.pop()

    # must take the smaller of the top 2 on odd days
    total += sum(larger[1::2])

    return total


print(maxWeight([2, 4, 4, 1, 1, 4, 5, 4, 1, 5, 3, 1, 5, 4, 5, 2]))
print(maxWeight([5, 5, 3, 1, 5, 5, 2, 4, 4, 4, 4, 3]))

"""
Not a very elegant solution but it works at least

https://leetcode.com/problems/maximum-elegance-of-a-k-length-subsequence/description/
The constraints tell us that DP will probably TLE, and we need a greedy solution, optimized with heap

First have all categories, then we remove the lowest profit item from our current state and add
the highest profit unused item (without caring about what category they are)

Note: doing this the other way around probably works too (and is probably better)
"""

from heapq import heappop, heappush, heapify


def findMaximumElegance(items: list[list[int]], k: int) -> int:
    n = len(items)
    items.sort(reverse=True)  # sort by profit, decreasing order
    cur = 0

    # first, take the highest from each category
    categories = {}
    used = set()
    for i, (profit, group) in enumerate(items):
        if len(used) >= k:
            break
        if group in categories:  # already have this category
            continue
        categories[group] = 1
        used.add(i)
        cur += profit

    # add extras, take highest profit since we already have one of each category
    i = 0
    a = 0
    while a < k - len(categories):
        if i in used:
            i += 1
            continue
        profit, group = items[i]
        cur += profit
        categories[group] += 1
        used.add(i)
        a += 1
        i += 1

    # now we try to switch out some items from the same categories
    state = [(items[i][0], items[i][1], i) for i in used]
    heapify(state)
    res = cur + len(categories) ** 2

    for i, (profit, group) in enumerate(items):
        if i in used:
            continue
        prev_profit, prev_group, prev_i = heappop(state)  # remove old
        used.remove(prev_i)
        used.add(i)
        cur -= prev_profit
        categories[prev_group] -= 1
        if categories[prev_group] == 0:
            del categories[prev_group]

        heappush(state, (profit, group, i))
        if group not in categories:
            categories[group] = 1
        else:
            categories[group] += 1
        cur += profit

        res = max(res, cur + len(categories) ** 2)

    return res


print(findMaximumElegance(items=[[1, 2], [10, 1]], k=1))

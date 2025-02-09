# https://leetcode.com/problems/assign-elements-to-groups-with-constraints
# looks like O(n^2) brute force but is actually O(nlogn)
# this approach also avoids having to factor which takes O(sqrt(n))

from collections import defaultdict


def assignElements(groups: list[int], elements: list[int]) -> list[int]:
    n = len(groups)
    m = len(elements)
    mx = max(groups)

    locs = defaultdict(list)
    for i, v in enumerate(groups):
        locs[v].append(i)

    vis = set()
    res = [-1] * n
    for i in range(m):
        if elements[i] in vis:
            continue
        vis.add(elements[i])

        for mul in range(elements[i], mx + 1, elements[i]):  # logn on average
            if mul not in locs:
                continue
            for idx in locs[mul]:
                res[idx] = i
            del locs[mul]

    return res


print(assignElements(groups=[8, 4, 3, 2, 4], elements=[4, 2]))
print(assignElements(groups=[2, 3, 5, 7], elements=[5, 3, 3]))
print(assignElements(groups=[10, 21, 30, 41], elements=[2, 1]))

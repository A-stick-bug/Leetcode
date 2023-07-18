from collections import defaultdict


def highFive(items):
    values = defaultdict(list)
    for id, score in items:
        values[id].append(score)

    for k in values.keys():
        values[k].sort(reverse=True)

    res = []
    for id, scores in values.items():
        res.append([id, int(sum(scores[:5]) / 5)])

    return sorted(res, key=lambda x: x[0])


items = [[1, 91], [1, 92], [2, 93], [2, 97], [1, 60], [2, 77], [1, 65], [1, 87], [1, 100], [2, 100], [2, 76]]
print(highFive(items))


import heapq
# using python's maxheap (probably unreliable)
def highFive_max_heap(items):
    values = defaultdict(list)
    for id, score in items:
        values[id].append(score)

    for k in values.keys():
        heapq._heapify_max(values[k])

    res = []
    for id, scores in values.items():
        temp = []
        for _ in range(5):
            temp.append(heapq._heappop_max(values[id]))
        res.append([id, int(sum(temp) / 5)])

    return sorted(res, key=lambda x: x[0])

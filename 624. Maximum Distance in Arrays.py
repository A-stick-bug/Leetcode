from typing import List

# easy to understand solution
def maxDistance(arrays: List[List[int]]) -> int:
    min_v = arrays[0][0]
    max_v = arrays[0][-1]
    res = 0
    for i in range(1, len(arrays)):
        # largest and smallest value cannot be from the same array
        diff = max_v - arrays[i][0]
        diff2 = arrays[i][-1] - min_v
        res = max(diff, diff2, res)  # result will be the biggest value

        if arrays[i][0] < min_v:
            min_v = arrays[i][0]
        if arrays[i][-1] > max_v:
            max_v = arrays[i][-1]

    return res


arrays = [[8,22,30],[100,10000],[1,1]]
print(maxDistance(arrays))

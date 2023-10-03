"""
https://leetcode.com/problems/rectangle-area-ii/description/
Solution using a 2D difference array
- need coordinate compression

Note: because there are so little rectangles (200), using the difference array didn't help much

Time complexityL O(n^2), worse case if all coordinates are unique (max difference array size)
- coordinate compressing takes n*logn from sorting
- building difference array takes O(1) per rectangle, O(n) total
- turning the difference array into a regular array using prefix sums method takes
  (unique x coordinates) * (unique y coordinates)

"""

from typing import List


def rectangleArea(rectangles: List[List[int]]) -> int:
    MOD = 10 ** 9 + 7

    # first, use coordinate compression because we already have all the queries
    all_x = set()
    all_y = set()
    for x1, y1, x2, y2 in rectangles:
        all_x.add(x1)
        all_x.add(x2)
        all_y.add(y1)
        all_y.add(y2)

    all_x = sorted(all_x)
    all_y = sorted(all_y)
    cx = {val: i + 1 for i, val in enumerate(all_x)}  # compress coordinates
    cy = {val: i + 1 for i, val in enumerate(all_y)}

    # use a difference array for O(1) updates per rectangle
    diff = [[0] * (len(cx) + 2) for _ in range(len(cy) + 2)]
    for x1, y1, x2, y2 in rectangles:
        x1, y1, x2, y2 = cx[x1], cy[y1], cx[x2], cy[y2]  # compress coordinates
        diff[y1][x1] += 1  # principle of inclusion and exclusion
        diff[y2][x1] -= 1
        diff[y1][x2] -= 1
        diff[y2][x2] += 1

    # we need to uncompress cells that are covered by a rectangle to get total area
    area = 0
    for i in range(1, len(cy) + 1):
        for j in range(1, len(cx) + 1):
            # principle of exclusion inclusion again
            diff[i][j] += diff[i - 1][j] + diff[i][j - 1] - diff[i - 1][j - 1]
            if diff[i][j] > 0:
                # to get actual area, we need to uncompress the coordinates (l * w)
                area = (area + (all_x[j] - all_x[j - 1]) * (all_y[i] - all_y[i - 1])) % MOD

    return area


print(rectangleArea([[0, 0, 3, 3], [2, 0, 5, 3], [1, 1, 4, 4]]))

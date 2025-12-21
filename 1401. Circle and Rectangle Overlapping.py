# https://leetcode.com/problems/circle-and-rectangle-overlapping
# observations
# - if there is overlap, there must be an overlap at a lattice point
#
# Consider points occupied by both shapes in 1D intervals (group points with same y coordinate)
# We can get each 'slice' of the circle with the Pythagorean theorem
#
# TC: O(r) where r is the radius

from math import sqrt, floor, ceil


class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        def overlap_1d(a, b) -> bool:  # check if a,b overlap
            a, b = sorted([a, b])
            return a[1] >= b[0]

        circle = []  # (y, x1, x2)  slices of the circle
        for y in range(yCenter - radius, yCenter + radius + 1):
            x_sz = sqrt(radius ** 2 - (y - yCenter) ** 2)
            circle.append((y, ceil(xCenter - x_sz), floor(xCenter + x_sz)))

        for y, cx1, cx2 in circle:  # check if any of the circle's slice overlaps with the rectangle
            if y1 <= y <= y2:
                if overlap_1d((cx1, cx2), (x1, x2)):
                    return True
        return False

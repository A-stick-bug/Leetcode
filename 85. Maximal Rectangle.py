"""
for each row, we use the largest rectangle in histogram method to find the maximum area in O(M)
time complexity is O(MN) because there are N rows
space complexity is O(M) because the histogram only takes up 1 row

to convert the matrix to a histogram, we increment by 1 if the value is 1 and set to 0 if it is 0
because a 0 will prevent a rectangle being formed from the bottom
"""

from typing import List


def largest_histogram(heights):
    heights.append(0)  # this will make sure we check remaining elements in stack after iterating all heights
    stack = []
    res = 0
    for i in range(len(heights)):

        # keep stack in increasing order (strict)
        while stack and heights[stack[-1]] >= heights[i]:
            height = heights[stack.pop()]

            # if the stack is empty, then the current height can extend all the way to the left
            width = i if not stack else i - stack[-1] - 1  # minus one because it is the width between 2 points
            res = max(res, height * width)  # check the maximum area we can obtain with current height

        stack.append(i)
    return res


def maximalRectangle(matrix: List[List[str]]) -> int:
    ROWS, COLS = len(matrix), len(matrix[0])
    histogram = [0] * COLS  # build a histogram and update on every row
    max_area = 0

    for row in matrix:
        for c in range(COLS):  # update histogram
            histogram[c] = (histogram[c] + 1) if row[c] == "1" else 0

        # get max area using the current row and every row above it
        max_area = max(max_area, largest_histogram(histogram))

    return max_area


print(maximalRectangle([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))

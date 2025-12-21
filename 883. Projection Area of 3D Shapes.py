# https://leetcode.com/problems/projection-area-of-3d-shapes/description/
# Given stacks of cubes on a 2d grid, find the total area of all 3 axis aligned projections
#
# Note that we could construct a 3d boolean array that stores whether each (x,y,z) is occupied
# but since all stacks are 'grounded', we have easier mathematical methods

def projectionArea(grid: list[list[int]]) -> int:
    area = 0

    # bird eye view, looking from z-axis
    area += sum(sum(i != 0 for i in row) for row in grid)

    # side view, from x-axis
    area += sum(max(row) for row in grid)

    # side view, from y-axis
    area += sum(max(col) for col in list(zip(*grid)))

    return area
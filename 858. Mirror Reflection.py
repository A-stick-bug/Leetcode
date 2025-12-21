# https://leetcode.com/problems/mirror-reflection
# Classic geometry problem with some basic number theory
# Key intuition: instead of reflecting the line, we reflect the entire room
# Note that each point at (xp, yp) for integers x,y is a corner
# We can determine which corner it corresponds to through the parity of x and y

from math import lcm


def mirrorReflection(p: int, q: int) -> int:
    # suppose the bottom-left is (0,0)
    y_dist = lcm(p, q)  # y coord of first corner
    x_dist = (y_dist // q) * p  # x coord of first corner
    y_parity = (y_dist // p) % 2
    x_parity = (x_dist // p) % 2
    if x_parity == 1 and y_parity == 0:
        return 0
    if x_parity == y_parity == 1:
        return 1
    else:  # we can do this since they guarantee it hits one of the 3 corners
        return 2

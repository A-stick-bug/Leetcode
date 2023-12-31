"""
https://leetcode.com/problems/number-of-ships-in-a-rectangle/description/
Interactive problem, when you see one of these, first thing to consider is divide and conquer

- In this problem, we start off by querying the entire region and if there are ships in that region, we split it
  into 4 quadrants and check those
- The base case is if our region is 1 point, in which case there can
  be 0 or 1 ship there
- Also, there is no need to recur further if there are no ship in the region

"""


class Sea:
    def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
        return True  # placeholder for testing purposes


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


def countShips(sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
    def solve(x1, y1, x2, y2):
        if x1 < x2 or y1 < y2:  # invalid query
            return 0
        if not sea.hasShips(Point(x1, y1), Point(x2, y2)):  # no ships in the region, don't recurse more
            return 0
        if x1 == x2 and y1 == y2:  # there is a ship on this individual point (and we know there can only be 1)
            return 1

        # there is one or more ships in this region, we need to recurse more
        mid_x = (x1 + x2) // 2
        mid_y = (y1 + y2) // 2
        return sum([solve(x1, y1, mid_x + 1, mid_y + 1),
                    solve(mid_x, mid_y, x2, y2),
                    solve(mid_x, y1, x2, mid_y + 1),
                    solve(x1, mid_y, mid_x + 1, y2)])

    return solve(topRight.x, topRight.y, bottomLeft.x, bottomLeft.y)


print(countShips(Sea(), Point(4, 4), Point(0, 0)))

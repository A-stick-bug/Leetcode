"""
https://leetcode.com/problems/car-fleet
Hint: plotting each car as time on X axis and position on Y is very helpful
Sample 1: https://www.desmos.com/calculator/yduxhht549

- sort by distance to target
- loop cars
  - if current intersects with the previous, simply ignore it
    - we can do this because anything that intersects with the current
      will also intersect with the previous
  - otherwise, set previous = current, as the current is guaranteed
    to intersect with everything that will intersect with the previous and more
"""


def carFleet(target: int, position: list[int], speed: list[int]) -> int:
    def intersects(pos1, speed1, pos2, speed2):  # assumes pos1 > pos2
        if speed1 >= speed2:
            return False
        reach1 = (target - pos1) / speed1  # when car1 reaches target
        reach2 = (target - pos2) / speed2  # when car1 reaches target
        return reach2 <= reach1

    cars = list(zip(position, speed))
    cars.sort(key=lambda x: x[0], reverse=True)  # by distance from target

    total = 1
    prev_pos, prev_v = cars[0]
    for pos, v in cars[1:]:
        if not intersects(prev_pos, prev_v, pos, v):
            prev_pos, prev_v = pos, v
            total += 1

    return total


print(carFleet(target=12, position=[10, 8, 0, 5, 3], speed=[2, 4, 1, 1, 3]))

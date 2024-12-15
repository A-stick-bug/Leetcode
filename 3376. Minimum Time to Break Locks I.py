# notice the low constraints
# brute force permutations, optimize each step in `solve` with math just in case

from itertools import permutations


def findMinimumTime(strength: list[int], K: int) -> int:
    def solve(arr):
        inc = 1
        time = 0
        for i in range(len(arr)):
            moves = (arr[i] + inc - 1) // inc  # ceil division
            time += moves
            inc += K
        return time

    return min(solve(p) for p in permutations(strength))


print(findMinimumTime(strength=[3, 4, 1], K=1))
print(findMinimumTime(strength=[2, 5, 4], K=2))

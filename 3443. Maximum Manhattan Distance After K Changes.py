# https://leetcode.com/problems/maximum-manhattan-distance-after-k-changes/
# keep track of prefix frequencies

from collections import Counter


def maxDistance(s: str, k: int) -> int:
    dir_map = {"S": (1, 0), "N": (-1, 0), "W": (0, -1), "E": (0, 1)}

    x = 0
    y = 0
    best = 0
    moves = Counter()

    for c in s:
        dx, dy = dir_map[c]
        moves[c] += 1
        x += dx
        y += dy

        mx, mi = max(moves["N"], moves["S"]), min(moves["N"], moves["S"])
        mx2, mi2 = max(moves["W"], moves["E"]), min(moves["W"], moves["E"])

        best = max(best, abs(x) + abs(y) + min(k, mi + mi2) * 2)

    return best


print(maxDistance(s="NWSE", k=1))
print(maxDistance(s="NSWWEW", k=3))

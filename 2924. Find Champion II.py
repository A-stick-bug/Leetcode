# https://leetcode.com/problems/find-champion-ii
# simple logic, don't need graph theory

def findChampion(n: int, edges: list[list[int]]) -> int:
    champion = [True] * n
    for a, b in edges:
        champion[b] = False

    if champion.count(True) > 1:
        return -1
    return champion.index(True)

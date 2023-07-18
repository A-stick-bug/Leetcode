from typing import List

# no space optimization
def findLonelyPixel(picture: List[List[str]]) -> int:
    r,c = len(picture), len(picture[0])
    rows = [0 for _ in range(r)]
    cols = [0 for _ in range(c)]
    for i in range(r):
        for j in range(c):
            if picture[i][j] == "B":
                rows[i] += 1
                cols[j] += 1

    res = 0
    for i in range(r):
        for j in range(c):
            if picture[i][j] == "B" and rows[i] == 1 and cols[j] == 1:
                res += 1
    return res

picture = [["W","W","B"],["W","B","W"],["B","W","W"]]
print(findLonelyPixel(picture))

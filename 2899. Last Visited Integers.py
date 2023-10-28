from typing import List


def lastVisitedIntegers(words: List[str]) -> List[int]:
    res = []
    vis = []
    prev = 0

    for w in words:
        if w == "prev":
            prev += 1
            if prev > len(vis):
                res.append(-1)
            else:
                res.append(vis[-prev])

        else:
            vis.append(int(w))
            prev = 0

    return res


print(lastVisitedIntegers(words = ["1","prev","2","prev","prev"]))

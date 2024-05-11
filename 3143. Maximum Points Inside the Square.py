def maxPointsInsideSquare(points, s: str) -> int:
    n = len(points)
    for i in range(n):
        points[i].append(s[i])

    loc = lambda x: max(abs(x[0]), abs(x[1]))

    points.sort(key=lambda x: loc(x))
    best = 0

    seen = set()
    i = 0
    while i < n:
        le = loc(points[i])
        while i < n and loc(points[i]) == le:
            if points[i][2] in seen:
                return best
            seen.add(points[i][2])
            i += 1
        best = max(best, i)

    return best


print(maxPointsInsideSquare(points=[[2, 2], [-1, -2], [-4, 4], [-3, 1], [3, -3]], s="abdca"))
print(maxPointsInsideSquare(points=[[1, 1], [-2, -2], [-2, 2]], s="abb"))
print(maxPointsInsideSquare(points=[[1, 1], [-1, -1], [2, -2]], s="ccd"))

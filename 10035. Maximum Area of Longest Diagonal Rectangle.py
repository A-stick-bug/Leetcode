def areaOfMaxDiagonal(dimensions) -> int:
    dimensions.sort(key=lambda x: (x[0] * x[0] + x[1] * x[1], x[0] * x[1]))
    return dimensions[-1][0] * dimensions[-1][1]


print(areaOfMaxDiagonal(dimensions=[[9, 3], [8, 6]]))

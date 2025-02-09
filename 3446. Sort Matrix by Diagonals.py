def sortMatrix(grid: list[list[int]]) -> list[list[int]]:
    def sort_diagonal(r, c, rev):
        values = []
        i, j = r, c
        while i < n and j < n:
            values.append(grid[i][j])
            i += 1
            j += 1
        values.sort(reverse=rev)
        i, j = r, c
        idx = 0
        while i < n and j < n:
            grid[i][j] = values[idx]
            i += 1
            j += 1
            idx += 1

    n = len(grid)
    for i in range(1, n):
        sort_diagonal(0, i, False)
    for i in range(n):
        sort_diagonal(i, 0, True)

    return grid


print(sortMatrix(grid=[[1, 7, 3], [9, 8, 2], [4, 5, 6]]))
print(sortMatrix(grid=[[0, 1], [1, 2]]))
print(sortMatrix(grid=[[1]]))

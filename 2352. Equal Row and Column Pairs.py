from collections import Counter


def equalPairs(grid):
    count = 0
    rows = Counter([tuple(row) for row in grid])  # create a counter of how many times each row appears

    # rotate array so that it's easier and faster to get the tuple of each column
    grid = zip(*grid)
    for col in grid:
        if tuple(col) in rows:
            # if row that the column is equal to appears multiple times, add the amount of times the row appears
            count += rows[col]
    return count


print(equalPairs(grid=[[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]]))

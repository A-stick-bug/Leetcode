"""
There are N-queens we need to place on a NxN board, therefore, we need 1 queen on each row.

- diagonal \, all (row, col) have the same (\) diagonal if its (row - col) is the same
- diagonal /, all (row, col) have the same (/) diagonal if its (row + col) is the same

"""


def totalNQueens(n: int) -> int:
    total = 0

    # for each row, try putting a queen in all columns
    def dfs_backtrack(row, cols, d1, d2):
        nonlocal total
        if row == n:
            total += 1
            return

        for col in range(n):
            if col in cols or (row - col) in d1 or (row+col) in d2:  # invalid state, no need to search further
                continue
            cols.add(col)
            d1.add(row - col)
            d2.add(row + col)
            dfs_backtrack(row + 1, cols, d1, d2)
            cols.remove(col)
            d1.remove(row - col)
            d2.remove(row + col)

    dfs_backtrack(0, set(), set(), set())
    return total


print(totalNQueens(4))

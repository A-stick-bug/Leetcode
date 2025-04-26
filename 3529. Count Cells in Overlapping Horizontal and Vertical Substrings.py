# https://leetcode.com/problems/count-cells-in-overlapping-horizontal-and-vertical-substrings
# First flatten the grid into an array, both vertically and horizontally
# Then use a string matching algorithm such as the Z-algorithm to search for the pattern
# We can use some math to map the array indices back to the grid indices


def countCells(grid: list[list[str]], pattern: str) -> int:
    def z_algorithm(s):
        n = len(s)
        z = [0] * n
        l = r = 0
        for i in range(1, n):
            if l <= i <= r:
                if i + z[i - l] - 1 < r:
                    z[i] = z[i - l]
                else:
                    z[i] = r - i + 1
                    l = i
                    for j in range(r + 1, n):
                        if s[j - i] == s[j]:
                            z[i] += 1
                            r = j
                        else:
                            break
            else:
                l = i
                for j in range(i, n):
                    if s[j - i] == s[j]:
                        z[i] += 1
                        r = j
                    else:
                        break
        return z

    # match horizontally
    s_rows = []
    for row in grid:
        s_rows.append("".join(row))
    s_rows = "".join(s_rows)

    n = len(s_rows)
    m = len(pattern)

    match_row = pattern + "!" + "".join(s_rows)
    z_row = z_algorithm(match_row)
    r_idx = -1
    works_row = [False] * n
    for i in range(m + 1, n + m + 1):
        if z_row[i] == m:  # matches
            r_idx = i + m - 1
        if r_idx >= i:
            works_row[i - (m + 1)] = True

    # match vertically
    s_cols = []
    for col in list(zip(*grid)):
        s_cols.append("".join(col))
    s_cols = "".join(s_cols)

    match_col = pattern + "!" + "".join(s_cols)
    z_col = z_algorithm(match_col)
    r_idx = -1
    works_col = [False] * n
    for i in range(m + 1, n + m + 1):
        if z_col[i] == m:  # matches
            r_idx = i + m - 1
        if r_idx >= i:
            works_col[i - (m + 1)] = True

    # print(works_col)
    # print(works_row)

    # put the vertical and horizontal matches back on the grid
    R = len(grid)
    C = len(grid[0])
    works_grid = [[0] * C for _ in range(R)]
    for i in range(n):
        if works_row[i]:
            works_grid[i // C][i % C] += 1
    for i in range(n):
        if works_col[i]:
            works_grid[i % R][i // R] += 1

    # for i in works_grid:
    #     print(i)

    return sum(sum(i == 2 for i in row) for row in works_grid)


print(countCells(
    grid=[["a", "a", "c", "c"], ["b", "b", "b", "c"], ["a", "a", "b", "a"], ["c", "a", "a", "c"], ["a", "a", "c", "c"]],
    pattern="abaca"))

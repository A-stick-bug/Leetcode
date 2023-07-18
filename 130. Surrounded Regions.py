def solve(board):
    rows = len(board)
    cols = len(board[0])
    keep = set()

    def dfs(row, col):
        if row < 0 or col < 0 or col >= cols or row >= rows or board[row][col] == "X" or (row, col) in keep:
            return

        keep.add((row, col))
        dfs(row - 1, col)
        dfs(row, col - 1)
        dfs(row + 1, col)
        dfs(row, col + 1)

    # keep track of which "O"s to keep
    for i in range(rows):
        dfs(i, 0)
        dfs(i, cols - 1)
    for i in range(cols):
        dfs(0, i)
        dfs(rows - 1, i)

    # removing all other "O"s (not in keep)
    for i in range(rows):
        for j in range(cols):
            if board[i][j] == "O" and (i, j) not in keep:
                board[i][j] = "X"
    return board


board = [["X", "O", "X", "O", "X", "O"],
         ["O", "X", "O", "X", "O", "X"],
         ["X", "O", "X", "O", "X", "O"],
         ["O", "X", "O", "X", "O", "X"]]


print(solve(board))

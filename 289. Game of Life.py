def gameOfLife(board):
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]

    def get_adj(i, j):
        count = 0
        for di, dj in directions:
            if m > i + di >= 0 and n > j + dj >= 0 and board[i + di][j + dj] != 0 and board[i + di][j + dj] != 2:
                count += 1
        return count

    m, n = len(board), len(board[0])
    for i in range(m):
        for j in range(n):

            adj = get_adj(i, j)
            if board[i][j] == 1:
                if adj != 2 and adj != 3:
                    board[i][j] = -1  # represent die next round

            elif adj == 3:
                board[i][j] = 2  # represent alive next round

    for i in range(m):
        for j in range(n):
            if board[i][j] == 2:
                board[i][j] = 1
            elif board[i][j] == -1:
                board[i][j] = 0
    return board


board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
print(gameOfLife(board))

def exists(board, word):
    rows, cols = len(board), len(board[0])
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

    # each cell can only be used once when searching, keep track using a set()
    def search(row, col, index):
        # found word
        if index == len(word):
            return True

        # out of bounds or already visited
        if row < 0 or col < 0 or row >= len(board) or col >= len(board[0]) or board[row][col] != word[index]:
            return False

        temp = board[row][col]
        board[row][col] = "#"  # mark as visited
        for r, c in directions:
            if search(row + r, col + c, index + 1):
                return True

        board[row][col] = temp  # if the cell is not usable, backtrack
        return False

    for i in range(rows):
        for j in range(cols):
            if search(i, j, 0):
                return True

    return False


board = [["A", "B", "C", "E"],
         ["S", "F", "C", "S"],
         ["A", "D", "E", "E"]]
word = "ABCB"

print(exists(board, word))

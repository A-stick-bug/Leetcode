# can use collections.Counter() and check if a letter in the word appears more times than it appears on the board

def exists(board, word):
    rows, cols = len(board), len(board[0])
    used = [[False for _ in range(cols)] for _ in range(rows)]
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

    # each cell can only be used once when searching, keep track using a set()
    def search(row, col, index, used):
        # found word
        if index == len(word):
            return True

        # out of bounds or already visited
        if row < 0 or col < 0 or row >= len(board) or col >= len(board[0]) or used[row][col] or board[row][col] != word[index]:
            return False

        # if the cell is not usable, backtrack
        used[row][col] = True
        for r, c in directions:
            if search(row + r, col + c, index + 1, used):
                return True

        used[row][col] = False
        return False

    for i in range(rows):
        for j in range(cols):
            if search(i, j, 0, used):
                return True
    return False


board = [["A", "B", "C", "E"],
         ["S", "F", "C", "S"],
         ["A", "D", "E", "E"]]
word = "ABCB"

print(exists(board, word))

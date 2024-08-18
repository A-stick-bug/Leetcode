# could only possibly take max 3 elements from each row

from itertools import combinations, permutations


def maximumValueSum(board: list[list[int]]) -> int:
    n = len(board)
    m = len(board[0])

    for i in range(n):  # each row has top 3 values and the columns they belong in
        board[i] = [(val, i) for i, val in enumerate(board[i])]
        board[i].sort(key=lambda x: x[0], reverse=True)
        board[i] = board[i][:3]

    pp = [(0, 0, 0), (0, 0, 1), (0, 0, 2), (0, 1, 0), (0, 1, 1), (0, 1, 2), (0, 2, 0), (0, 2, 1), (0, 2, 2), (1, 0, 0),
          (1, 0, 1), (1, 0, 2), (1, 1, 0), (1, 1, 1), (1, 1, 2), (1, 2, 0), (1, 2, 1), (1, 2, 2), (2, 0, 0), (2, 0, 1),
          (2, 0, 2), (2, 1, 0), (2, 1, 1), (2, 1, 2), (2, 2, 0), (2, 2, 1), (2, 2, 2)]

    inf = 1 << 60
    best = -inf

    for row1 in range(n):
        for row2 in range(row1 + 1, n):
            for row3 in range(row2 + 1, n):
                comb_rows = [row1, row2, row3]
                for indices in pp:  # select column order for each row
                    elements = [board[comb_rows[i]][indices[i]] for i in range(3)]
                    if elements[0][1] != elements[1][1] and elements[1][1] != elements[2][1] and elements[0][1] != \
                            elements[2][1]:
                        best = max(best, sum(elements[i][0] for i in range(3)))

    return best


print(maximumValueSum(board=[[-3, 1, 1, 1], [-3, 1, -3, 1], [-3, 2, 1, 1]]))
print(maximumValueSum(board=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(maximumValueSum(board=[[1, 1, 1], [1, 1, 1], [1, 1, 1]]))

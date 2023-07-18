from collections import deque


def letterCombinations(digits):
    letters = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }

    if not digits:
        return []

    q = deque(letters[digits[0]])

    for c in range(1, len(digits)):  # for every letter
        for _ in range(len(q)):
            tmp = q.popleft()
            for i in letters[digits[c]]:  # add every possible letter
                q.append(tmp + i)
    return q

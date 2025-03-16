from itertools import permutations


def totalNumbers(digits: list[int]) -> int:
    res = set()
    for perm in permutations(digits, 3):
        if perm[0] != 0 and perm[-1] % 2 == 0:
            res.add(perm)
    return len(res)


print(totalNumbers([1, 6, 2, 8, 7]))
print(totalNumbers([1, 2, 3, 4]))
print(totalNumbers([0, 2, 2]))
print(totalNumbers([6, 6, 6]))
print(totalNumbers([1, 3, 5]))

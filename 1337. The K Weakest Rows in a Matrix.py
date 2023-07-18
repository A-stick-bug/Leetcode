# slightly optimized
def kWeakestRows(mat, k):
    def binary_search(row):
        low = 0
        high = len(mat[0])
        while low < high:
            mid = low + (high - low) // 2
            if row[mid] == 1:
                low = mid + 1
            else:
                high = mid
        return low

    weakest = [(binary_search(row), i) for i, row in enumerate(mat)]
    weakest.sort(key=lambda x: x[0])
    return list(map(lambda x: x[1], weakest[:k]))


mat = [[1, 1, 0, 0, 0], [1, 1, 1, 1, 0], [1, 0, 0, 0, 0], [1, 1, 0, 0, 0], [1, 1, 1, 1, 1]]
k = 3
print(kWeakestRows(mat, k))


# brute force, bad solution
def brute_force(mat, k):
    weakest = {}
    index = 0

    for i in mat:
        weak = i.count(0)
        weakest[index] = weak

        index += 1

    x = sorted(weakest.items(), key=lambda x: x[1], reverse=True)
    new = dict(x)

    arr = []

    for x in new.keys():
        arr.append(x)

    return arr[:k]

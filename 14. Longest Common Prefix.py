# character matching

def longest(strs):
    shortest = len(min(strs, key=len))
    prefix = ""
    for i in range(shortest):
        current = strs[0][i]

        for j in range(1, len(strs)):
            if strs[j][i] != current:
                return prefix

        prefix += current

    return prefix


strs = ["ab", "a"]
print(longest(strs))
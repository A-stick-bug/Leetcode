# Linear time solution, be careful when indexing lists

def longest(s):
    longest = 1

    if s == "":
        return 0

    letters = []
    for i in s:
        if i not in letters:
            letters.append(i)

        else:
            if len(letters) > longest:
                longest = len(letters)

            letters = letters[letters.index(i)+1:]

            letters.append(i)

        if len(letters) > longest:
            longest = len(letters)

    return longest

s = "aabaab!bb"
print(longest(s))
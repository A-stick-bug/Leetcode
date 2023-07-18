def wordPattern(pattern, s):
    s = s.split()
    pattern = list(pattern)
    hash = {}

    if not pattern or not s:
        return False
    if len(s) != len(pattern):
        return False

    for i in range(len(pattern)):
        if pattern[i] in hash:
            if hash[pattern[i]] != s[i]:
                return False
        else:
            if s[i] in hash.values():
                return False

            hash[pattern[i]] = s[i]

    return True


pattern = "abba"
s = "dog cat cat yu"
print(wordPattern(pattern, s))

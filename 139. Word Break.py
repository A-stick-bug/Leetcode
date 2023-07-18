# review this later

def wordBreak(s,wordDict):
    bools = [False] * (len(s) + 1)
    bools[0] = True

    for i in range(1, len(s) + 1):
        for j in range(i):
            if bools[j] and s[j:i] in wordDict:
                bools[i] = True
                break

    return bools[-1]


print(wordBreak('cog',["og","c"]))


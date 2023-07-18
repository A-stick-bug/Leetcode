def truncateSentence(s,k):
    i = 0
    while i < len(s) and k > 0:
        if s[i] == " ":
            k -= 1
        i += 1
    return s[:i].strip()


print(truncateSentence("Hello World a b c",3))

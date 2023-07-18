def validPalindrome(s: str) -> bool:
    if s == s[::-1]:
        return True

    start, end = 0, len(s) - 1
    check = 0
    while end > start:
        if s[end] != s[start]:
            if s[start+1:end+1] == s[start+1:end+1][::-1]:
                return True
            elif s[start:end] == s[start:end][::-1]:
                return True
            else:
                return False

        start += 1
        end -= 1

    return True


s = "abc"
print(validPalindrome(s))

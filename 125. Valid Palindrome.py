# instead of using 2 pointers, can also return s == s[::-1] (reverse)

def isPalindrome(s) -> bool:
    s = s.lower()
    for i in s:
        if not i.isalpha() or not i.isalnum():
            s = s.replace(i, "")

    start = 0
    end = len(s) - 1
    while end > start:
        if s[start] != s[end]:
            return False

        start += 1
        end -= 1

    return True

s = "0P"
print(isPalindrome(s))

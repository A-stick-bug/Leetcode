# for two pointers, can also use "while end > start:"

def reverseString(s):
    start = 0
    end = len(s) - 1

    for i in range(len(s) // 2):
        s[start], s[end] = s[end], s[start]
        start += 1
        end -= 1

    return s

s = ["h","e","l","l","o"]
print(reverseString(s))
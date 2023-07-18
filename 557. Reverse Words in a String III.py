def reverseWords(s: str) -> str:
    new = ""
    for i in s.split():
        new += i[::-1] + " "

    return new

print(reverseWords("Hello World"))
def replaceDigits(s: str) -> str:
    cut = False  # if last value is not a number
    if len(s) % 2 != 0:
        cut = True
        temp = s[-1]
        s = s[:-1]

    new = ""
    for i in range(0, len(s), 2):
        new += s[i]+chr(ord(s[i]) + int(s[i+1]))

    if cut:
        return new+temp

    return new


s = "a1b2c3d4e"
print(replaceDigits(s))
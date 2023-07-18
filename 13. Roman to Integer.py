# could use dict

value = 0
s = "LVIII"

while s:
    if "CM" in s:
        value += 900
        s = s.replace("CM", "", 1)
    elif "CD" in s:
        value += 400
        s = s.replace("CD", "", 1)
    elif "XL" in s:
        value += 40
        s = s.replace("XL", "", 1)
    elif "XC" in s:
        value += 90
        s = s.replace("XC", "", 1)
    elif "IX" in s:
        value += 9
        s = s.replace("IX", "", 1)
    elif "IV" in s:
        value += 4
        s = s.replace("IV", "", 1)
    elif "M" in s:
        value += 1000
        s = s.replace("M", "", 1)
    elif "D" in s:
        value += 500
        s = s.replace("D", "", 1)
    elif "C" in s:
        value += 100
        s = s.replace("C", "", 1)
    elif "L" in s:
        value += 50
        s = s.replace("L", "", 1)
    elif "X" in s:
        value += 10
        s = s.replace("X", "", 1)
    elif "V" in s:
        value += 5
        s = s.replace("V", "", 1)
    elif "I" in s:
        value += 1
        s = s.replace("I", "", 1)

print(value)

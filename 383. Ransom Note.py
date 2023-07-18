# remember that string are immutable, must use x = [string function on x]

ransomNote = "aa"
magazine = "aab"

value = True

for i in ransomNote:
    if i in magazine:
        ransomNote = ransomNote.replace(i, "", 1)
        magazine = magazine.replace(i, "", 1)
    else:
        value = False
        break

if ransomNote or value == False:
    print(False)
else:
    print(value)

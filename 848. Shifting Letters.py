# keep track of variables more carefully

def shiftingLetters(s, shifts):
    s = list(s)
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    for i in reversed(range(len(shifts) - 1)):
        shifts[i] += shifts[i + 1]

    shift = 0

    for letter in range(len(s)):
        letter_index = alphabet.index(s[letter])

        s[letter] = alphabet[(letter_index + shifts[shift])%26]

        shift += 1

    return "".join(s)

s = "bad"
shifts = [10,20,30]

print(shiftingLetters(s, shifts))

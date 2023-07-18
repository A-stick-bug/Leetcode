def plus_one(digits):
    digits = list(map(str, digits))  # makes all values strings
    digits = "".join(digits)  # turns list into a string

    digits = int(digits)  # turns digits into int
    digits += 1  # increase digits by one
    digits = str(digits)  # cast to string (int cannot be directly cast to list)
    digits = list(map(int, digits))  # cast all values in list to int

    return digits  # turn string into a list


digits = [4,3,2,1]
print(plus_one(digits))
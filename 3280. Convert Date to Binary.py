def convertDateToBinary(date: str) -> str:
    date = date.split('-')
    date = list(map(lambda x: bin(int(x))[2:], date))
    return "-".join(map(str, date))


print(convertDateToBinary(date="1900-01-01"))

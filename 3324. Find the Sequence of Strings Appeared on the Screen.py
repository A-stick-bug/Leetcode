# simple implementation

def stringSequence(target: str) -> list[str]:
    res = [""]
    for i in range(len(target)):
        res.append(res[-1] + "a")
        while target[:i + 1] != res[-1]:
            n_res = res[-1]
            n_res = n_res[:-1] + chr(ord(n_res[-1]) + 1)
            res.append(n_res)
    return res[1:]


print(stringSequence("he"))

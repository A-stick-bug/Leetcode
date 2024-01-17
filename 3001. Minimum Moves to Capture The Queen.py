def minMovesToCaptureTheQueen(a: int, b: int, c: int, d: int, e: int, f: int) -> int:
    dir_k = [(0,1),(1,0),(-1,0),(0,-1)]
    dir_b = [(1,1),(-1,-1),(1,-1),(-1,1)]

    for dr ,dc in dir_k:
        rr, cc = a, b
        while 1 <= rr <= 8 and 1 <= cc <= 8:
            if (rr,cc) == (c,d):
                break
            if (rr,cc) == (e,f):
                return 1
            rr += dr
            cc += dc

    for dr ,dc in dir_b:
        rr, cc = c, d
        while 1 <= rr <= 8 and 1 <= cc <= 8:
            if (rr,cc) == (a, b):
                break
            if (rr,cc) == (e,f):
                return 1
            rr += dr
            cc += dc

    return 2

print(minMovesToCaptureTheQueen(a = 1, b = 1, c = 1, d = 4, e = 1, f = 8))

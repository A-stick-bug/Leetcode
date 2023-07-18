def isSubsequence(s,t):
    s_pointer = 0
    t_pointer = 0
    while t_pointer < len(t) and s_pointer < len(s):
        if s[s_pointer] == t[t_pointer]:
            s_pointer += 1
        t_pointer += 1

    return s_pointer == len(s)


s = "abc"
t = "ahbgdc"
print(isSubsequence(s,t))

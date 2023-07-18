def validParentheses(s):
    match = {')': '(', ']': '[', '}': '{'}
    start = {"(","[","{"}

    stack = []
    for c in s:
        if c in start:
            stack.append(c)
        else:
            if not stack or match[c] != stack.pop():
                return False
    return not stack

print(validParentheses(list("((({{{}}})))")))

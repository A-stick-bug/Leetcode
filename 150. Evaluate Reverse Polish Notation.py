# excellent problem, tests your knowledge on stacks and very fun

def evalRPN(tokens) -> int:
    stack = []
    for token in tokens:
        if token == "+":
            b = int(stack.pop())
            a = int(stack.pop())
            stack.append(a + b)
        elif token == "-":
            b = int(stack.pop())
            a = int(stack.pop())
            stack.append(a - b)
        elif token == "*":
            b = int(stack.pop())
            a = int(stack.pop())
            stack.append(a * b)
        elif token == "/":
            b = int(stack.pop())
            a = int(stack.pop())
            stack.append(a / b)
        else:
            stack.append(token)

    return int(stack[0])

test = "3 2 1 + - 9 -".split()
print(evalRPN(test))

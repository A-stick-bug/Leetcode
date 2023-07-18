# watch out for 0s when doing math related problems
n = 3 # value to change

out = []

for i in range(n + 1):
    if i != 0:
        if i % 15 == 0:
            out.append("FizzBuzz")
        elif i % 3 == 0:
            out.append("Fizz")
        elif i % 5 == 0:
            out.append("Buzz")
        else:
            out.append(str(i))

print(out)

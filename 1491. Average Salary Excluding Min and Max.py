def average(salary):
    salary.remove(max(salary))
    salary.remove(min(salary))
    total = 0

    for i in salary:  # find total
        total += i

    return total / len(salary)  # return mean


salary = [4000, 3000, 1000, 2000]
print(average(salary))

def factorial(x):
    if x == 1:
        return 1
    elif x == 0:
        return 1
    else:
        total = 0
        print x
        for n in range(1,x):
            total = total * n
        return total

print factorial(4)

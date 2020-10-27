def factorial(n):
    if n == 1:
        return 1
    elif n == 0:
        return 1
    else:
        return n*factorial(n-1)


for i in range(0, 11):
    print(f"the factorial of {i} equals to {factorial(i)}")
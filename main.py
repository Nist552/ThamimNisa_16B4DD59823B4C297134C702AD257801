#1.1 Implement a recursive funtion to calculate factorial of a given number

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


result = factorial(5)
print("Factorial of 5 is:", result)

'''Write a Python function to calculate the factorial of a number (a 
nonnegative integer) '''

def factorial(n):
   
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


number = 5
print(f"The factorial of {number} is {factorial(number)}.")

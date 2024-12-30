# Write a Python program to returns sum of all divisors of a number  

def sum_of_divisors(n):
    
    if n <= 0:
        raise ValueError("Number must be positive.")
    
   
    total = sum(i for i in range(1, n + 1) if n % i == 0)
    return total


number = 12 
result = sum_of_divisors(number)
print(f"The sum of all divisors of {number} is {result}.")

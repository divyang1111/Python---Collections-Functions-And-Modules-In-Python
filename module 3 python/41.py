# Write a Python function to check whether a number is perfect or not.

def is_perfect_number(n):
    
    if n <= 0:
        return False
    
   
    divisor_sum = sum(i for i in range(1, n) if n % i == 0)
    
    
    return divisor_sum == n


number = 28
if is_perfect_number(number):
    print(f"{number} is a perfect number.")
else:
    print(f"{number} is not a perfect number.")

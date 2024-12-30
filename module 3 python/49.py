'''Write a Python program to find the maximum and minimum numbers 
from the specified decimal numbers.'''

def find_max_min(numbers):
   
    if not numbers:
        raise ValueError("The list of numbers cannot be empty.")
    
    max_number = max(numbers)
    min_number = min(numbers)
    
    return max_number, min_number


decimal_numbers = [1.5, 2.7, 3.9, 0.4, 5.6, 2.3]
max_num, min_num = find_max_min(decimal_numbers)

print(f"The maximum number is: {max_num}")
print(f"The minimum number is: {min_num}")
  

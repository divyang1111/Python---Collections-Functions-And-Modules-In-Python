'''Write a Python function to get the largest number, smallest num and sum 
of all from a list.'''

def analyze_numbers(numbers):
    if not numbers:
        return "The list is empty. Please provide a list with numbers."
    
    largest = max(numbers)
    smallest = min(numbers)
    total_sum = sum(numbers)

    return largest, smallest, total_sum


numbers = [10, 5, 23, 7, 42, -3]
largest, smallest, total = analyze_numbers(numbers)
print(f"Largest: {largest}, Smallest: {smallest}, Sum: {total}")

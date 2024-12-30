# Write a Python function to check whether a number is in a given range

def is_in_range(number, start, end):
    
    return start <= number <= end


num = 5
range_start = 1
range_end = 10

if is_in_range(num, range_start, range_end):
    print(f"{num} is in the range [{range_start}, {range_end}].")
else:
    print(f"{num} is not in the range [{range_start}, {range_end}].")

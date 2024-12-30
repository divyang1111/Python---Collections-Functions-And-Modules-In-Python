#Write a Python program to find the second smallest number in a list. 

def second_smallest(numbers):
   
    unique_numbers = sorted(set(numbers))
    if len(unique_numbers) < 2:
        return "There is no second smallest number."
    else:
        return unique_numbers[1]


my_list = [10, 20, 4, 5, 1, 20, 4]
result = second_smallest(my_list)
print(f"The second smallest number is: {result}")

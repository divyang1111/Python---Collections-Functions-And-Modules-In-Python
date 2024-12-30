#Write a Python program to convert a tuple to a string.

def tuple_to_string(input_tuple):
    
    return ''.join(map(str, input_tuple))


my_tuple = (1, 2, 3, 'hello', 4)
result_string = tuple_to_string(my_tuple)
print(f"Converted string: {result_string}")

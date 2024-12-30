#Write a Python program to create a tuple with different data types.

def create_mixed_tuple():
    
    mixed_tuple = (42, "Hello", 3.14, True, [1, 2, 3], {"key": "value"})
    return mixed_tuple


result_tuple = create_mixed_tuple()
print(f"Tuple with different data types: {result_tuple}")

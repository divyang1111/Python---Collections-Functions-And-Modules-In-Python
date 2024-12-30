#Write a Python program to map two lists into a dictionary

def map_lists_to_dict(keys, values):
   
    return dict(zip(keys, values))


keys = ['a', 'b', 'c', 'd']
values = [1, 2, 3, 4]

result_dict = map_lists_to_dict(keys, values)
print(f"Mapped dictionary: {result_dict}")

#Write a Python program to remove an empty tuple(s) from a list of tuples. 

def remove_empty_tuples(tuple_list):
    
    return [t for t in tuple_list if t]


tuple_list = [(1, 2), (), (3, 4), (), (5, 6)]
result = remove_empty_tuples(tuple_list)
print(f"List after removing empty tuples: {result}")

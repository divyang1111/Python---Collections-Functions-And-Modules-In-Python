#Write a Python program to replace last value of tuples in a list.

def replace_last_value_of_tuples(tuple_list, new_value):
    
    new_list = [t[:-1] + (new_value,) for t in tuple_list]
    return new_list


tuple_list = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
new_value = 99
result = replace_last_value_of_tuples(tuple_list, new_value)
print(f"Updated list of tuples: {result}")

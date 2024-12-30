'''Write a Python function that takes a list and returns a new list with unique 
elements of the first list. '''

def get_unique_elements(input_list):
    
    return list(set(input_list))


original_list = [1, 2, 2, 3, 4, 5, 5, 6]
unique_list = get_unique_elements(original_list)
print(f"Original List: {original_list}")
print(f"List with unique elements: {unique_list}")

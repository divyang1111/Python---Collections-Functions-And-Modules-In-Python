#Write a Python program to check a list is empty or not.

def remove_duplicates(input_list):
    # Convert the list to a set to remove duplicates, then back to a list
    return list(set(input_list))


original_list = [1, 2, 3, 2, 4, 1, 5, 6, 3]
unique_list = remove_duplicates(original_list)
print(f"Original List: {original_list}")
print(f"List without duplicates: {unique_list}")

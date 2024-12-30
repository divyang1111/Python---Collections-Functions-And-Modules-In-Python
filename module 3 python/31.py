#Write a Python script to merge two Python dictionarie

def merge_dicts(dict1, dict2):
    
    merged_dict = {**dict1, **dict2}
    return merged_dict


dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

merged_dict = merge_dicts(dict1, dict2)
print(f"Merged dictionary: {merged_dict}")

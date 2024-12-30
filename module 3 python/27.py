'''Write a Python script to concatenate following dictionaries to create a 
new one.'''

def concatenate_dictionaries(*dicts):
    
    result_dict = {}
    for d in dicts:
        result_dict.update(d) 
    return result_dict


dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
dict3 = {'e': 5, 'f': 6}


new_dict = concatenate_dictionaries(dict1, dict2, dict3)
print(f"Concatenated dictionary: {new_dict}")

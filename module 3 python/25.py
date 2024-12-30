#Write a Python program to convert a list of tuples into a dictionary.

def list_to_dict(tuple_list):
   
    return dict(tuple_list)


tuple_list = [("a", 1), ("b", 2), ("c", 3)]
result_dict = list_to_dict(tuple_list)
print(f"Converted dictionary: {result_dict}")

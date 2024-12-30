'''Write a Python script to sort (ascending and descending) a dictionary by 
value. '''

def sort_dict_by_value(my_dict, descending=False):
   
    sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=descending))
    return sorted_dict


my_dict = {'apple': 10, 'banana': 5, 'cherry': 7, 'date': 3}


ascending_sorted_dict = sort_dict_by_value(my_dict, descending=False)
print(f"Dictionary sorted in ascending order: {ascending_sorted_dict}")


descending_sorted_dict = sort_dict_by_value(my_dict, descending=True)
print(f"Dictionary sorted in descending order: {descending_sorted_dict}")

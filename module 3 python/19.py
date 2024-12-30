#Write a Python program to convert a list to a tuple. 

def list_to_tuple(my_list):
   
    return tuple(my_list)


my_list = [10, 20, 30, 40, 50]
result_tuple = list_to_tuple(my_list)
print(f"Converted tuple: {result_tuple}")

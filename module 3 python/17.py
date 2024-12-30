'''Write a Python program to check whether an element exists within a 
tuple.'''

def element_exists_in_tuple(my_tuple, element):
   
    return element in my_tuple


my_tuple = (10, 20, 30, 40, 50)
element_to_check = 30
result = element_exists_in_tuple(my_tuple, element_to_check)

if result:
    print(f"The element {element_to_check} exists in the tuple.")
else:
    print(f"The element {element_to_check} does not exist in the tuple.")
 
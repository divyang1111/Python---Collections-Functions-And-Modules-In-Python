#Write a Python program to find the length of a tuple. 

def tuple_length(my_tuple):
   
    return len(my_tuple)


my_tuple = (10, 20, 30, 40, 50)
result = tuple_length(my_tuple)
print(f"The length of the tuple is: {result}")

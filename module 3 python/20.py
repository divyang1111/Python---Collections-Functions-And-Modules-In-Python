#Write a Python program to reverse a tuple.

def reverse_tuple(my_tuple):
    
    return my_tuple[::-1]


my_tuple = (10, 20, 30, 40, 50)
reversed_tuple = reverse_tuple(my_tuple)
print(f"Reversed tuple: {reversed_tuple}")

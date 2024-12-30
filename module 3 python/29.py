'''Write a Python script to print a dictionary where the keys are numbers 
between 1 and 15.'''

def create_dict():
   
    my_dict = {i: i**2 for i in range(1, 16)} 
    return my_dict


my_dict = create_dict()
print(my_dict)

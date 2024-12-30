#Write a Python program to find the repeated items of a tuple. 

def find_repeated_items(my_tuple):
   
    item_count = {}
    for item in my_tuple:
        if item in item_count:
            item_count[item] += 1
        else:
            item_count[item] = 1
    
   
    repeated_items = [item for item, count in item_count.items() if count > 1]
    return repeated_items


my_tuple = (1, 2, 3, 4, 5, 6, 2, 3, 7, 8, 3)
repeated_items = find_repeated_items(my_tuple)
print(f"Repeated items in the tuple: {repeated_items}")

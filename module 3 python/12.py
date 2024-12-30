#Write a Python program to check whether a list contains a sub list

def contains_sublist(main_list, sublist):
    
    sublist_len = len(sublist)
    for i in range(len(main_list) - sublist_len + 1):
        if main_list[i:i + sublist_len] == sublist:
            return True
    return False


main_list = [1, 2, 3, 4, 5, 6]
sublist = [3, 4]
result = contains_sublist(main_list, sublist)
print(f"Does the main list contain the sublist? {result}")

#Write a Python program to unzip a list of tuples into individual lists. 

def unzip_tuples(tuple_list):
   
    return list(zip(*tuple_list))


tuple_list = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
unzipped_lists = unzip_tuples(tuple_list)
print(f"Unzipped lists: {unzipped_lists}")

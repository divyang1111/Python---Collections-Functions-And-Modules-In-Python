#Write a Python program to split a list into different variables. 

def split_list_to_variables(input_list):
    
    if len(input_list) == 4: 
        var1, var2, var3, var4 = input_list
        return var1, var2, var3, var4
    else:
        return "The list must have exactly 4 elements."


my_list = [10, 20, 30, 40]
result = split_list_to_variables(my_list)

if isinstance(result, tuple):
    var1, var2, var3, var4 = result
    print(f"var1: {var1}, var2: {var2}, var3: {var3}, var4: {var4}")
else:
    print(result)

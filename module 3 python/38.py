# Write a Python program to create a dictionary from a string. 


input_string = "hello world"


char_frequency = {}


for char in input_string:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1


print("Dictionary from the string:", char_frequency)

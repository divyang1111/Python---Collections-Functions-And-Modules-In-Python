#Write a Python program to print all unique values in a dictionary.

data = {
    "key1": 10,
    "key2": 20,
    "key3": 10,
    "key4": 30,
    "key5": 20
}


unique_values = set(data.values())


print("Unique values in the dictionary are:", unique_values)

#Write a Python program to find the highest 3 values in a dictionary  


data = {
    "a": 45,
    "b": 22,
    "c": 100,
    "d": 87,
    "e": 65
}


top_3_values = sorted(data.values(), reverse=True)[:3]


print("The highest 3 values in the dictionary are:", top_3_values)

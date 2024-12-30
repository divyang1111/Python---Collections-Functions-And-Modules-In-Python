# Write a Python program to read a random line from a file. 

import random

def read_random_line(file_path):
    
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            
            random_line = random.choice(lines)
            return random_line.strip()  
    except FileNotFoundError:
        return f"Error: The file {file_path} does not exist."
    except Exception as e:
        return f"Error: {e}"


file_path = "sample.txt"  
print("Random line from the file:", read_random_line(file_path))

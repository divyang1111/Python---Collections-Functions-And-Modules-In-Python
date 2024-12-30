'''Write a Python program to generate and print a list of first and last 5 
elements where the values are square of numbers between 1 and 30.'''

def generate_square_list():
    
    squares = [x ** 2 for x in range(1, 31)]
   
    result = squares[:5] + squares[-5:]
    return result


result_list = generate_square_list()
print(f"First and last 5 elements: {result_list}")

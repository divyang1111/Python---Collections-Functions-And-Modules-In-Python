# Write a Python program to convert degree to radian  

import math

def degree_to_radian(degrees):
   
    radians = math.radians(degrees)
    return radians


degree = 45  
radian = degree_to_radian(degree)
print(f"{degree} degrees is equal to {radian} radians.")
 
 
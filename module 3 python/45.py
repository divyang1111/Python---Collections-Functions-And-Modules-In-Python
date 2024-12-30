# Write a Python program to calculate the area of a trapezoid  

def trapezoid_area(a, b, h):
    
    area = 0.5 * (a + b) * h
    return area


base1 = 5  
base2 = 7 
height = 4  

area = trapezoid_area(base1, base2, height)
print(f"The area of the trapezoid is {area} square units.")

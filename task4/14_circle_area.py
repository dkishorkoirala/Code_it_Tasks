from math import pi as p

def circle_area(radius):
    return p * radius * radius

r = float(input("Enter a radius: "))
print(circle_area(r))
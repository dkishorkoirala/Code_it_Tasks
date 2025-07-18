from math import sqrt

def get_hypotenuse(a, b):
    return sqrt(a**2 + b**2)

a = int(input("Enter a number: "))
b = int(input("Enter another number: "))

print(get_hypotenuse(a, b))
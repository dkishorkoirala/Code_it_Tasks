from math import floor , ceil

def ceil_floor(num):
    return f"FLoor: {floor(num)}\nCeil: {ceil(num)}" 

num = float(input("Enter a number: "))
print(ceil_floor(num))
from math import pow

def get_power(base, exp):
    return pow(base, exp)

base = float(input("Enter base number: "))
exp = float(input("Enter exponent: "))
print(get_power(base, exp))


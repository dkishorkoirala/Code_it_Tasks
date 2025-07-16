a = int(input("Enter a number : "))
b = int(input("Enter another number : "))

GCD = min(a,b)

while GCD > 0:
    if a % GCD == 0 and b % GCD == 0:
        print("The GCD of", a, "and", b, "is", GCD)
        break
    else:
        GCD -= 1
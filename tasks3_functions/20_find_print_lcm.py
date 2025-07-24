def find_lcm(a, b):
    lcm = max(a,b)
    while True:
        if lcm % a == 0 and lcm % b == 0:
            print("The LCM of", a, "and", b, "is", lcm)
            break
        else:
            lcm += 1

a = int(input("Enter first number: "))
b =int(input("Enter second number: "))

find_lcm(a, b)
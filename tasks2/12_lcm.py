num1 = int(input("enter a number: "))
num2 = int(input("enter another number: "))

lcm = max(num1, num2)
# lcm = 1
while True:
    if lcm % num1 == 0 and lcm % num2 == 0:
        print("The LCM of", num1, "and", num2, "is", lcm)
        break
    else:
        lcm += 1
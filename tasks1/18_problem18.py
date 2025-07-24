a = int(input("Enter a side: "))
b = int(input("Enter b side: "))
c = int(input("Enter c side: "))

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("The triangle is equilateral.")

    elif a == b or a == c or b == c:
        print("The triangle is isosceles.")
        
    else:
        print("The triangle is scalene.")
else:
    print("The triangle is not valid.")
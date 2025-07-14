a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
op = input("Enter the operation to perform(+,-,*,/): ")

if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/":
    print(a / b)
else:
    print("Invalid operation")
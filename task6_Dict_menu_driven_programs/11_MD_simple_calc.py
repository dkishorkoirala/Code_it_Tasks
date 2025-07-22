MENU = '''
1. Add
2. Subtract
3. Multiply
4. Divide
5. Exit
'''
while True: 
    print(MENU)
    choice = input("enter your choice: ")

    if choice == '1':
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        print(f"The sum of {num1} and {num2} is",num1 + num2)
    
    elif choice == "2":
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        print(f"The difference of {num1} and {num2} is",num1 - num2)
    
    elif choice == '3':
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        print(f"The multiplication of {num1} and {num2} is",num1 * num2)
        
    elif choice == "4":
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        print(f"The division of {num1} and {num2} is",num1 / num2)
        
    elif choice == "5":
        print("Thanks for using us...")
        break
    
    else:
        print("Invalid choice")
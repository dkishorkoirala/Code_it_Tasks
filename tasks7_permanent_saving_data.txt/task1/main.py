from resources import MENU, EXIT, add, sub, mul, div, write_csv, read_csv


while True:
    print(MENU)
    try: 
        choice = input("Enter your choice: ")
    except ValueError:
        print("Choice must be NUmberl: ")
    if choice == "1":
        while True:
            try: 
                a = int(input ("Enter first number: "))
                b = int(input("Enter second number: "))
            except ValueError:
                print("Both inputs must be valid integers.")
            else:
                result = add(a,b)
                print("The sum of two numbers is",add(a, b))
                write_csv("calculations.csv", ["Addition", a, b, result])
                break
            
    elif choice == "2":
        while True:
            try: 
                a = int(input ("Enter first number: "))
                b = int(input("Enter second number: "))
            except ValueError:
                print("Both inputs must be valid integers.")
            else:
                result = sub(a,b)
                print("The difference of two numbers is",sub(a, b))
                write_csv("calculations.csv", ["Subtraction", a, b, result])
                break
    elif choice == "3":
        while True:
            try: 
                a = int(input ("Enter first number: "))
                b = int(input("Enter second number: "))
            except ValueError:
                print("Both inputs must be valid integers.")
            else:
                result = mul(a,b)
                print("The product of two numbers is",mul(a, b))
                write_csv("calculations.csv", ["Multiplication", a, b, result])

                break
    elif choice == "4":
        while True:
            try: 
                a = int(input ("Enter first number: "))
                b = int(input("Enter second number: "))
                result = div(a, b)
            except ValueError:
                print("Both inputs must be valid integers.")
            except ZeroDivisionError:
                print("Cannot divide by zero")
            else:
                print("The Division of two number is",result)
                write_csv("calculations.csv",["Division", a, b, result])
                break
    elif choice == "5":
        read_csv("calculations.csv")
                
    elif choice == "6":
        print(EXIT)
        break
    
    else:
        print("Invalid choice: Try again!!")
    
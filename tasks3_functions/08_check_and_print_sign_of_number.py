def check(num):
    if num > 0:
        print("Positive Number")
    
    elif num < 0:
        print("Negative Number")
    
    else:
        print("Zero")

n = int(input("Enter your number to check: "))
check(n)
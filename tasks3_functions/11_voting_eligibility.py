def eligible(n):
    if n >= 18:
        print("You can vote")
    
    else:
        print(f"You can vote after {18-n} years")

age = int(input("Enter your age: "))
eligible(age)
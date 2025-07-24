pass_ = input("Enter password: ")

if len(pass_) >= 8:
    if pass_.isalpha():
        print("Weak password: Only letters")

    elif pass_.isdigit():
        print("Weak password: Only digits")
        
    else:
        print("Strong password")
else:
    print("Weak password: Too short")
MENU = '''
1. Check balance
2. Deposit money
3. Withdraw money
4. Exit
'''
balance = 1000
while True:
    print(MENU)
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        print(f"Your balance is {balance}")
    
    elif choice == "2":
        deposit = int(input("Enter the amount to deposit: "))
        balance += deposit
        print(f"Deposited {deposit}. Your new balance is {balance}")
    
    elif choice == "3":
        withdraw = int(input("Enter the amount to withdraw: "))
        if withdraw > balance:
            print("Insufficient balance")
        else:
            balance -= withdraw
            print(f"Withdrew {withdraw}. Your new balance is {balance}")
    
    elif choice == "4":
        print("Exiting the program....")
        break
    
    else:
        print("Invalid choice! Please Try again")
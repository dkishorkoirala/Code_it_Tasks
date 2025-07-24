fruits = ["apple", "banana", "cherry", "mango", "kiwi", "litchi"]

check = input("Enter a fruit: ").lower()
if check in fruits:
    print(f"{check} is in the list")
else:
    print(f"{check} is not in the list")
fruits = {
    "Apple" : 32,
    "mango" : 45,
    "banana" : 23,
    "grapes" : 56,
    "kiwi" : 78
}
check = input("Enter fruit to check: ").lower()

for fruit in fruits:
    if check == fruit.lower():
        print(f"{check.capitalize()} is in the list with Rs. {fruits[fruit]}")
        break
    else:
        print(f"{check} is not in the list")
        break
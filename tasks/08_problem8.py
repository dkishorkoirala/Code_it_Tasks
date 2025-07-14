char = input("Enter a character: ")

if char.isupper():
    print("The character is uppercase.")
elif char.islower():
    print("The character is lowercase.")
else:
    print("The character is neither uppercase nor lowercase, could be special character.")
    
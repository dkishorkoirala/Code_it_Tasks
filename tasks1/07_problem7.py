char = input("Enter single character: ")

if char.isalpha():
    print(f"The character {char} is an alphabet.")
elif char.isdigit():
    print(f"The character {char} is a digit.")

else:
    print(f"The character {char} is a special character.")
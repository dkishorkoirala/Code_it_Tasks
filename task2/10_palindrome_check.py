num = int(input("Enter a number: "))
rev = 0
num1 = num

while num != 0:
    rem = num % 10
    rev = 10 * rev + rem
    num = num // 10

if num1 == rev:
    print("Palindrome number")

else: 
    print("Not a palindrome number")
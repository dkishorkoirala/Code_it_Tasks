def is_palindrome(num):
    rev = 0
    temp = num
    while num != 0:
        rem = num % 10
        rev = rev * 10 + rem
        num = num // 10
    if temp == rev:
        return "Palindrome number"
    else:
        return "Not a palindrome"
    

num = int(input("Enter a number: "))
print(is_palindrome(num))
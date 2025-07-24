num = int(input("Enter a number: "))
smallest = 9
while num != 0:
    rem = num % 10    
    smallest = min(rem, smallest)
    num = num // 10

print(smallest)

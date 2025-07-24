num = int(input("Enter your number: "))

largest = 0

while num!= 0:
    rem = num % 10
    largest = max(rem, largest)
    num = num // 10

print(largest)
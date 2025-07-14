num = int(input("Enter single digit: "))

if  0 <= num <= 9:
    if num % 2 == 0:
        print("The number is single digit even number")
    else:
        print("The number is single digit odd number")
else:
    print("The number is not single digit")
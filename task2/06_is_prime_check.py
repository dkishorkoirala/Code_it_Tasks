n = int(input("Enter a number: "))

if n < 2:
    print("Number is not prime")

else:
    for i in range(2 , n):
        if (n % i) == 0 :
            print("Number is not prime")
            break

    else:
        print("Number is prime")
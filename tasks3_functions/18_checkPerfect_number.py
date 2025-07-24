def perfect_check(n):
    if n < 2:
        print("Number is not perfect")

    else: 
        sum = 0
        for i in range (1, n):
            if n % i == 0:
                sum += i

        if sum == n:
            print("Number is perfect")
        else:
            print("Number is not perfect")

n = int(input("Enter a number: "))
perfect_check(n)
def fact(num):
    fact = 1
    for i in range(num, 1, -1):
        fact *= i

    print(fact)

n = int(input("Enter a number to find factorial of : "))
fact(n)
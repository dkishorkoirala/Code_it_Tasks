def fabonacci_generator(num):
    a = 0
    b = 1
    for i in range(num):
        print(a, end = " ")
        a, b = b, a+b

n = int(input("Enter number of fabonacci series you want: "))

fabonacci_generator(n)

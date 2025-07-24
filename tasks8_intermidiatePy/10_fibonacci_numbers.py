def fibo():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


f = fibo()
n = int(input("Enter a number: "))
for i in range(n):
    print(next(f))

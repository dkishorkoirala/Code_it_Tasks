def sum_digits(num):
    sum = 0
    while num != 0:
        rem = num % 10
        sum += rem
        num = num // 10
    print(sum)

n = int(input("Enter your number: "))
sum_digits(n)
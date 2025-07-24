def sum_digits(num):
    sum = 0
    while num != 0:
        rem = num % 10
        sum += rem
        num = num // 10
    return sum

num = int(input("Enter the number: "))
print(sum_digits(num))
def armstrong_number_check(num):
    power = len(str(num))
    sum = 0
    temp = num

    while temp > 0:
        digit = temp % 10
        sum += digit ** power
        temp //= 10

    if num == sum:
        print(f"{num} is an Armstrong number.")
    else:
        print(f"{num} is not an Armstrong number.")
n = int(input("Enter a number : "))
armstrong_number_check(n)
def sum_natureal(number):
    sum = 0
    for i in range(1, number+1):
        sum += i
    print(sum)


n = int(input("Enter a number"))
sum_natureal(n)
def even_odd_counter(num):
    counter = 0
    odd_counter = 0
    while num != 0:
        rem = num % 10
        if rem % 2 == 0:
            counter += 1
        else:
            odd_counter += 1
        num = num // 10

    print("Even digit counter", counter)
    print("Odd digit counter", odd_counter)

num = int(input("Enter a number: "))
even_odd_counter(num)
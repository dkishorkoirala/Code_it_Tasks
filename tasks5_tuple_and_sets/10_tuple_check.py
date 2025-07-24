my_tuple = (1, 2, 3, 23,43,54,65,76,87)

num = int(input("Enter a number: "))
if num in my_tuple:
    print(f"{num} is present in tuple")
else:
    print(f"{num} is not present in tuple")
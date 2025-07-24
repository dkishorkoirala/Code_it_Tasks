num = int(input("Enter a number: "))
sum = 0
sumodd = 0
while num !=0:
    rem = num % 10
    if rem % 2 == 0:
        sum += rem
    else:
        sumodd += rem
    num = num // 10

print("sum of Even digit", sum)
print("sum of Odd digit", sumodd)
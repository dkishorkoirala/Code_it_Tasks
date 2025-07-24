i = []

for j in range(5):
    num = int(input("Enter a number: "))
    i.append(num)

check = int(input("Enter the number to count in list: "))
print(f"The number {check} appears:",i.count(check),"Times")
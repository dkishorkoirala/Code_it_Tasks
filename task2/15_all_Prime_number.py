start = int(input("From: "))
end = int(input("to: "))

for i in range(start, end+1):
    if i < 2:
        print(f"{i} : Number is not prime")

    else:
        for j in range(2, i):
            if i % j == 0:
                print(f"{i} : Number is not prime")
                break

        else:
            print(f"{i} : Number is prime")
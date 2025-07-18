def is_prime(n):
    if n <=1 :
        return "False its not prime"
    else:
        for i in range(2, n):
            if n % i == 0:
                return "False its not prime"
        else:
            return "True its prime"

num = int(input("Enter a prime number: "))
print(is_prime(num))
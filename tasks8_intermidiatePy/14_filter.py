def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


a = [2, 3, 4, 5, 6, 7, 8, 9, 10]
b = list(filter(is_prime, a))
print(b)

def get_gcd(a, b):
    gcd = min(a, b)

    
    while gcd > 0:
        if a % gcd == 0 and b % gcd == 0:
            return gcd
            
        gcd -= 1

    return gcd

a = int(input("Enter a number: "))
b = int(input("Enter another number: "))

print(get_gcd(a, b))
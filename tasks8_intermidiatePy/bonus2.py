import random


def log(func):
    def wrapper(*args, **kwargs):
        print(f"Generator {func.__name__} is being used...")
        return func(*args, **kwargs)

    return wrapper


@log
def random_gen(n=10):
    for _ in range(n):
        yield random.randint(1, 100)


obj = random_gen(10)
# print(next(obj))

odd_numbers = filter(lambda x: x % 2 == 1, obj)
odd_squares = list(map(lambda x: x**2, odd_numbers))

# num = list(obj)
# print(num)
print(odd_squares)

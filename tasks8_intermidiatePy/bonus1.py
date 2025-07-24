import random


def random_():
    yield random.randint(1, 100)


obj = random_()
print(next(obj))
